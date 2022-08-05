from os import environ
from pathlib import Path

from flask import Flask, request, Response

WPAP_DIR = Path(environ.get("WPAP_DIR", "./wpap_cache"))
WPAP_DIR.mkdir(exist_ok=True, parents=True)

app = Flask("WindowPositionAssistantProxy")


@app.route("/<proxy_id>", methods=["GET", "POST"])
def proxy(proxy_id):
    if request.method == "GET":
        try:
            response = (WPAP_DIR / proxy_id).read_text()
        except IOError:
            response = "[]"

        return Response(
            response=response,
            status=200,
            mimetype="application/json",
        )
    elif request.method == "POST":
        (WPAP_DIR / proxy_id).write_text(request.get_data(as_text=True))
        return ""
