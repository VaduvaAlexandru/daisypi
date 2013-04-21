import os
import flask

import data.update
import data.entities
from data import DB


DEBUG = os.environ.get('DEBUG') == 'on'
PORT = int(os.environ.get('PORT', '5000'))


app = flask.Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
DB.init_app(app)
with app.app_context():
    DB.create_all()


@app.route('/')
def hello_world():
    return flask.render_template('index.html', **{
       'baby_messages': data.entities.ProfileMessage.query.filter_by(profile='baby_monitoring'),
       'all_messages': data.entities.ProfileMessage.query.all(),
    })


@app.route('/stuff')
def baby_stuff():
    return flask.render_template('baby_template.html', **{
       'baby_messages': data.entities.ProfileMessage.query.filter_by(profile='baby_monitoring'),})


@app.route('/update', methods=['POST'])
def update():
    data.update.update_json(flask.request.json)
    data.update.test_upload()
    return str(flask.request.json)


if __name__ == '__main__':
    host = '127.0.0.1' if DEBUG else '0.0.0.0'
    app.run(debug=DEBUG, port=PORT, host=host)
