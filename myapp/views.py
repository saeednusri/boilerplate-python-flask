from myapp import app
import myapp.package.package_functions as test

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
    return test.package_1_test()
