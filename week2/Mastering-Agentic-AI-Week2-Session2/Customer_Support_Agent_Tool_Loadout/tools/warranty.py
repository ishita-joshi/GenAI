from langchain_core.tools import tool
from typing import Any
from data.mock_stores import MOCK_WARRANTY

@tool("check_warranty")
def check_warranty(order_id: str) -> dict[str, Any]:
    """Check warranty coverage for order_id.
    
    Args:
        order_id: The unique identifier for the order.
        
    Returns:
        A dictionary containing the order_id and warranty coverage information.
    """
    return {"order_id": order_id, "warranty": MOCK_WARRANTY.get(order_id)}

@tool("extend_warranty")
def extend_warranty(order_id: str, months: int = 12) -> dict[str, Any]:
    """Extend warranty for eligible products.
    
    Args:
        order_id: The unique identifier for the order.
        months: Number of months to extend warranty, defaults to 12.
        
    Returns:
        A dictionary with 'ok' status, order_id, and extended months.
    """
    return {"ok": True, "order_id": order_id, "extended_months": months}
