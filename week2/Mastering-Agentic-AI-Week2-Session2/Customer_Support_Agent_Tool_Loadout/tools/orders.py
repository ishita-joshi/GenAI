from langchain_core.tools import tool
from typing import Any
from data.mock_stores import MOCK_ORDERS


@tool("order_status")
def order_status(order_id: str) -> dict[str, Any]:
    """Get fulfillment & delivery details for order_id.
    
    Args:
        order_id: The unique identifier for the order.
        
    Returns:
        A dictionary containing the order_id and its current status information.
    """
    return {"order_id": order_id, "status": MOCK_ORDERS.get(order_id)}


@tool("cancel_order")
def cancel_order(order_id: str) -> dict[str, Any]:
    # Simplified: allow cancel if delivery not done
    """Attempt to cancel an order before shipment.
    
    Args:
        order_id: The unique identifier for the order.
        
    Returns:
        A dictionary with 'ok' status and cancellation details, or an error
        if the order is not found or already delivered.
    """
    data = MOCK_ORDERS.get(order_id)
    if not data:
        return {"ok": False, "error": "order not found"}
    if data.get("delivered"):
        return {"ok": False, "reason": "already delivered"}
    return {"ok": True, "order_id": order_id, "canceled": True}