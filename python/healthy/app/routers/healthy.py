from fastapi import APIRouter
import json
import os

router = APIRouter()


@router.get("/healthy")
def healthy():
    example_file_path = os.path.join("app", "static", "example.json")
    with open(example_file_path, "r") as file:
        return json.load(file)
