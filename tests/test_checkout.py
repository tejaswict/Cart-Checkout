import pytest
from entities.pricing_rules import PricingRules
from entities.product import Product


@pytest.fixture
def catalog():
    """
    Fixture for the product catalog used in all tests.
    """
    return {
        "ipd": Product(sku="ipd", name="Super iPad", price=549.99),
        "mbp": Product(sku="mbp", name="MacBook Pro", price=1399.99),
        "atv": Product(sku="atv", name="Apple TV", price=109.50),
        "vga": Product(sku="vga", name="VGA adapter", price=30.00),
    }


@pytest.fixture
def pricing_rules():
    """
    Fixture for the pricing rules instance used in all tests.
    """
    return PricingRules()


def test_three_for_two_apple_tv(pricing_rules, catalog):
    """
    Test the 3-for-2 deal on Apple TVs.
    SKUs Scanned: atv, atv, atv
    Total expected: 2 * price of Apple TV
    """
    items = ["atv", "atv", "atv"]
    total = pricing_rules.apply(items, catalog)
    assert total == 2 * catalog["atv"].price


def test_apple_tv_and_vga_bundle(pricing_rules, catalog):
    """
    Test the case with 3 Apple TVs and a VGA adapter.
    SKUs Scanned: atv, atv, atv, vga
    Total expected: 2 * price of Apple TV + price of VGA adapter
    """
    items = ["atv", "atv", "atv", "vga"]
    total = pricing_rules.apply(items, catalog)
    expected_total = 2 * catalog["atv"].price + catalog["vga"].price
    assert total == expected_total


def test_bulk_discount_on_super_ipad(pricing_rules, catalog):
    """
    Test bulk discount on Super iPads (more than 4).
    SKUs Scanned: ipd, ipd, ipd, ipd, ipd
    Total expected: 5 * discounted price of $499.99
    """
    items = ["ipd", "ipd", "ipd", "ipd", "ipd"]
    total = pricing_rules.apply(items, catalog)
    expected_total = 5 * 499.99  # Discounted price
    assert total == expected_total


def test_super_ipad_no_bulk_discount(pricing_rules, catalog):
    """
    Test normal pricing on Super iPads (less than 5).
    SKUs Scanned: ipd, ipd, ipd
    Total expected: 3 * regular price of Super iPad
    """
    items = ["ipd", "ipd", "ipd"]
    total = pricing_rules.apply(items, catalog)
    expected_total = 3 * catalog["ipd"].price
    assert total == expected_total


def test_macbook_pro_with_free_vga(pricing_rules, catalog):
    """
    Test the free VGA adapter bundled with every MacBook Pro.
    SKUs Scanned: mbp, vga
    Total expected: price of MacBook Pro (VGA adapter is free)
    """
    items = ["mbp", "vga"]
    total = pricing_rules.apply(items, catalog)
    expected_total = catalog["mbp"].price  # VGA adapter is free
    assert total == expected_total


def test_macbook_pro_no_vga(pricing_rules, catalog):
    """
    Test MacBook Pro without a VGA adapter.
    SKUs Scanned: mbp
    Total expected: price of MacBook Pro
    """
    items = ["mbp"]
    total = pricing_rules.apply(items, catalog)
    expected_total = catalog["mbp"].price
    assert total == expected_total


def test_mixed_items(pricing_rules, catalog):
    """
    Test a mix of items to check all pricing rules together.
    SKUs Scanned: atv, ipd, ipd, atv, ipd, ipd, ipd
    Total expected: various prices with bulk discounts and 3-for-2 deal.
    """
    items = ["atv", "ipd", "ipd", "atv", "ipd", "ipd", "ipd"]
    total = pricing_rules.apply(items, catalog)
    expected_total = (2 * catalog["atv"].price) + (5 * 499.99)
    assert total == expected_total


def test_macbook_pro_with_free_vga_and_others(pricing_rules, catalog):
    """
    Test case with MacBook Pro and additional VGA adapter, ensuring only one VGA adapter is free.
    SKUs Scanned: mbp, vga, ipd
    Total expected: price of MacBook Pro + price of Super iPad (VGA adapter is free)
    """
    items = ["mbp", "vga", "ipd"]
    total = pricing_rules.apply(items, catalog)
    expected_total = catalog["mbp"].price + catalog["ipd"].price
    assert total == expected_total
