import os
import flask

from data.update import update_json

DEBUG = os.environ.get('DEBUG') == 'on'
PORT = int(os.environ.get('PORT', '5000'))


app = flask.Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']


@app.route('/')
def hello_world():
    return flask.render_template('index.html')


@app.route('/update', methods=['POST'])
def update():
    update_json(flask.request.json)
    return str(flask.request.json)


if __name__ == '__main__':
    host = '127.0.0.1' if DEBUG else '0.0.0.0'
    app.run(debug=DEBUG, port=PORT, host=host)
