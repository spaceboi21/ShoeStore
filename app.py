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
    
    shoe = collection.find_one({"sku": sku, "size": size})
    
    if shoe:
        return jsonify({
            "name": shoe["name"],
            "sku": shoe["sku"],
            "size": shoe["size"],
            "release_date": shoe["release_date"],
            "gender": shoe["gender"],
            "app_price": shoe["app_price"],
            "recent_sale": shoe["recent_sale"],
            "consign_price": shoe["consign_price"],
            "liquidity": shoe["liquidity"],
            "image_url": shoe["Image"]  # Using the Image field from the database
        })
    else:
        return jsonify({"error": "Shoe not found"}), 404

if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0")
