from flask import Flask, jsonify, request
from komercio import produtos

app = Flask(__name__)

@app.get('/products')
def list_products():
    return jsonify(produtos), 200

@app.get('/products/<product_id>')
def get(product_id: int):
    for item in produtos:
        if item["id"] == int(product_id):
            return item, 200

@app.post('/products')
def create ():
    body = request.get_json()
    last_id = produtos[-1]['id']
    body["id"] = last_id + 1
    produtos.append(body)
    return body, 201


@app.patch('/products/<int:product_id>')
def update(product_id: int):
    new_product = request.get_json()
    for product in produtos:
        if product["id"] == int(product_id):
            for value in new_product:
                product[value] = new_product[value]
    return "", 204



@app.delete('/products/<product_id>')
def delete(product_id: int):
    for product in produtos:
        if product["id"] == int(product_id):
            produtos.remove(product)
    return "", 204  
    