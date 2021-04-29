import fastapi as _fastapi
import fastapi.encoders as _encoders
import fastapi.responses as _responses


import services as _services

app = _fastapi.FastAPI()


@app.get("/programmer-memes")
def get_programmer_meme():
    image_path = _services.select_random_image("ProgrammerHumor")
    return _responses.FileResponse(image_path)


@app.post("/programmer-memes")
def post_programmer_meme(image: _fastapi.UploadFile = _fastapi.File(...)):
    file_name = _services.upload_image("ProgrammerHumor", image)
    if file_name is None:
        return _fastapi.HTTPException(status_code=409, detail="incorrect file type")
    return _responses.FileResponse(file_name)


@app.get("/cat-memes")
def get_cat_memes():
    image_path = _services.select_random_image("Catmemes")
    return _responses.FileResponse(image_path)


@app.get("/image")
def get_meme():
    return _responses.FileResponse("ProgrammerHumor/tq00bck4mov61.gif")
