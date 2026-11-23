from langchain_core.tools import tool
from typing import Any
from data.mock_stores import MOCK_PAYMENTS


@tool("payment_history_lookup")
def payment_history_lookup(user_id: str) -> dict[str, Any]:
    """List payment events for a user_id.
    
    Args:
        user_id: The unique identifier for the user.
        
    Returns:
        A dictionary containing the user_id and list of payment history records.
    """
    return {"user_id": user_id, "payments": MOCK_PAYMENTS.get(user_id, [])}


@tool("resend_invoice")
def resend_invoice(order_id: str, to_email: str) -> dict[str, Any]:
    """Resend invoice for an order to user's email.
    
    Args:
        order_id: The unique identifier for the order.
        to_email: The email address to send the invoice to.
        
    Returns:
        A dictionary with 'ok' status, the email sent to, and order_id.
    """
    return {"ok": True, "sent_to": to_email, "order_id": order_id}