from fastapi import FastAPI
import requests
from pydantic import BaseModel

app = FastAPI()

@app.get("/get_value")
def get_value():
    return {"value": "BircleAI"}


class PostRequestModel(BaseModel):
    url: str

@app.post("/fetch_data")
def fetch_data(request_data: PostRequestModel):
    try:
        response = requests.get(request_data.url)
        response_data = response.json()
        print("Response from external API:", response_data)
        return response_data
    except Exception as e:
        return {"error": str(e)}

@app.put("/square/{number}")
def square_number(number: int):
    return {"result": number ** 2}