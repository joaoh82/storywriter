#!/usr/bin/env python
# -*- coding utf-8 -*-

from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/story', methods=['POST'])
def story():
    req_data = request.get_json()
    words = req_data['words'] if 'words' in req_data else []
    template = req_data['template']

    return jsonify({'template': template, 'words': words})

def app_error(e):
    return jsonify({'message': str(e)}), 400

if __name__ == '__main__':
    app.register_error_handler(Exception, app_error)
    app.run(host='0.0.0.0', port=8080)