import json
from fastapi import FastAPI,Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "https://fnd-api.herokuapp.com/",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



@app.get("/")
def home():
    return {"DATA" : "Test"}

@app.post('/get_url')
async def get_url(self, request: Request):
    body = await request.body()
    json_body = json.loads(body)
    self.response_data = {
                "msg": json_body
            }
    return self.respond_api()

def respond_api(self):
        return JSONResponse(content=self.response_data, status_code=self.response_code)
