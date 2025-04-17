import os
import cv2
import numpy as np
from tensorflow.keras.preprocessing import image


class LoadModel:
    def __init__(self,model=None):
        self.model =  model
        if self.model is None:
            self.model = self.get_model()

    def get_model(self):
        from keras.saving.save import load_model
        model_name = "efficientnet_fixed_model.h5"
        model = load_model('output/' + model_name)
        return model

    def get_disease(self,path):
        img = cv2.imread(path)
        img = cv2.resize(img, (128, 128))
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        kopya = img.copy()
        kopya = cv2.cvtColor(kopya, cv2.COLOR_RGB2GRAY)
        blur = cv2.GaussianBlur(kopya, (5, 5), 0)
        thresh = cv2.threshold(blur, 10, 255, cv2.THRESH_BINARY)[1]
        kontur = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        kontur = kontur[0][0]
        kontur = kontur[:, 0, :]
        x1 = tuple(kontur[kontur[:, 0].argmin()])[0]
        y1 = tuple(kontur[kontur[:, 1].argmin()])[1]
        x2 = tuple(kontur[kontur[:, 0].argmax()])[0]
        y2 = tuple(kontur[kontur[:, 1].argmax()])[1]
        x = int(x2 - x1) * 4 // 50
        y = int(y2 - y1) * 5 // 50
        kopya2 = img.copy()
        if x2 - x1 > 100 and y2 - y1 > 100:
            kopya2 = kopya2[y1 + y: y2 - y, x1 + x: x2 - x]
            kopya2 = cv2.resize(kopya2, (128, 128))
        lab = cv2.cvtColor(kopya2, cv2.COLOR_RGB2LAB)
        l, a, b = cv2.split(lab)
        clahe = cv2.createCLAHE(clipLimit=5.0, tileGridSize=((8, 8)))
        cl = clahe.apply(l)
        limg = cv2.merge((cl, a, b))
        son = cv2.cvtColor(limg, cv2.COLOR_LAB2RGB)
        med_son = cv2.medianBlur(son, 3)
        arka_plan = cv2.medianBlur(son, 37)
        maske = cv2.addWeighted(med_son, 1, arka_plan, -1, 255)
        son_img = cv2.bitwise_and(maske, med_son)

        img_array = image.img_to_array(son_img)

        # Normalize et
        img_array = img_array / 255.0

        # Batch boyutu ekle (1, 128, 128, 3)
        img_array = np.expand_dims(img_array, axis=0)

        # Tahmin yap
        predictions = self.model.predict(img_array)

        return predictions.argmax() # en yüksek tahmin edilen sınıf


