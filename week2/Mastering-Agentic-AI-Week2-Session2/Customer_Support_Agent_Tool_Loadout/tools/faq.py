# pyright: reportUnknownParameterType=false, reportUnknownVariableType=false, reportUnknownMemberType=false, reportGeneralTypeIssues=false, reportUnknownArgumentType=false
from langchain_core.tools import tool
from typing import Any


FAQ_KB = [
    ("How do I start a return?", "Initiate a return from Orders page within 30 days of delivery."),
    ("When do refunds show up?", "Refunds typically appear 5‑7 business days after processing."),
    ("What if I was double charged?", "Contact support with order ID; we'll verify logs and refund if needed."),
]


@tool("faq_search", return_direct=False)
def faq_search(q: str) -> dict[str, Any]:
    """Search the FAQ knowledge base for matching entries.
    
    Performs a simple token-based search by counting how many words from the query
    appear in each FAQ entry (both title and answer). Returns the top 3 matches
    sorted by score in descending order.
    
    Args:
        q: The search query string.
        
    Returns:
        A dictionary with a 'matches' key containing a list of up to 3 FAQ entries.
        Each entry has 'title', 'answer', and 'score' keys.
    """
    hits = []
    ql = q.lower()
    for title, ans in FAQ_KB:
        score = sum(1 for tok in ql.split() if tok in (title + " " + ans).lower())
        if score:
            hits.append({"title": title, "answer": ans, "score": score})
    hits.sort(key=lambda x: x["score"], reverse=True)
    return {"matches": hits[:3]}



