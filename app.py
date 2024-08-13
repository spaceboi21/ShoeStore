from flask import Flask, render_template, request, jsonify
import pymongo

app = Flask(__name__)

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["ShoeStore"]
collection = db["shoe_details"]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/shoe_details')
def shoe_details():
    sku = request.args.get('sku')
    size = request.args.get('size')

    # Cast the size to the appropriate data type
    try:
        size = float(size)
    except ValueError:
        return jsonify({"error": "Invalid size format"}), 400

    # Find the shoe in the database
    shoe = collection.find_one({"sku": sku, "size": size})
    
    if shoe:
        return jsonify({
            "name": shoe["name"],
            "sku": shoe["sku"],
            "size": shoe["size"],
            "release_date": shoe["release_date"],
            "gender": shoe["gender"],
            "app_price": shoe.get("app_price"),
            "recent_sale": shoe.get("recent_sale"),
            "consign_price": shoe.get("consign_price"),
            "liquidity": shoe.get("liquidity"),
            "image_url": shoe["image_url"]
        })
    else:
        return jsonify({"error": "Shoe not found"}), 404

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
