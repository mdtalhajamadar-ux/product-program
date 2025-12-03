from product import product_details

def test_product_details():
    expected_output=(
        "Product Name : mobile\n"
        "product ID : M01\n"
        "Quantity : 10\n"
        "Price : 100000"
    )

    assert product_details("mobile", "M01", 10, 100000)==expected_output