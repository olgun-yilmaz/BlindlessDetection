import os
import cv2
import numpy as np
from tensorflow.keras.preprocessing import image

from src.module.ai_module import apply_preprocessing


class LoadModel:
    def __init__(self,model=None):
        self.model =  model
        if self.model is None:
            self.model = self.get_model()

    def get_model(self):
        from keras.saving.save import load_model
        model_name = "new_model.h5"
        model = load_model('models/' + model_name)
        return model

    def get_disease(self,path):
        img = cv2.imread(path, cv2.IMREAD_COLOR)
        final_img = apply_preprocessing(img)

        img_array = image.img_to_array(final_img)

        # Normalize et
        img_array = img_array / 255.0

        img_array = np.expand_dims(img_array, axis=0)

        # Tahmin yap
        predictions = self.model.predict(img_array)

        max_value = np.max(predictions)

        if max_value > 0.8:
            pred = predictions.argmax()
        else:
            pred = -1

        return pred # en yüksek tahmin edilen sınıf


