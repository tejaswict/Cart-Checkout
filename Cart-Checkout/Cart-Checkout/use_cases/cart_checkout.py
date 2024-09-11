from typing import List
from entities.checkout import Checkout, PricingRules
from entities.product import ProductRepository


class CheckoutUseCase:
    """
    The use case for handling the checkout process,
    including applying pricing rules.

    Attributes:
        pricing_rules (PricingRules): The pricing rules applied
        to the checkout.
        product_repository (ProductRepository):
        Repository for fetching product data.
    """

    def __init__(self, pricing_rules: "PricingRules", product_repository: "ProductRepository") -> None:
        self.pricing_rules = pricing_rules
        self.product_repository = product_repository

    def execute(self, scanned_items: List[str]) -> float:
        """
        Executes the checkout process,
        calculating the total price for scanned items.

        """
        # Fetch all products from the repository
        products = self.product_repository.get_all_products()
        catalog = {product.sku: product for product in products}

        # Process the checkout
        checkout = Checkout(self.pricing_rules)
        for item in scanned_items:
            checkout.scan(item)

        return checkout.total(catalog)
