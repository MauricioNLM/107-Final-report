from flask import Flask  , request
import json
products = [{'name': 'mauricio','age' : 26 },{'name': 'Joel','age' : 30 },{'name':'Saul', 'age':15}]

app = Flask(__name__)
@app.get("/")
def home():
    return "Welcome to end point"

#GET /api/catalog

@app.get("/api/catalog")
def catalog():
    return products

# POST /api/catalog endpoint to save products

@app.post("/api/catalog")
def catalog():
    product = request.get_json()
    print(f"New procucto ${product}")
    products.append(product)
    return "test"

# GET /api/reports/total return the total value of the catalog

@app.get("/api/reports/total")
def catalog():
    return len(products)

#GET /api/products/<category> that returns the list of products that belong to the given category name

@app.get("/api/products/<int:category>")
def dcategory(category):
    found_products = [product for product in products if product['name'] == category]
    if found_products:
        return found_products
    else:
        return "that category does not exist"


app.run(debug=True)