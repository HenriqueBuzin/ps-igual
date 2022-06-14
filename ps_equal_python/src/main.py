from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello_geek():
    data = '<h1>Hello from Flask & Docker</h2>'
    return jsonify(data)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000", debug=True)
