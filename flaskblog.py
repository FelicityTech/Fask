import os
from flask import send_from_directory
from flask import Flask
app = Flask(__name__)

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')
@app.route("/")
def hello():
    return "<h1>Home Page</h1>"


if __name__ == '__main__':
    app.run(debug=True)