from flask import Flask
from flask_restful import Api, Resource
import requests
import json
app = Flask(__name__)
api = Api(app)
class buy(Resource):
    def post(self,id):
        Base = " http://127.0.0.1:6000/"
        response = requests.post(Base + "buy/"+str(id))
        x=response.json()
        if x['stock left']==0:
            return {"result": "fail no stock left"}
        else:
            response = requests.put(Base + "update/" + str(id))
            return {"result": "success"}



api.add_resource(buy,"/buy/<int:id>")
if __name__ == "__main__":
    app.run(port=7000,debug=True)