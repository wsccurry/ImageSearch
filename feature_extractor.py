import dlib  # 人脸识别的库dlib
import numpy as np  # 数据处理的库numpy

# face recognition model, the object maps human faces into 128D vectors
facerec = dlib.face_recognition_model_v1("model/dlib_face_recognition_resnet_model_v1.dat")
# Dlib 预测器
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor('model/shape_predictor_68_face_landmarks.dat')

class FeatureExtractor:
    def __init__(self):
        pass

    def extract(self,img):
        dets = detector(img,1)
        # 检测到人脸
        if len(dets) != 0:
            shape = predictor(img, dets[0])
            face_descriptor = facerec.compute_face_descriptor(img, shape)
            face_array = np.array(face_descriptor).reshape((1, 128))
            return face_array
        return



