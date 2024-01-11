#!flask/bin/python
from flask import Flask, jsonify, abort, request

app = Flask(__name__)

sets = [
    {
        'id': 1,
        'name': 'Paiste cymbal set',
        'description': u'This is a new Paiste PST8 drum cymbals, B20',
    },
    {
        'id': 2,
        'name': u'Istanbul agop cymbal set',
        'description': u'This is a brand new Istanbul B20 cymbal set',
    }
]

@app.route('/list/api/v1.0/sets', methods=['GET'])
def get_sets():
    return jsonify({'sets': sets})

@app.route('/list/api/v1.0/sets/<int:set_id>', methods=['GET'])
def get_set(set_id):
    if len(sets) == 0:
        abort(404)
    return jsonify({'set': sets[0]})

@app.route('/list/api/v1.0/sets', methods=['POST'])
def create_set():
    if not request.json or not 'name' in request.json:
        abort(400)
    set= {
        'id': sets[-1]['id'] + 1,
        'name': request.json['name'],
        'description': request.json.get('description', "")
    }
    sets.append(set)
    return jsonify({'set': set}), 201

@app.route('/list/api/v1.0/sets/<int:set_id>', methods=['PUT'])
def update_set(set_id):
    if len(sets) == 0:
        abort(404)
    if not request.json:
        abort(400)
    sets[0]['name'] = request.json.get('name', sets[0]['name'])
    sets[0]['description'] = request.json.get('description', sets[0]['description'])
    return jsonify({'set': sets[0]})

@app.route('/list/api/v1.0/sets/<int:set_id>', methods=['DELETE'])
def delete_set(set_id):
    if len(sets) == 0:
        abort(404)
    sets.remove(sets[0])
    return jsonify({'result': True})

if __name__ == '__main__':
    app.run(debug=True)