from my_app import app
import my_app.package_1 as test

@app.route('/')
def example():
    return "Example Flask App"

@app.route('/healthz')
def health_check():
    return "OK"

@app.route('/package_1')
def packagetest():
    return test.package_1_test()
