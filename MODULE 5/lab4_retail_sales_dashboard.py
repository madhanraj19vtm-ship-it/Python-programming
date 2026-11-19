# Lab Exercise 4: Retail Sales Dashboard Using CSV and Matplotlib
# Objective: Read retail sales data from a CSV file and visualize it
# using a line graph and a bar chart.

import csv
from pathlib import Path
from collections import defaultdict
import matplotlib.pyplot as plt

CSV_FILE = Path(__file__).with_name("sales.csv")


def load_sales_data():
    """Read sales records from the CSV file."""
    if not CSV_FILE.exists():
        print(f"Error: {CSV_FILE.name} was not found.")
        return []

    records = []

    try:
        with CSV_FILE.open("r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            required_columns = {"Date", "Product", "Sales"}

            if not required_columns.issubset(reader.fieldnames or []):
                print("Error: CSV must contain Date, Product, and Sales columns.")
                return []

            for row in reader:
                try:
                    records.append({
                        "date": row["Date"],
                        "product": row["Product"],
                        "sales": float(row["Sales"])
                    })
                except (ValueError, TypeError):
                    print("Skipping invalid row:", row)

    except OSError as error:
        print("Unable to read CSV file:", error)

    return records


def display_summary(records):
    """Print total sales and product-wise sales."""
    total_sales = sum(record["sales"] for record in records)
    product_sales = defaultdict(float)

    for record in records:
        product_sales[record["product"]] += record["sales"]

    print("\n===== RETAIL SALES SUMMARY =====")
    print("Number of records:", len(records))
    print(f"Total sales: Rs. {total_sales:,.2f}")

    print("\nProduct-wise Sales:")
    for product, amount in sorted(product_sales.items()):
        print(f"{product}: Rs. {amount:,.2f}")


def create_dashboard(records):
    """Display a line graph and a bar chart."""
    date_sales = defaultdict(float)
    product_sales = defaultdict(float)

    for record in records:
        date_sales[record["date"]] += record["sales"]
        product_sales[record["product"]] += record["sales"]

    dates = sorted(date_sales)
    products = sorted(product_sales)

    figure, axes = plt.subplots(1, 2, figsize=(13, 5))

    axes[0].plot(
        dates,
        [date_sales[date] for date in dates],
        marker="o",
        linewidth=2
    )
    axes[0].set_title("Sales Trend by Date")
    axes[0].set_xlabel("Date")
    axes[0].set_ylabel("Sales (Rs.)")
    axes[0].tick_params(axis="x", rotation=45)
    axes[0].grid(True)

    axes[1].bar(
        products,
        [product_sales[product] for product in products]
    )
    axes[1].set_title("Product-wise Total Sales")
    axes[1].set_xlabel("Product")
    axes[1].set_ylabel("Sales (Rs.)")
    axes[1].tick_params(axis="x", rotation=45)

    figure.suptitle("Retail Sales Dashboard")
    figure.tight_layout()
    plt.show()


def main():
    records = load_sales_data()

    if not records:
        print("No valid sales data available.")
        return

    display_summary(records)
    create_dashboard(records)


if __name__ == "__main__":
    main()
