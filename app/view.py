@app.route('/')
def example():
    return "Example Flask App"

@app.route('/healthz')
def health_check():
    return "OK"
