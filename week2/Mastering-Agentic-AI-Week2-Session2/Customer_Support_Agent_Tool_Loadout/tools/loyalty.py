from langchain_core.tools import tool
from typing import Any

@tool("loyalty_points")
def loyalty_points(user_id: str) -> dict[str, Any]:
    # Demo value
    """Fetch user's loyalty/points balance.
    
    Args:
        user_id: The unique identifier for the user.
        
    Returns:
        A dictionary containing the user_id and their loyalty points balance.
    """
    return {"user_id": user_id, "points": 4200}

@tool("apply_coupon")
def apply_coupon(order_id: str, code: str) -> dict[str, Any]:
    """Validate/apply a coupon to an order.
    
    Args:
        order_id: The unique identifier for the order.
        code: The coupon code to apply.
        
    Returns:
        A dictionary with 'ok' status, order_id, code, and discount amount.
    """
    return {"ok": True, "order_id": order_id, "code": code, "discount": 150}