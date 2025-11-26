from os import environ
from pathlib import Path

from flask import Flask, request, Response, abort

WPAP_DIR = Path(environ.get("WPAP_DIR", "./wpap_cache"))
WPAP_DIR.mkdir(exist_ok=True, parents=True)

app = Flask("WindowPositionAssistantProxy")


@app.route("/<int:proxy_id>", methods=["GET", "POST"])
def proxy(proxy_id: int):
    # see https://github.com/GramyPomagamy/WindowPositionAssistant/blob/master/WindowPositionAssistant/Program.cs#L103
    if not (100 <= proxy_id <= 999):
        abort(400)

    path = WPAP_DIR / str(proxy_id)

    if request.method == "GET":
        try:
            response = path.read_text()
        except IOError:
            response = "[]"

        return Response(
            response=response,
            status=200,
            mimetype="application/json",
        )
    elif request.method == "POST":
        path.write_text(request.get_data(as_text=True))
        return ""
