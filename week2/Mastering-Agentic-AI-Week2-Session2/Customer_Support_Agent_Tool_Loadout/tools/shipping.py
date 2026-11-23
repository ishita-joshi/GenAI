from langchain_core.tools import tool
from typing import Any

@tool("shipping_status")
def shipping_status(order_id: str) -> dict[str, Any]:
    # Mock status
    """Track current shipment status for order_id.
    
    Args:
        order_id: The unique identifier for the order.
        
    Returns:
        A dictionary containing the order_id, current shipping status, and ETA.
    """
    return {"order_id": order_id, "status": "in_transit", "eta": "2025-11-05"}

@tool("shipping_update_address")
def shipping_update_address(order_id: str, new_address: str) -> dict[str, Any]:
    """Update shipping address before dispatch.
    
    Args:
        order_id: The unique identifier for the order.
        new_address: The new shipping address.
        
    Returns:
        A dictionary with 'ok' status, order_id, and the updated address.
    """
    return {"ok": True, "order_id": order_id, "new_address": new_address}