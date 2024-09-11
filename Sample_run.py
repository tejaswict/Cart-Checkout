from use_cases.cart_checkout import CheckoutUseCase
from entities.product import ProductRepository
from entities.pricing_rules import PricingRules
from infrastructure.db import SessionLocal

# Initialize the database session
db_session = SessionLocal()

# Initialize repositories and use cases
product_repository = ProductRepository(db_session)
pricing_rules = PricingRules()

# Checkout use case
checkout_use_case = CheckoutUseCase(pricing_rules, product_repository)

# Example: Scanning items
# scanned_items = ['atv', 'atv', 'atv', 'vga']
# scanned_items = ['atv', 'ipd', 'ipd', 'atv', 'ipd', 'ipd', 'ipd']
scanned_items = ["mbp", "vga", "ipd"]
total_price = checkout_use_case.execute(scanned_items)
print(f"Total Price: ${total_price:.2f}")
