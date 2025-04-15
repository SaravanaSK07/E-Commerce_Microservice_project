from flask import Flask
 import requests
 
 app = Flask(__name__)
 
 @app.route('/orders', methods=['GET'])
 def get_orders():
     user = requests.get('http://localhost:8080/users').json()
     product = requests.get('http://localhost:3000/products').json()
     try:
         user = requests.get('http://localhost:8080/users', timeout=2).json()
     except (requests.RequestException, ValueError):
         return "Error: User Service unavailable", 503
     
     try:
         product = requests.get('http://localhost:3000/products', timeout=2).json()
     except (requests.RequestException, ValueError):
         return "Error: Product Service unavailable", 503
     
     return f"Order for {user['name']}: {product['name']} at ${product['price']}"
 
 if __name__ == "__main__":
