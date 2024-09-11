from typing import List, Dict
from .product import Product


class PricingRules:
    """
    Represents the pricing rules applied during checkout.
    Handles special pricing logic such as discounts and bundles.
    """

    def apply(self, items: List[str], catalog: Dict[str, Product]) -> float:
        """
        Applies the pricing rules to the scanned items and calculates the total price.

        Args:
            items (List[str]): List of scanned item SKUs.
            catalog (Dict[str, Product]): The product catalog.

        Returns:
            float: The total price after applying the pricing rules.
        """
        total = 0
        counts = {sku: items.count(sku) for sku in set(items)}

        # 3-for-2 deal on Apple TVs
        if "atv" in counts:
            total += (counts["atv"] // 3) * 2 * catalog["atv"].price
            total += (counts["atv"] % 3) * catalog["atv"].price

        # Bulk discount on Super iPads
        if "ipd" in counts:
            if counts["ipd"] > 4:
                total += counts["ipd"] * 499.99  # Discounted price for more than 4
            else:
                total += counts["ipd"] * catalog["ipd"].price

        # MacBook Pro with free VGA adapter
        if "mbp" in counts:
            total += counts["mbp"] * catalog["mbp"].price
            if "vga" in counts:
                counts["vga"] -= counts["mbp"]  # Free VGA adapters for each MBP sold

        # Add remaining VGA adapters (those not bundled for free)
        if "vga" in counts and counts["vga"] > 0:
            total += counts["vga"] * catalog["vga"].price

        return total
