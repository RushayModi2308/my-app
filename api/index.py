from fastapi import FastAPI, Query
import json

app = FastAPI()

# Load data from JSON file
with open("q-vercel-python.json", "r") as file:
    marks_data = json.load(file)

@app.get("/api")
def get_marks(name: list[str] = Query(...)):
    result = {"marks": []}
    for n in name:
        for entry in marks_data:
            if entry["name"] == n:
                result["marks"].append(entry["marks"])
    return result
