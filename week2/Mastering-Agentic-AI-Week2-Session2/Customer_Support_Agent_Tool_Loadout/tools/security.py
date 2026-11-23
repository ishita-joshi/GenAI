from langchain_core.tools import tool
from typing import Any

@tool("two_factor_reset")
def two_factor_reset(user_id: str) -> dict[str, Any]:
    """Reset 2FA after identity checks.
    
    Args:
        user_id: The unique identifier for the user.
        
    Returns:
        A dictionary with 'ok' status, user_id, and reset status message.
    """
    return {"ok": True, "user_id": user_id, "status": "2FA reset initiated"}