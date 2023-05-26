#from Modules.blood_model import blood_pressue
#from Modules.voice_model import voice_emotion
#from Modules.face_model import face_emotion

def most_frequent(List):
    return max(set(List), key = List.count)

def predict_all():
    face = face_emotion.face_emotion_detection()
    voice = voice_emotion.voice_emotion_pred()
    bp = blood_pressue.predict_blood_pressure()
    
    result = most_frequent([face,voice,bp])
    return result









