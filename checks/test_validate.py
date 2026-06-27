#!/usr/bin/env python3
import importlib.util
import pathlib
import tempfile
import unittest


ROOT = pathlib.Path(__file__).resolve().parents[1]
VALIDATE = ROOT / "checks" / "validate.py"


def load_validate():
    spec = importlib.util.spec_from_file_location("validate", VALIDATE)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def write(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.strip() + "\n", encoding="utf-8")


GUIDELINE = """
# Topic

## Rule

Use the rule.

## Why

Because it matters.

## Do

- Do this.

## Avoid

- Avoid that.

## Example

```rust
fn main() {}
```

## Exceptions

- None.
"""


WORKFLOW = """
# Workflow

## Required Guidelines

Load [guidelines.md](../guidelines.md).

## Workflow

1. Do the work.

## Avoid

- Avoid shortcuts.
"""


SKILL = """
---
name: example
---

# Skill

## First Steps

Load [root.md](root.md).

## Routing Examples

| Task | Load |
| --- | --- |
| Topic | [Topic](guidelines/topic.md) |
| Workflow | [Workflow](workflows/workflow.md) |

## Core Behavior

- Use the guide.
"""


ROOT_DOC = """
# Root

## Supporting Files

- [guidelines.md](guidelines.md)
- [workflow](workflows/workflow.md)

## Routing Examples

| Task | Load |
| --- | --- |
| Topic | [Topic](guidelines/topic.md) |
| Workflow | [Workflow](workflows/workflow.md) |

## Core Behavior

- Use the guide.
"""


class ValidateTests(unittest.TestCase):
    def test_valid_skill_tree_passes(self):
        validate = load_validate()

        with tempfile.TemporaryDirectory() as tmp:
            root = pathlib.Path(tmp)
            write(root / "SKILL.md", SKILL)
            write(root / "root.md", ROOT_DOC)
            write(root / "guidelines.md", "[Topic](guidelines/topic.md)")
            write(root / "guidelines" / "topic.md", GUIDELINE)
            write(root / "workflows" / "workflow.md", WORKFLOW)

            result = validate.validate(root)

        self.assertEqual([], result.errors)

    def test_reports_broken_links_and_missing_index_entries(self):
        validate = load_validate()

        with tempfile.TemporaryDirectory() as tmp:
            root = pathlib.Path(tmp)
            write(root / "SKILL.md", "[Missing](guidelines/missing.md)")
            write(root / "root.md", "")
            write(root / "guidelines.md", "")
            write(root / "guidelines" / "topic.md", GUIDELINE)
            write(root / "workflows" / "workflow.md", WORKFLOW)

            result = validate.validate(root)

        self.assertTrue(any("broken link" in error for error in result.errors))
        self.assertTrue(any("guidelines.md does not list guidelines/topic.md" in error for error in result.errors))
        self.assertTrue(any("root.md does not link workflows/workflow.md" in error for error in result.errors))

    def test_rust_blocks_are_extracted_and_empty_blocks_fail(self):
        validate = load_validate()

        with tempfile.TemporaryDirectory() as tmp:
            root = pathlib.Path(tmp)
            write(root / "SKILL.md", SKILL)
            write(root / "root.md", ROOT_DOC)
            write(root / "guidelines.md", "[Topic](guidelines/topic.md)")
            write(root / "guidelines" / "topic.md", GUIDELINE.replace("fn main() {}", ""))
            write(root / "workflows" / "workflow.md", WORKFLOW)

            result = validate.validate(root)

        self.assertEqual(1, result.rust_block_count)
        self.assertTrue(any("empty rust block" in error for error in result.errors))


if __name__ == "__main__":
    unittest.main()
