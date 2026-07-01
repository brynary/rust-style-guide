# Smart Pointers and Interior Mutability

## Rule

Prefer ordinary ownership first; use `Arc` for shared ownership, `Mutex` or `RwLock` for real shared mutable state, and channels for ownership transfer.

## Why

Rust's ownership model is usually the simplest concurrency and mutation model. Smart pointers and interior mutability are useful when ownership really is shared or mutation must happen through a shared handle, but they add coordination costs and failure modes.

## Do

- Use owned values and borrowing before introducing smart pointers.
- Use `Box<T>` for recursive data, large enum variants, or single-owner heap allocation.
- Use `Box<dyn Trait>` for owned dynamic dispatch when one owner is enough.
- Use `Rc<T>` only for single-threaded shared ownership.
- Use `Arc<T>` for shared ownership across threads or Tokio tasks.
- Use `Weak` (`std::rc::Weak` or `std::sync::Weak`) to break parent-child or observer cycles.
- Use `.clone()` consistently for `Rc`, `Arc`, and ordinary cloned values.
- Use `Mutex<T>` for shared mutable state with short critical sections.
- Use `RwLock<T>` only when many readers and few writers make that extra complexity worthwhile.
- Use channels when a value should move to an owner that processes messages or events.
- Use `OnceLock` or `LazyLock` for one-time initialization.
- Keep lock scopes small and copy out owned data before slow work.

## Avoid

- Do not use `Arc<Mutex<T>>` as the default way to avoid ownership design.
- Do not use `Rc` or `RefCell` in multi-threaded code.
- Do not create `Rc` or `Arc` cycles; two strong references pointing at each other are never freed and leak the whole graph.
- Do not use `RefCell` when a normal `&mut self` API would work.
- Do not hold locks across blocking I/O, callbacks, or `.await` points.
- Do not choose `RwLock` just because reads are common; start with `Mutex` unless contention matters.
- Do not create global mutable state unless initialization and access rules are clear.
- Do not take multiple locks without a documented lock ordering.

## Async Notes

In Tokio code, use `tokio::sync` primitives when waiting for the lock must not block the runtime or when a guard may intentionally live across an `.await`. Prefer structuring code so lock guards are dropped before `.await`.

Use standard-library locks for synchronous code and short non-async critical sections.

## Pointer and Thread-Safety Table

| Need | Prefer | Thread-safe use |
| --- | --- | --- |
| Single owner, heap allocation | `Box<T>` | Movable across threads when `T: Send` |
| Single-thread shared ownership | `Rc<T>` | No; use only on one thread |
| Cross-thread shared ownership | `Arc<T>` | Yes when `T: Send + Sync` |
| Single-thread interior mutation | `Cell<T>` or `RefCell<T>` | No; use only on one thread |
| Shared mutable state | `Mutex<T>` | Yes when `T: Send` and critical sections stay short |
| Read-heavy shared state | `RwLock<T>` | Yes when `T: Send + Sync` and contention justifies it |
| One-time initialization | `OnceLock<T>` or `LazyLock<T>` | Yes when the initialized value is thread-safe |
| Ownership transfer | Channel | Yes when sent values are `Send` |

## Example

```rust
use std::{
    sync::{mpsc, Arc, Mutex},
    thread,
};

#[derive(Clone, Debug)]
pub struct SharedMetrics {
    inner: Arc<Mutex<Metrics>>,
}

impl SharedMetrics {
    pub fn new() -> Self {
        Self {
            inner: Arc::new(Mutex::new(Metrics::default())),
        }
    }

    pub fn record(&self, event: Event) {
        let mut metrics = self.inner.lock().expect("metrics mutex poisoned");
        metrics.record(event);
    }

    pub fn snapshot(&self) -> Metrics {
        self.inner
            .lock()
            .expect("metrics mutex poisoned")
            .clone()
    }
}

impl Default for SharedMetrics {
    fn default() -> Self {
        Self::new()
    }
}

#[derive(Clone, Copy, Debug, Eq, PartialEq)]
pub enum Event {
    Success,
    Failure,
}

#[derive(Clone, Debug, Default, Eq, PartialEq)]
pub struct Metrics {
    pub successes: usize,
    pub failures:  usize,
}

impl Metrics {
    pub fn record(&mut self, event: Event) {
        match event {
            Event::Success => self.successes += 1,
            Event::Failure => self.failures += 1,
        }
    }
}

pub fn spawn_metrics_collector() -> (mpsc::Sender<Event>, thread::JoinHandle<Metrics>) {
    let (sender, receiver) = mpsc::channel();

    let handle = thread::spawn(move || {
        let mut metrics = Metrics::default();

        for event in receiver {
            metrics.record(event);
        }

        metrics
    });

    (sender, handle)
}
```

## Exceptions

- Use `Cell` or `RefCell` for narrow single-threaded caches, adapters, tests, or APIs where runtime borrow checking is genuinely simpler.
- Use `Arc<Mutex<T>>` directly when shared mutable state is the simple domain model.
- Use `RwLock` when profiling or domain knowledge shows read contention matters.
- Use channels even for same-thread code when ownership transfer makes control flow clearer.
