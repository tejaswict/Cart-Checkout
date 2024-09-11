# Checkout System

This project implements a checkout system for a computer store with flexible pricing rules, developed using clean architecture principles and the repository pattern. It supports special offers such as bulk discounts, 3-for-2 deals, and bundle offers.

Written in a way where usecase can be called by any endpoint. Currently not using specific frameworks
## Features

- **Flexible Pricing Rules**: Easily configurable discounts and promotions, such as:
  - 3-for-2 deal on Apple TVs
  - Bulk discount on Super iPads when buying more than 4
  - Free VGA adapter with every MacBook Pro
- **Clean Architecture**: Organized with separate layers for business logic, repositories, and domain models.
- **PostgreSQL Backend**: Uses PostgreSQL for data persistence, with schema migrations managed by Alembic.
- **Unit Tests**: Thorough test coverage using `pytest` for key pricing scenarios.

## Product Catalog

The system starts with the following product catalog:

| SKU  | Name          | Price   |
| ---- | ------------- | ------- |
| ipd  | Super iPad    | $549.99 |
| mbp  | MacBook Pro   | $1399.99|
| atv  | Apple TV      | $109.50 |
| vga  | VGA adapter   | $30.00  |

## Pricing Rules

1. **3-for-2 Apple TV Deal**: Buy 3 Apple TVs and only pay for 2.
2. **Bulk Discount on Super iPads**: If more than 4 Super iPads are purchased, the price drops to $499.99 each.
3. **Free VGA Adapter with MacBook Pro**: For every MacBook Pro purchased, a VGA adapter is bundled for free.

## Setup

### Prerequisites

- Python 3.11
- PostgreSQL
- Alembic (for migrations)
- `pytest` (for testing)

### Installation

1. **Clone the Repository**

   ```bash
   git clone 
   cd checkout-system

2. **Clone the Repository**
tox -vv
source .tox/py311/bin/activate

3.  **Configure Database**

Update your database connection string in the alembic.ini file or environment variables. Your PostgreSQL connection URL should look like this:

postgresql://username:password@localhost:5432/products

4. **Run Alembic Migrations**

Create the database schema using Alembic

5. **Run Tests ** 

pytest tests/test_checkout.py

6. **Run Project**

Sample runner is given which validates the cart functionality.

python Sample_run.py