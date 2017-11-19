from app import app


@app.route('/', methods=['GET', 'POST'])
def homepage():
    return 'Hello Universe'


@app.route('/')
def mainpage():
    return "hello world"
