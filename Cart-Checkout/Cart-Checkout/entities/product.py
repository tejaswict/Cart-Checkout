from typing import List
from infrastructure.models import ProductModel
from sqlalchemy.orm import Session


class Product:
    """
    Represents a product in the catalog.

    Attributes:
        sku (str): The stock-keeping unit (SKU) of the product.
        name (str): The name of the product.
        price (float): The price of the product.
    """

    def __init__(self, sku: str, name: str, price: float) -> None:
        """
        Initialize a Product instance.
        """
        self.sku = sku
        self.name = name
        self.price = price

    def get_price(self) -> float:
        """
        Returns the price of the product.
        """
        return self.price


class ProductRepository:
    """
    Repository for handling product data retrieval from the database.

    Attributes:
        session (Session): The SQLAlchemy database session.
    """

    def __init__(self, session: Session) -> None:
        """
        Initialize the ProductRepository instance.

        Args:
            session (Session): The SQLAlchemy session for database access.
        """
        self.session = session

    def get_all_products(self) -> List[ProductModel]:
        """
        Fetch all products from the database.

        Returns:
            List[ProductModel]: A list of all products from the database.
        """
        return self.session.query(ProductModel).all()

    def get_product_by_sku(self, sku: str) -> ProductModel:
        """
        Fetch a product by its SKU.

        Args:
            sku (str): The SKU of the product to fetch.

        Returns:
            ProductModel: The product model matching the SKU.
        """
        return self.session.query(ProductModel).filter_by(sku=sku).first()
