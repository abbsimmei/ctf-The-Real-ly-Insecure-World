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
        with open("storage/friends.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        raise HTTPException(status_code=500, detail="Friends file not found.")
    except json.JSONDecodeError:
        raise HTTPException(status_code=500, detail="Error decoding friends JSON.")

def load_you():
    try:
        with open("storage/you.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        raise HTTPException(status_code=500, detail="You file not found.")
    except json.JSONDecodeError:
        raise HTTPException(status_code=500, detail="Error decoding you JSON.")

def load_chat(id):
    try:
        # Split the ID into id1 and id2
        id1 = ""
        id2 = ""
        for i in range(len(id)):
            if i % 2 == 0:
                id1 += id[i]
            else:
                id2 += id[i]

        # Try the first file
        try:
            with open(f"storage/chat/{id2}-{id1}.json", "r", encoding="utf-8") as f:
                jsonLoad = json.load(f)
                print(jsonLoad)
                return jsonLoad
        except FileNotFoundError:
            # If the first file isn't found, try the second file
            with open(f"storage/chat/{id1}-{id2}.json", "r", encoding="utf-8") as f:
                jsonLoad = json.load(f)
                print(jsonLoad)
                return jsonLoad

    # Handle errors
    except FileNotFoundError:
        raise HTTPException(status_code=500, detail="Chat file not found.")
    except json.JSONDecodeError:
        raise HTTPException(status_code=500, detail="Error decoding chat JSON.")

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/chat/{chat_id}")
def read_item(chat_id: str):
    chat = load_chat(chat_id)
    return {"item_id": chat}

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