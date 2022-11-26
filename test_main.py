import json

from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def object_to_json(class_object: object) -> str:
    return json.dumps(class_object.__dict__)
