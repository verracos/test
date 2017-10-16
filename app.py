from flask import Flask

app = Flask(__name__)

@app.route('/')
def holamundo():
    return 'Aplicación Verracos en Mantenimiento. Disculpen las molestias.'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8080')