from langchain_core.tools import tool
from typing import Any
from data.mock_stores import MOCK_GIFTCARDS

@tool("giftcard_balance")
def giftcard_balance(code: str) -> dict[str, Any]:
    """Check gift card balance by code.
    
    Args:
        code: The gift card code.
        
    Returns:
        A dictionary containing the code and gift card information including
        balance and currency.
    """
    return {"code": code, "info": MOCK_GIFTCARDS.get(code, {"balance": 0, "currency": "INR"})}

@tool("block_giftcard")
def block_giftcard(code: str) -> dict[str, Any]:
    """Block a compromised gift card.
    
    Args:
        code: The gift card code to block.
        
    Returns:
        A dictionary with 'ok' status, code, and blocked confirmation.
    """
    return {"ok": True, "code": code, "blocked": True}