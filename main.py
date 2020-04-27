from flask import Flask

app = Flask(__name__)

# Comment sample
@app.route('/')
def index():
    return 'Hey, we have Flask in a Docker container!'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')