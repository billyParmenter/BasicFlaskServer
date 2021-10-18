from flask import Flask
from flask_cors import CORS
from flask_restful import Api, Resource


app = Flask(__name__)
cors = CORS(app)
api = Api(app)

# FUNCTION : Running
# ROUTE: /
# DESCRIPTION : This route is used to test that the server is 
#                   running and the client can connect to it
# PARAMETERS : None
# RETURNS : <string> : "Running"
class Running(Resource):
    def get(self):
        return "Running"


# FUNCTION : Another_route
# ROUTE: /
# DESCRIPTION : This is an example of another route
# PARAMETERS : None
# RETURNS : <string> : "Running"
class Another_route(Resource):
    def get(self):
        return "Another endpoint"



api.add_resource(Running, "/")
api.add_resource(Another_route, "/another_route")


if __name__ == "__main__":
    app.run(host='0.0.0.0')
