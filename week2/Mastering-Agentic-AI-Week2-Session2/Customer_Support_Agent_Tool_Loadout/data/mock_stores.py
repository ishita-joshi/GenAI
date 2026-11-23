MOCK_CRM = {
"user_123": {"name": "Anita Rao", "email": "anita@example.com", "tier": "GOLD", "open_tickets": 1},
"user_456": {"name": "Rohit Sharma", "email": "rohit@example.com", "tier": "SILVER", "open_tickets": 0},
}


MOCK_PAYMENTS = {
"user_123": [
{"order_id": "A1001", "amount": 1299.0, "status": "captured", "ts": "2025-10-10"},
{"order_id": "A1022", "amount": 1299.0, "status": "refunded", "ts": "2025-10-12"},
{"order_id": "A1099", "amount": 649.0, "status": "captured", "ts": "2025-10-28"},
],
"user_456": [
{"order_id": "B2001", "amount": 2499.0, "status": "captured", "ts": "2025-09-30"},
],
}


MOCK_ORDERS = {
"A1001": {"item": "Wireless Earbuds X2", "delivered": True, "delivery_date": "2025-10-12"},
"A1022": {"item": "Wireless Earbuds X2", "delivered": True, "delivery_date": "2025-10-13"},
"A1099": {"item": "Phone Case (Graphite)", "delivered": True, "delivery_date": "2025-10-31"},
"B2001": {"item": "Smartwatch Z", "delivered": True, "delivery_date": "2025-10-05"},
}


MOCK_TICKETS = {
"user_123": [
{"ticket_id": "T-9001", "status": "open", "topic": "Delayed refund"}
],
"user_456": [],
}


MOCK_WARRANTY = {
"A1001": {"months": 12, "expires": "2026-10-12"},
"B2001": {"months": 12, "expires": "2026-10-05"},
}


MOCK_GIFTCARDS = {
"GC-111": {"balance": 500.0, "currency": "INR"},
}