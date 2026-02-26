import json
import requests
from flask import Request, Response

def handler(request: Request) -> Response:
    q = request.args.get("q")
    if not q:
        return Response(json.dumps({"error": "Missing q parameter"}), status=400, mimetype="application/json")

    url = f"https://api.github.com/search/repositories?q={q}"
    data = requests.get(url).json()

    body = {"query": q, "results": data.get("items", [])}
    return Response(json.dumps(body), mimetype="application/json")
