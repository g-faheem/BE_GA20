from keras.models import  model_from_json
from keras.models import load_model
import cv2
import numpy as np
import h5py


def face_emotion_detection():

    emotions = ["anger", "contempt", "disgust", "fear", "happy", "sadness", "surprise"]
    finemotions=["negative","neutral","positive"]

    # Load the saved model

    json_file = open('model.json', 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    model = model_from_json(loaded_model_json)
    # load weights into new model
    model.load_weights("emotion_recognition_model.h5")


    # evaluate loaded model on test data
    model.compile(loss='binary_crossentropy', optimizer='rmsprop', metrics=['accuracy'])


    # Load a custom image
    custom_img_path = ("C:/Users/princ/PycharmProjects/EmoReg/app_code/captures/image.jpg")
    custom_img = cv2.imread(custom_img_path, cv2.IMREAD_GRAYSCALE)
    custom_img = cv2.resize(custom_img, (48, 48))
    custom_img = custom_img.astype("float32") / 255.0
    custom_img = custom_img.reshape(1, 48, 48, 1)

    # Make a prediction on the custom image
    preds = model.predict(custom_img)
    finpreds = np.zeros((1, 3))
    finpreds[0,0]=preds[0,0]+preds[0,1]+preds[0,2]+preds[0,3]+preds[0,5]
    finpreds[0,1]=preds[0,6]
    finpreds[0,2]=preds[0,4]
    emotion_idx = np.argmax(preds)
    emotion = emotions[emotion_idx]
    finemotion_idx = np.argmax(finpreds)
    finemotion = finemotions[finemotion_idx]
    return finemotion


