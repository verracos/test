from flask import Flask

app = Flask(__name__)

@app.route('/')
def holamundo():
    return 'Hola soy un Test para OpenShift 3!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8080')