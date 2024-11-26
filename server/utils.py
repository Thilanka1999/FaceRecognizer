import joblib
import json
import numpy as np
import base64
import cv2
from wavelet import w2d

__model = None

__name_to_num = {}
__num_to_name = {}



def classify(img_base64_data):

    cropped_imges = get_cropped(img_base64_data)
    results =  []
    for faces in cropped_imges:
        resize_raw = cv2.resize(faces, (32, 32))
        wave_img = w2d(faces, 'db1', 5)
        resize_wave = cv2.resize(wave_img, (32, 32))
        reshape_raw = resize_raw.reshape(32*32*3, 1)
        reshape_wave = resize_wave.reshape(32*32, 1)
        stacked = np.vstack((reshape_raw, reshape_wave))
        single_arry_img = stacked.reshape(1, 32*32*3 + 32*32).astype(float)
        print(__model.predict(single_arry_img)[0])
        results.append({
            "class": __num_to_name[__model.predict(single_arry_img)[0]],
            "class_probs": np.around(__model.predict_proba(single_arry_img)*100, 2).tolist()[0],
            "class_dick": __name_to_num

        })
        

    # out = __model.predict(cropped_imges)
    return results


def test_virat():
    with open('b64.txt', 'r') as f:
        return f.read()
    

def base64_cv2img(img_base64_data):
    encoded_data = img_base64_data.split(',')[1]
    nparr = np.frombuffer(base64.b64decode(encoded_data), np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    return img



def get_cropped(img_base64_data):
    faces_cascade = cv2.CascadeClassifier("haarcascades/haarcascade_frontalface_default.xml")
    eye_cascade = cv2.CascadeClassifier("haarcascades/haarcascade_eye.xml")

    img = base64_cv2img(img_base64_data)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)    
    faces = faces_cascade.detectMultiScale(gray, 1.3, 5)
    cropped_faces = []
    for x, y, w, h in faces:   
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]     
        eyes = eye_cascade.detectMultiScale(roi_gray)
        if len(eyes) >= 2:
            cropped_faces.append(roi_color)
    return cropped_faces

def load_saved_artifacts():
    global __name_to_num
    global __num_to_name

    with open('artifacts/class_dictionary.json', 'r') as f:
        __name_to_num = json.load(f)
        __num_to_name = {v:k for k,v in __name_to_num.items()}
    global __model
    if __model is None:
        with open("artifacts/saved_model.pkl", 'rb') as f:
            __model = joblib.load(f)




if __name__ == '__main__':
    load_saved_artifacts()
    print(classify(test_virat()))