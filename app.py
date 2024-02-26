from flask import Flask, jsonify

from controllers.pengabdian import pengabdian
from controllers.penelitian import penelitian
from controllers.scopus import scopus

app = Flask(__name__)

@app.route('/penelitian', methods=['GET'])
def get_penelitian_data():
    return jsonify(penelitian())

@app.route('/pengabdian', methods=['GET'])
def get_pengabdian_data():
    return jsonify(pengabdian())

@app.route('/scopus', methods=['GET'])
def get_scopus_data():
    return jsonify(scopus())

if __name__ == '__main__':
    app.run(debug=True)