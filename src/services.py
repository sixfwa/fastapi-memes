from typing import List
import os as _os
import random as _random
import time as _time
import fastapi as _fastapi
import imghdr as _img


def _get_image_filenames(directory_name: str) -> List[str]:
    return _os.listdir(directory_name)


def select_random_image(directory_name: str) -> str:
    images = _get_image_filenames(directory_name)
    random_image = _random.choice(images)
    path = f"{directory_name}/{random_image}"
    return path


def _is_image(filename: str):
    valid_extensions = (".png", ".jpg", ".jpeg", ".gif")
    return filename.endswith(valid_extensions)


def upload_image(directory_name: str, image: _fastapi.UploadFile):
    if _is_image(image.filename):
        timestr = _time.strftime("%Y%m%d-%H%M%S")
        image_name = timestr + image.filename.replace(" ", "-")
        with open(f"{directory_name}/{image_name}", "wb+") as image_upload:
            image_upload.write(image.file.read())

        return file_name
    return None
