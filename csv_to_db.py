import pandas as pd
import pymongo

# Read the CSV file (assuming it's a standard CSV with commas as the separator)
df = pd.read_csv("dataset.csv")

# Replace empty strings with None to handle missing data
df = df.replace(r'^\s*$', None, regex=True)

# # Rename columns to match MongoDB fields if necessary
df.rename(columns={
    "Image": "image_url",
    "SKU": "sku",
    "Size": "size",
    "Release Date": "release_date",
    "Gender": "gender",
    "Name": "name",
    "App Price": "app_price",
    "Consig Price": "consign_price",
    "Liquidity": "liquidity",
    "Last Sold Price": "recent_sale"
}, inplace=True)

# Convert to a list of dictionaries
data = df.to_dict(orient="records")

# Connect to MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["ShoeStore"]
collection = db["shoe_details"]

# Clear existing data in the collection (optional)
collection.delete_many({})

# Insert the new data into MongoDB
collection.insert_many(data)

# Confirm the database and collection
print("Databases:", client.list_database_names())
print("Collections in ShoeStore DB:", db.list_collection_names())
