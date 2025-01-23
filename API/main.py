from typing import Union

from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import json

app = FastAPI()

########################
#                      #
# Change CORS policy!! #
#                      #
########################

origins = [
    "http://localhost:3000",  # Replace with the actual origin of your frontend
    "http://127.0.0.1:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



#           #
# Functions #
#           #

def load_friends():
    try:
        with open("storage/friends.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        raise HTTPException(status_code=500, detail="Friends file not found.")
    except json.JSONDecodeError:
        raise HTTPException(status_code=500, detail="Error decoding friends JSON.")

def load_you():
    try:
        with open("storage/you.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        raise HTTPException(status_code=500, detail="You file not found.")
    except json.JSONDecodeError:
        raise HTTPException(status_code=500, detail="Error decoding you JSON.")


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.get("/friends/")
def read_friends(q: Union[str, None] = None):
    friends = load_friends()

    if q:
        # Filter friends based on the query string (e.g., by name)
        filtered_friends = [friend for friend in friends if q.lower() in friend["name"].lower()]
        return JSONResponse(content=filtered_friends)

    return JSONResponse(content=friends)

@app.get("/you/")
def read_you(q: Union[str, None] = None):
    you = load_you()

    if q:
        # Filter friends based on the query string (e.g., by name)
        filtered_you = [item for item in you if q.lower() in item["name"].lower()] 
        return JSONResponse(content=filtered_you)

    return JSONResponse(content=you)