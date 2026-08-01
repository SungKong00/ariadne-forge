from .pricing import shipping_fee_cents


def order_summary(order_id: str) -> dict[str, object]:
    return {"order_id": order_id, "shipping_fee_cents": shipping_fee_cents()}
