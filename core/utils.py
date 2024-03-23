import os
from flask import jsonify


def response(
    data,
    success=1,
    status_code=200,
):
    if success:
        payload = {
            "data": data,
        }
    else:
        payload = {
            "error": data,
        }
        if not status_code:
            status_code = 400
    res = {"success": success, "payload": payload}

    return jsonify(res), status_code


def clear_dir(dir, size=5):
    images = os.listdir(dir)
    # sort by creation time
    images.sort(key=lambda x: os.path.getctime(os.path.join(dir, x)))
    for i in range(len(images) - size):
        os.remove(os.path.join(dir, images[i]))
