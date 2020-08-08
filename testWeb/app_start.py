from flask import Flask, request, redirect, url_for, send_from_directory, render_template
 
app = Flask(__name__)
app.debug = True
 
# Routes
@app.route('/', methods=['GET'])
def root():
    return app.send_static_file('index.html')
 
@app.route('/')
def static_prox(path):
    return app.send_static_file(path)
 
if __name__ == "__main__":
    app.run(host='172.31.26.120', port=80, threaded=True)

