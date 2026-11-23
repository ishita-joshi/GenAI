from langchain_core.tools import tool
from typing import Any
from datetime import datetime, timezone
from config import RETURN_POLICY_DAYS
from data.mock_stores import MOCK_ORDERS

@tool("refund_policy_check")
def refund_policy_check(delivery_date: str) -> dict[str, Any]:
    """Check return eligibility window by delivery_date.
    
    Args:
        delivery_date: The delivery date in YYYY-MM-DD format.
        
    Returns:
        A dictionary with 'ok' status, days since delivery, the policy window,
        and eligibility status.
    """
    try:
        delivered = datetime.strptime(delivery_date, "%Y-%m-%d").replace(tzinfo=timezone.utc)
    except Exception as e:
        return {"ok": False, "error": str(e)}
    days_since = (datetime.now(timezone.utc) - delivered).days
    return {"ok": True, "days_since_delivery": days_since, "window_days": RETURN_POLICY_DAYS, "eligible": days_since <= RETURN_POLICY_DAYS}

@tool("create_refund_ticket")
def create_refund_ticket(order_id: str, reason: str) -> dict[str, Any]:
    # Minimal mock
    """Create a refund ticket for an order with the specified reason.
    
    Args:
        order_id: The unique identifier for the order.
        reason: The reason for the refund request.
        
    Returns:
        A dictionary with 'ok' status, refund ticket_id, and reason.
    """
    return {"ok": True, "ticket_id": f"R-{order_id}", "reason": reason}