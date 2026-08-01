import unittest

from services.payments.pricing import shipping_fee_cents
from services.payments.summary import order_summary


class PaymentTest(unittest.TestCase):
    def test_existing_shipping_fee_is_unchanged(self) -> None:
        self.assertEqual(shipping_fee_cents(), 500)

    def test_existing_summary_is_unchanged(self) -> None:
        self.assertEqual(
            order_summary("order-1"),
            {
                "order_id": "order-1",
                "shipping_fee_cents": 500,
            },
        )


if __name__ == "__main__":
    unittest.main()
