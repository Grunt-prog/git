from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    print("Hi helloe")
    return "Hello, Dockerized Flask! hi hello123456"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5003)
