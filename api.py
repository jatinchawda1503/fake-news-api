import json
from urllib import response
from fastapi import FastAPI,Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from fakenews.inference import make_predictions
from scraper import scrape_data
import pandas as pd


app = FastAPI()
# import sys
# #print(sys.path)
# import site 
# print(site.getsitepackages()[-1])


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

url = []
print(url)




@app.post("/")
async def get_url(request: Request):
    body = await request.json()
    res = list(body.values())[0]
    data = scrape_data(res)
    result = make_predictions(data)
    if result == 0:
        response = "This is True news"
    else:
        response = "This is Fake news"
    print(response)
    return {response}


# @app.get("/get_prediction")
# def get_prediction():
#     response = get_url(Request)
#     print(response)
#     #data = scrape_data(response)
#     data = pd.read_csv('data/test.csv')
#     result = make_predictions(data)
#     if result == 0:
#         response = "This is True news"
#     else:
#         response = "This is Fake news"
#     print(response)
#     return {response}