from flask import Flask
from flask_restful import Api

app = Flask(__name__)
#api = Api(app)

@app.route("/")
def hello():
    return "<h1 style='color:blue'>Hello There!</h1>"
## Resources
# Status
# Status List
# Device
# Device List

if __name__ == '__main__':
    app.run(port=8080, debug=True)
