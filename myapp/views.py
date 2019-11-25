from myapp import app
import myapp.package_1.package_1_functions as test

@app.route('/')
def example():
    return "Example Flask App"

@app.route('/healthz')
def health_check():
    return "OK"

@app.route('/package_1')
def packagetest():
    return test.package_1_test()
