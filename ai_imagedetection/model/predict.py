from tensorflow.keras.applications.imagenet_utils import decode_predictions
from PIL import Image
import numpy as np
from .model_loader import model

# 이미지를 예측해서 결과를 알려주는 함수
def predict(image: Image.Image):
    image = np.asarray(image.resize((224, 224)))[..., :3]   # RGB
    image = np.expand_dims(image, 0)
    image = image / 127.5 - 1.0
    result = decode_predictions(model.predict(image), 2)[0]
    response = []
    for res in result:
        response.append({"class": res[1], "predictions": f"{res[2]*100:0.2f} %"})
    return response