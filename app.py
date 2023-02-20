from flask import Flask,request
from OpenAIAuth import Authenticator,Error
import json

app = Flask(__name__)

@app.route("/", methods = ["POST"])
def access_token():
    rsp = {
        "code": 0,
        "access_token":"",
        "message": ""
    }
    try:
        data = request.get_json()
        u = data.get("u")
        p = data.get("p")
        auth = Authenticator(u,p)
        auth.begin()
        rsp["access_token"] = auth.get_access_token()
        response = json.dumps(rsp)
        return response,200,{"Content-Type":"application/json"}
    except Error as e: 
        rsp["code"] = 1
        rsp["message"] = e.details
        response = json.dumps(rsp)
        return response,200,{"Content-Type":"application/json"}


if __name__ == "__main__":
    app.run()