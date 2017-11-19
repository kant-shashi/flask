from flask import Flask

app = Flask(__name__)

app.config.from_object('config.DevelopmentConfig')

@app.route('/')
def mainpage():
    return "hello Universe"

@app.route('/user/<string:name>')
def user(name):
    return 'hello ' + name



if __name__ == '__main__':
    app.run(use_reloader=True)