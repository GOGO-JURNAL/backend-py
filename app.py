from flask import Flask, jsonify, request

from controllers.pengabdian import pengabdian
from controllers.penelitian import penelitian
from controllers.scopus import scopus

app = Flask(__name__)

@app.route('/penelitian', methods=['POST'])
def get_penelitian_data():
    return jsonify(penelitian(request.get_json()))

@app.route('/pengabdian', methods=['POST'])
def get_pengabdian_data():
    return jsonify(pengabdian(request.get_json()))

@app.route('/scopus', methods=['POST'])
def get_scopus_data():
    return jsonify(scopus(request.get_json()))

if __name__ == '__main__':
    app.run(debug=True)