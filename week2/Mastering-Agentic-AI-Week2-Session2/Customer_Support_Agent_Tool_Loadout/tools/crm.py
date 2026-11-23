from langchain_core.tools import tool
from typing import Any, cast
from data.mock_stores import MOCK_CRM


@tool("crm_lookup")
def crm_lookup(user_id: str) -> dict[str, Any]:
    """Retrieve CRM profile (name, tier, tickets) by user_id.
    
    Args:
        user_id: The unique identifier for the user.
        
    Returns:
        A dictionary containing the user_id and their CRM profile information,
        including name, tier, tickets, and other relevant data.
    """
    return {"user_id": user_id, "profile": MOCK_CRM.get(user_id)}


@tool("add_note_to_crm")
def add_note_to_crm(user_id: str, note: str) -> dict[str, Any]:
    """Append a note onto user's CRM profile.
    
    Args:
        user_id: The unique identifier for the user.
        note: The note text to append to the CRM profile.
        
    Returns:
        A dictionary with 'ok' status and the updated list of notes, or an error
        if the user is not found.
    """
    prof = MOCK_CRM.get(user_id)
    if not prof:
        return {"ok": False, "error": "user not found"}
    prof_any: dict[str, Any] = cast(dict[str, Any], prof)
    if "notes" not in prof_any:
        prof_any["notes"] = []
    prof_any["notes"].append(note)
    return {"ok": True, "notes": prof_any["notes"]}


@tool("verify_email")
def verify_email(user_id: str, email: str) -> dict[str, Any]:
    """Verify if an email belongs to user_id.
    
    Args:
        user_id: The unique identifier for the user.
        email: The email address to verify.
        
    Returns:
        A dictionary with 'ok' status indicating whether the email matches
        the user's registered email in the CRM.
    """
    prof = MOCK_CRM.get(user_id)
    return {"ok": bool(prof and prof.get("email") == email)}


@tool("update_email")
def update_email(user_id: str, new_email: str) -> dict[str, Any]:
    """Update email in CRM for user_id.
    
    Args:
        user_id: The unique identifier for the user.
        new_email: The new email address to update.
        
    Returns:
        A dictionary with 'ok' status and the updated email, or an error
        if the user is not found.
    """
    prof = MOCK_CRM.get(user_id)
    if not prof:
        return {"ok": False, "error": "user not found"}
    prof["email"] = new_email
    return {"ok": True, "email": new_email}