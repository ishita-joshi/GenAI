from langchain_core.tools import tool
from typing import Any
from data.mock_stores import MOCK_TICKETS

@tool("escalate_ticket")
def escalate_ticket(ticket_id: str, level: str = "L2") -> dict[str, Any]:
    """Escalate a support ticket to L2/L3.
    
    Args:
        ticket_id: The unique identifier for the ticket.
        level: The escalation level, defaults to 'L2'.
        
    Returns:
        A dictionary with 'ok' status, ticket_id, and escalation level.
    """
    return {"ok": True, "ticket_id": ticket_id, "level": level}

@tool("create_ticket")
def create_ticket(user_id: str, topic: str, details: str) -> dict[str, Any]:
    """Create a new support ticket for a user.
    
    Args:
        user_id: The unique identifier for the user.
        topic: The topic or category of the ticket.
        details: Additional details about the issue.
        
    Returns:
        A dictionary with 'ok' status and the newly created ticket_id.
    """
    tid = f"T-{abs(hash(topic+user_id))%10000}"
    MOCK_TICKETS.setdefault(user_id, []).append({"ticket_id": tid, "status": "open", "topic": topic})
    return {"ok": True, "ticket_id": tid}

@tool("list_open_tickets")
def list_open_tickets(user_id: str) -> dict[str, Any]:
    """List open tickets for a user.
    
    Args:
        user_id: The unique identifier for the user.
        
    Returns:
        A dictionary containing the user_id and list of open tickets.
    """
    return {"user_id": user_id, "tickets": MOCK_TICKETS.get(user_id, [])}

@tool("close_ticket")
def close_ticket(ticket_id: str) -> dict[str, Any]:
    """Close a ticket if the issue is resolved.
    
    Args:
        ticket_id: The unique identifier for the ticket.
        
    Returns:
        A dictionary with 'ok' status, ticket_id, and closed confirmation.
    """
    return {"ok": True, "ticket_id": ticket_id, "closed": True}