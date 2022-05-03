from flask import Flask, jsonify, request
import recommendation as rcm
import base64
import sqlite3

app = Flask(__name__)
def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

con = sqlite3.connect('Hewa.db', check_same_thread=False)
con.row_factory = sqlite3.Row
conList = []
con.row_factory = dict_factory
cur = con.cursor()


@app.route('/recommendation', methods=['POST'])
def index():
    uid = request.args.get('uid')
    data = request.get_json()
    result = rcm.getRecommendations(data, uid)
    print(result)
    return jsonify({'uid': uid, 'recommendation': result})


@app.route('/test', methods=['GET'])
def test():
    return jsonify({'greeting': 'Hi'})


@app.route('/post_test', methods=['POST'])
def post_test():
    return jsonify({'greeting': 'Hi'})


@app.route('/get_recommendation', methods=['POST'])
def get_recommendation():
    data = request.form
    print(type(data))
    return jsonify

@app.route('/query', methods=['GET'])
def comment_readlDataFromSQLite():
    data = request.args.get('query')
    # print(data)
    cur.execute(data)
    # print(cur.fetchone())
    # for row in cur.execute('SELECT * FROM menuTABLE'):
    #     conList.append(row)
    #     print(row)
    return jsonify(cur.fetchall())


if __name__ == "__main__":
    app.run(threaded=True, port=6000)
