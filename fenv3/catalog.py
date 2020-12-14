from flask import Flask
from flask_restful import Api, Resource
import json


app = Flask(__name__)
api = Api(app)
books = [["","","","",""],["","","","",""],["","","","",""],["","","","",""],["","","","",""],["","","","",""],["","","","",""]]
f = open("data.txt","r")

for i in range(7):
     for j in range(5):
         books[i][j]=f.readline()
         books[i][j]=books[i][j].rstrip("\n")
         print(books[i][j])

f.close()
class search(Resource):
    def get(self, type):
        print(type)
        s=""
        for p in range(7):
            if books[p][1]==type:
               s=s+"title : "+ books[p][0]+" , "
               s=s+"id : " +books[p][4]+" , "


        return{"books":s}
class lookup(Resource):
    def get(self, id):
        s=""
        for p in range(7):
            if books[p][4]==str(id):
                s = s + "title : " + books[p][0] + " , "
                s = s + "stock : " + books[p][3] + " , "
                s = s + "price : " + books[p][2] + " , "
        return {"books": s}
class buy(Resource):
    def post(self,id):
        s=""
        x=0
        for p in range(7):
            if books[p][4] == str(id):
                s=books[p][3]
                x=int(s)
                if x>0 :


                    return {"stock left": x}
                else:
                    return {"stock left": 0}
class update(Resource):
    def put(self,id):
        for p in range(7):
            if books[p][4] == str(id):
                books[p][3] = str(int(books[p][3]-1));
                f = open("data.txt", "w")

                for i in range(4):
                    for j in range(5):
                        f.write(books[i][j] + "\n")
        return {"result": "success"}
api.add_resource(search, "/search/<string:type>")
api.add_resource(lookup,"/lookup/<int:id>")
api.add_resource(buy,"/buy/<int:id>")
api.add_resource(update,"/update/<int:id>")
if __name__ == "__main__":
    app.run(port=9000,debug=True)
