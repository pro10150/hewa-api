import os
import threading
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

# Define the lock globally
lock = threading.Lock()

def Func(host,cursor,db):
    try:
        lock.acquire(True)
        res = cursor.execute('''...''',(host,))
        # do something
    finally:
        lock.release()

@app.route('/', methods=['GET'])
def start():
    return "Hello world!"


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

@app.route('/query', methods=['POST'])
def comment_readlDataFromSQLite():
    data = request.args.get('query')
    jsonData = request.get_json()
    print(tuple(jsonData))
    # print(data)
    try:
        lock.acquire(True)
        cur.execute(data, tuple(jsonData))
    finally:
        lock.release()
    # print(cur.fetchone())
    # for row in cur.execute('SELECT * FROM menuTABLE'):
    #     conList.append(row)
    #     print(row)
    return jsonify(cur.fetchall())

@app.route('/emptyQuery', methods=['POST'])
def emptyQuery():
    data = request.args.get("query")

    try:
        lock.acquire(True)
        cur.execute(data)
    finally:
        lock.release()

    return jsonify(cur.fetchall())

if __name__ == "__main__":
    port = os.environ.get("PORT", 5000)
    app.run(debug=True, host='0.0.0.0', port=port)
