import pytest

def product_details(name, product_id, qty, price):
    result=(
        f"Product Name : {name}\n"
        f"product ID : {product_id}\n"
        f"Quantity : {qty}\n"
        f"Price : {price}"

    )

    return result

if __name__=="__main__":
    name="Laptop"
    product_id="P001"
    qty=5
    price=100000
    print(product_details(name, product_id, qty, price))