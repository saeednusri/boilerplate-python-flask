from myapp import app
import myapp.package.functions as functions

@app.route('/execute', methods = ['POST'])
def execute():
    # Add code here
    return "Success"

@app.route('/')
def example():
    return "Example Flask App"

@app.route('/healthz')
def health_check():
    return "OK"

@app.route('/package_1')
def packagetest():
    return str(functions.add(1,1))
