from flask import request, url_for, jsonify, redirect
from flask_api import FlaskAPI, status, exceptions

# Para visitar la rutas seguir los siguientes enlaces

#curl -i http://localhost:5000/get
#curl -X POST http://localhost:5000/post -H "Content-Type: application/json" -d '{"username":"user", "password":"pass"}'
#curl -i -H "Content-Type: application/json" -X POST -d '{"username":"user", "password":"pass"}' http://localhost:5000/post
#curl -i -H "Content-Type: application/json" -X POST -d '{"username":"wrong", "password":"wrong"}' http://localhost:5000/post
#curl -i http://localhost:5000/redirect
#curl -i http://localhost:5000/divide_by_zero
#curl -i http://localhost:5000/unavalible_resource


app = FlaskAPI(__name__)

@app.route("/get", methods=['GET'])
def get():
    content = 'OK'
    resp = jsonify(content)
    resp.status = str(status.HTTP_200_OK)
    return resp

@app.route("/post", methods=['POST'])
def post():
    content = request.json
    if content['username'] == 'user' and content['password'] == 'pass':
        content = 'OK'
        resp = jsonify(content)
        resp.status = str(status.HTTP_200_OK)
        return resp
    else:
        content = 'Credentials invalid'
        resp = jsonify(content)
        resp.status = str(status.HTTP_403_FORBIDDEN)
        return resp

@app.route("/redirect", methods=['GET'])
def redirect_endpoint():
    return redirect("/get", code=302)

@app.route("/divide_by_zero", methods=['GET'])
def divide_by_zero():
    try:
        a=10/0
    except:
        content = 'Internal error'
        resp = jsonify(content)
        resp.status = str(status.HTTP_500_INTERNAL_SERVER_ERROR)
        return resp

@app.errorhandler(404) 

def not_found(e): 
    content = 'Error! File not found'
    resp = jsonify(content)
    resp.status = str(status.HTTP_404_NOT_FOUND)
    return resp

if __name__ == "__main__":
    app.run(debug=True)