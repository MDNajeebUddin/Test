from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dummy.db'
db = SQLAlchemy(app)


class Dummy(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    age = db.Column(db.Integer)


@app.route('/')
def home():
    return 'Welcome to the Flask backend!'


@app.route('/api/data')
def get_data():
    dummy_objects = Dummy.query.all()
    data = [{'id': dummy.id, 'name': dummy.name, 'age': dummy.age} for dummy in dummy_objects]
    return jsonify(data)


@app.route('/api/data/<int:id>')
def get_data_by_id(id):
    dummy_object = Dummy.query.get(id)
    if dummy_object is None:
        return jsonify({'error': 'Object not found'})
    data = {'id': dummy_object.id, 'name': dummy_object.name, 'age': dummy_object.age}
    return jsonify(data)


@app.route('/index')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
