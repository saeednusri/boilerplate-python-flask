import os
from flask import Flask
app = Flask(__name__)
app.debug = True

@app.route('/')
def example():
    return "Example Flask App"

@app.route('/healthz')
def health_check():
    return "OK"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
