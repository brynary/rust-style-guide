# Enums vs Traits

## Rule

Use enums for closed sets you own, traits for open extension points, and trait objects only when runtime heterogeneity is required.

## Why

Enums give exhaustive handling and simple control flow. Traits let other code provide new implementations. Trait objects add indirection, so use them when the flexibility is worth it.

## Do

- Use an enum when all variants are known and controlled by this crate.
- Use a trait when downstream code should provide new behavior.
- Use generics when static dispatch and compile-time type knowledge are useful.
- Use `Box<dyn Trait>` or `Arc<dyn Trait>` for heterogeneous collections or dependency injection.
- Keep traits small and behavior-focused.

## Avoid

- Do not emulate inheritance hierarchies with traits.
- Do not create a trait for a closed set just because the design feels object-oriented.
- Do not expose a large public trait with many unrelated methods.
- Do not use `dyn Trait` in tight loops without a reason.

## Example: Closed Set

```rust
pub enum PaymentMethod {
    Card(CardPayment),
    BankTransfer(BankTransfer),
}

impl PaymentMethod {
    pub fn risk_score(&self) -> u8 {
        match self {
            Self::Card(card) => card.risk_score(),
            Self::BankTransfer(transfer) => transfer.risk_score(),
        }
    }
}
```

## Example: Open Extension Point

```rust
pub trait PaymentProcessor {
    fn authorize(&self, payment: PaymentRequest) -> Result<Authorization, PaymentError>;
}

pub struct Checkout<P> {
    processor: P,
}

impl<P: PaymentProcessor> Checkout<P> {
    pub fn submit(&self, request: PaymentRequest) -> Result<Authorization, PaymentError> {
        self.processor.authorize(request)
    }
}
```

## Exceptions

- Use `dyn Trait` at architectural boundaries when concrete types are selected at runtime.
- Use an enum wrapper around trait implementors when performance and exhaustive matching matter more than open extension.
- Use sealed traits when callers should consume behavior but not implement it.

## Decision Points

- Default polymorphism bias: enum-first, trait-first, or `dyn Trait`-heavy.
- Whether public extension points should be sealed.
- Whether architecture boundaries should prefer generics or trait objects.
