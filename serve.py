from collections import defaultdict

from flask import Flask, request
from flask.json import jsonify

app = Flask("WindowPositionAssistantProxy")
proxy_storage = defaultdict(list)

@app.route("/<int:proxy_id>", methods=['GET', 'POST'])
def proxy(proxy_id):
    if request.method == "GET":
        return jsonify(proxy_storage[proxy_id])
    elif request.method == "POST":
        proxy_storage[proxy_id] = request.get_json(force=True)
        return ""
