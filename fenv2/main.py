from flask import Flask
from flask_restful import Api, Resource
import requests
app = Flask(__name__)
api =Api(app)
class he(Resource):
    def get(self):
        return{"data":"hello"}

api.add_resource(hello, "/hello")
if __name__ == "__main__":
   d

