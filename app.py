from Read import read_home, read
from fastapi.templating import Jinja2Templates
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI()

templates = Jinja2Templates(directory="templates")
@app.get('/')
def main(request: Request):
    return templates.TemplateResponse('index.html', {'request': request})
@app.get('/repo')
def repo(request: Request):
    return templates.TemplateResponse('repo.html', {'request': request})

@app.get("/api/read_developer")
async def read_developer(github_id : str = None):
    name = github_id
    if not name:
        return JSONResponse({"error": "Missing 'name' parameter"}, status_code=400)
    res = await read_home(name)
    return JSONResponse({"information" : res.to_dict()}, status_code=200)

@app.get("/api/read_repo")
async def read_repo(github_id : str = None):
    name = github_id
    if not name:
        return JSONResponse({"error": "Missing 'name' parameter"}, status_code=400)
    res = await read(name)
    data = []
    for item in res:
        data.append({key: value.to_dict() if hasattr(value, 'to_dict') else value for key, value in item.items()})
    return JSONResponse({"information" : data}, status_code=200)