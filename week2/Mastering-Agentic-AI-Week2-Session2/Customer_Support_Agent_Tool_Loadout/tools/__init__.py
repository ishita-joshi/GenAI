from dataclasses import dataclass
from langchain_core.tools import BaseTool

# Import all individual tool modules (each defines a @tool)
from .faq import faq_search
from .crm import crm_lookup, add_note_to_crm, update_email, verify_email
from .payments import payment_history_lookup, resend_invoice
from .orders import order_status, cancel_order
from .refunds import refund_policy_check, create_refund_ticket  # noqa: F401
from .shipping import shipping_status, shipping_update_address
from .tickets import escalate_ticket, create_ticket, list_open_tickets, close_ticket
from .loyalty import loyalty_points, apply_coupon
from .recommendations import recommend_product
from .warranty import check_warranty, extend_warranty
from .giftcards import giftcard_balance, block_giftcard
from .security import two_factor_reset

@dataclass
class ToolCard:
    name: str
    description: str
    handle: BaseTool

# Catalog of 25 tools (name, semantic-search description, callable handle)
catalog: list[ToolCard] = [
    ToolCard("faq_search", "Search FAQ KB for returns, refunds, charges, how‑tos.", faq_search),
    ToolCard("crm_lookup", "Retrieve CRM profile (name, tier, tickets) by user_id.", crm_lookup),
    ToolCard("payment_history_lookup", "List payment history for a user_id.", payment_history_lookup),
    ToolCard("order_status", "Get fulfillment & delivery details for order_id.", order_status),
    ToolCard("refund_policy_check", "Check return eligibility window by delivery_date.", refund_policy_check),
    ToolCard("create_refund_ticket", "Open a refund ticket for an order with a reason.", create_refund_ticket),
    ToolCard("shipping_status", "Track current shipment status for order_id.", shipping_status),
    ToolCard("shipping_update_address", "Update shipping address before dispatch.", shipping_update_address),
    ToolCard("escalate_ticket", "Escalate a support ticket to L2/L3.", escalate_ticket),
    ToolCard("create_ticket", "Create a new support ticket for a user.", create_ticket),
    ToolCard("list_open_tickets", "List open tickets for a user.", list_open_tickets),
    ToolCard("close_ticket", "Close a ticket if the issue is resolved.", close_ticket),
    ToolCard("loyalty_points", "Fetch user's loyalty/points balance.", loyalty_points),
    ToolCard("apply_coupon", "Validate/apply a coupon to an order.", apply_coupon),
    ToolCard("resend_invoice", "Resend invoice for an order to user's email.", resend_invoice),
    ToolCard("verify_email", "Verify if an email belongs to user_id.", verify_email),
    ToolCard("update_email", "Update email in CRM for user_id.", update_email),
    ToolCard("add_note_to_crm", "Append a note onto user's CRM profile.", add_note_to_crm),
    ToolCard("recommend_product", "Recommend products based on recent purchases.", recommend_product),
    ToolCard("check_warranty", "Check warranty coverage for order_id.", check_warranty),
    ToolCard("extend_warranty", "Extend warranty for eligible products.", extend_warranty),
    ToolCard("giftcard_balance", "Check gift card balance by code.", giftcard_balance),
    ToolCard("block_giftcard", "Block a compromised gift card.", block_giftcard),
    ToolCard("cancel_order", "Attempt to cancel an order before shipment.", cancel_order),
    ToolCard("two_factor_reset", "Reset 2FA after identity checks.", two_factor_reset),
]