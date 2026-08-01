# Payment service convention

- Shipping surcharge values belong in `services/payments/policy.py` as named constants.
- Boolean behavior switches added to public functions are keyword-only and default to the previous behavior.
- `pricing.py` owns fee calculation; `summary.py` may format the calculated result but must not duplicate fee policy.
