import json
import requests
from flask import Request, Response

def handler(request: Request) -> Response:
    q = request.args.get("q")
    if not q:
        return Response(json.dumps({"error": "Missing q parameter"}), status=400, mimetype="application/json")

    url = f"https://api.duckduckgo.com/?q={q}&format=json&no_redirect=1&no_html=1"
    data = requests.get(url).json()

    body = {
        "query": q,
        "abstract": data.get("Abstract"),
        "heading": data.get("Heading"),
        "related": data.get("RelatedTopics", [])
    }
    return Response(json.dumps(body), mimetype="application/json")
