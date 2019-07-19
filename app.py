#!/usr/bin/env python
# -*- coding utf-8 -*-

from flask import Flask, jsonify, request
import re

app = Flask(__name__)

@app.route('/story', methods=['POST'])
def story():
    req_data = request.get_json()
    words = req_data['words'] if 'words' in req_data else []
    template = req_data['template']

    matches = re.findall("&[0-9]{1}", template)
    if len(matches) == len(words):
        for idx in range(len(matches)):
            template = template.replace(matches[idx], words[int(matches[idx].replace("&", ""))-1])
    else:
        raise Exception("wrong number of arguments")

    return jsonify({'story': template})

@app.route('/health', methods=['GET'])
def health():
    return 'ok', 200

def app_error(e):
    return jsonify({'message': str(e)}), 400

if __name__ == '__main__':
    app.register_error_handler(Exception, app_error)
    app.run(host='0.0.0.0', port=8080)