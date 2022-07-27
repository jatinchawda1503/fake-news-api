from fastapi import FastAPI,Request
from fakenews.inference import make_predictions
from scraper import scrape_data


app = FastAPI()

@app.post("/")
async def get_url(request: Request):
    body = await request.json()
    res = list(body.values())[0]
    data = scrape_data(res)
    result = make_predictions(data)
    print(result)
    if result == 0:
        response = "This is True news"
    else:
        response = "This is Fake news"
    return {response}
