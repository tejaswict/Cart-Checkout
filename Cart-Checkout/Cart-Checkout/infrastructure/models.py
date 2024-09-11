from sqlalchemy import Column, String, Float
from infrastructure.db import Base


class ProductModel(Base):
    """
    SQLAlchemy model representing a product in the database.

    Attributes:
        sku (str): The SKU of the product.
        name (str): The name of the product.
        price (float): The price of the product.
    """

    __tablename__ = "products"

    sku = Column(String, primary_key=True)
    name = Column(String, nullable=False)
    price = Column(Float, nullable=False)

    def __init__(self, sku: str, name: str, price: float) -> None:
        """
        Initialize a ProductModel instance.

        Args:
            sku (str): SKU of the product.
            name (str): Name of the product.
            price (float): Price of the product.
        """
        self.sku = sku
        self.name = name
        self.price = price
