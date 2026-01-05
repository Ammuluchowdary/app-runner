import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    # We pull the name from an Environment Variable (optional)
    name = os.environ.get("USER_NAME", "Explorer")
    return f"<h1>Hello {name}!</h1><p>Your Flask app is running on AWS App Runner.</p>"

if __name__ == "__main__":
    # App Runner needs the app to listen on 0.0.0.0
    # The default port for App Runner is usually 8080
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)
