from flask import Flask

app = Flask(__name__)

@app.route('/')
def holamundo():
    return 'Hola soy un Test!'

if __name__ == '__main__':
    app.run()