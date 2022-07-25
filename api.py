import json
from fastapi import FastAPI,Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()




# origins = [
#     "https://fnd-api.herokuapp.com/",
#     "http://127.0.0.1:8000/"
# ]

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )



@app.get("/hello")
def home():
    return {"DATA" : "Test"}

@app.post("/")
async def get_url(request: Request):
    body =  await request.json()
    # json_body = json.loads(body)
    # print(json_body)
    return body


