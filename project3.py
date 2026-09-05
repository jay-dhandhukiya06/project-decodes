#project3  AI Recommendation Logic

import pandas as pd

data = pd.read_csv("Dataset for Data Analytics - Sheet1.csv")

print("Product Recommendation System")
print("-----------------------------")

# 2. Display available products
print("\nAvailable Products:")
print(data["Product"].unique())

# 3. Take user preferences
product = input("\nEnter a product you are interested in: ").strip().lower()
payment = input("Enter your preferred payment method: ").strip().lower()

# 4. Convert columns to lowercase for matching
data["Product_lower"] = data["Product"].str.lower()
data["Payment_lower"] = data["PaymentMethod"].str.lower()

# 5. Match user preferences
recommendations = data[
    (data["Product_lower"] == product) &
    (data["Payment_lower"] == payment)
]

# 6. Display recommendations
if len(recommendations) > 0:

    print("\nRecommended Products:")

    # Remove duplicate products
    recommended_products = recommendations[
        ["Product", "UnitPrice", "Quantity", "TotalPrice"]
    ].drop_duplicates()

    print(recommended_products.to_string(index=False))

else:
    recommendations = data[data["Product_lower"] == product]

    if len(recommendations) > 0:
        print("\nNo exact payment-method match found.")
        print("Here are some recommendations:")

        recommended_products = recommendations[
            ["Product", "UnitPrice", "Quantity", "TotalPrice"]
        ].drop_duplicates()

        print(recommended_products.to_string(index=False))

    else:
        print("\nSorry, no matching product found.")

print("\nThank you for using the Recommendation System!")