import glob
import os
import pickle
from PIL import Image
from feature_extractor import FeatureExtractor
import cv2
import numpy as np
import json

PATH = "static/img/"
fe = FeatureExtractor()
data = {}

if (os.path.exists(PATH)):
    files = os.listdir(PATH)
    for file in files:
        m = os.path.join(PATH, file)
        if (os.path.isdir(m)):
            feature_sum = np.zeros((1, 128))
            img_nums = 0
            for img_path in sorted(glob.glob(m + '/*')):
                print(img_path)
                try:
                    img = cv2.imdecode(np.fromfile(img_path,dtype=np.uint8),-1)
                    feature = fe.extract(img)
                    if feature is not None:
                        feature_sum += feature
                        img_nums += 1
                except Exception as e:
                    print(e)
            if img_nums > 0:
                feature_avg = feature_sum / img_nums
                data[file] = feature_avg.tolist()
    with open("features.json","w") as f:
        json.dump(data, f, ensure_ascii=False)
        f.close()




