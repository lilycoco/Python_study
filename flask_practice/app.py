from flask import Flask
app = Flask(__name__)
@app.route("/")
def index():
  return "Hello from flask"

@app.route("/api/hello")
def api_hello():
  return "api_hello"

@app.route("/api/items/<int:item_id>")
def api2(item_id):
  return "item_id is %d" % item_id
if __name__ == "__main__":
  app.run()

