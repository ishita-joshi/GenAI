from langchain_core.tools import tool
from typing import Any

@tool("recommend_product")
def recommend_product(user_id: str) -> dict[str, Any]:
    """Recommend products based on recent purchases.
    
    Args:
        user_id: The unique identifier for the user.
        
    Returns:
        A dictionary with 'ok' status, user_id, and list of recommended products.
    """
    return {"ok": True, "user_id": user_id, "top_picks": ["Silicone Case", "USB‑C Cable", "Screen Guard"]}
