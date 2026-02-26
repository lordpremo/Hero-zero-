import json
from flask import Request, Response

def handler(request: Request) -> Response:
    body = {
        "api": "BROKEN LORD API",
        "owner": "Lord",
        "brand": "BROKEN LORD",
        "status": "running",
        "version": "1.0.0",
        "endpoints": {
            "wiki": "/api/wiki?q=",
            "duckduckgo": "/api/ddg?q=",
            "books": "/api/books?q=",
            "github": "/api/github?q=",
            "stackoverflow": "/api/stack?q="
        }
    }
    return Response(json.dumps(body), mimetype="application/json")
