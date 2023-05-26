import joblib
import numpy as np

def predict_blood_pressure(num):
    model2 = joblib.load(r"Modules/blood_model/emorecmodel.pickle")
    input_arr2 = np.array([num])
    result2 = model2.predict([input_arr2])
    if (result2 == "Happy"):
        result2 = "POSITIVE"
    else:
        result2 = "NEGATIVE"
    return result2
