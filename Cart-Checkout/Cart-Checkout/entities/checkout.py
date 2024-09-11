from typing import List, Dict
from .pricing_rules import PricingRules
from .product import Product


class Checkout:
    """
    Handles scanning of items and calculates the total price based on pricing rules.

    Attributes:
        pricing_rules (PricingRules): The pricing rules applied to the checkout.
        items (List[str]): List of scanned item SKUs.
    """

    def __init__(self, pricing_rules: "PricingRules") -> None:
        """
        Initialize a Checkout instance.

        Args:
            pricing_rules (PricingRules): Pricing rules applied to the checkout.
        """
        self.pricing_rules = pricing_rules
        self.items = []

    def scan(self, item_sku: str) -> None:
        """
        Scans an item by adding its SKU to the items list.

        Args:
            item_sku (str): The SKU of the item to scan.
        """
        self.items.append(item_sku)

    def total(self, catalog: Dict[str, Product]) -> float:
        """
        Calculates the total price based on scanned items and pricing rules.

        Args:
            catalog (Dict[str, Product]): The catalog of products.

        Returns:
            float: The total price for all scanned items.
        """
        return self.pricing_rules.apply(self.items, catalog)
