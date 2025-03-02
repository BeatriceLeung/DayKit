from flask import Flask
# from flask_cors import CORS

app = Flask(__name__)
# CORS(app, supports_credentials=True)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5002)