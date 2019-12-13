import numpy as np
from PIL import Image
from feature_extractor import FeatureExtractor
import time
from flask import Flask, request, render_template
import json
import cv2

app = Flask(__name__)


def return_euclidean_distance(feature_1, feature_2):
    feature_1 = np.array(feature_1)
    feature_2 = np.array(feature_2)
    dist = np.sqrt(np.sum(np.square(feature_1 - feature_2)))
    return dist

fe = FeatureExtractor()
with open("features.json", "r") as f:
    data = json.load(f)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['query_img']

        query_img = Image.open(file.stream)  # PIL image
        uploaded_img_path = "static/uploaded/" + str(time.time()) + "_" + file.filename
        query_img.save(uploaded_img_path)
        query_img = cv2.cvtColor(np.asarray(query_img), cv2.COLOR_RGB2BGR)
        query_img_feature = fe.extract(query_img)
        result_dist = np.float(10)
        for name, feaure in data.items():
            temp_dist = return_euclidean_distance(feaure, query_img_feature)
            if temp_dist < result_dist:
                result_name = name
                result_dist = temp_dist
        if result_dist > 0.4:
            result_name = "抱歉，没有查询到该位明星"
            result_url = "#"
        else:
            result_url = "https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=2&ch=&tn=02003390_3_hao_pg&bar=&wd="+result_name+"&rsv_spt=1&oq=%25E7%2599%25BE%25E5%25BA%25A6%25E7%25BD%2591%25E9%25A1%25B5%25E6%2590%259C%25E7%25B4%25A2%25E8%25BF%259E%25E6%258E%25A5&rsv_pq=addc279f0002c620&rsv_t=9751I7HpZclwH%2FvNHGc8TG2LMpeBZmu2JpmMjp%2BV383%2FEaFmpjBkYLBQZ2PWuaG55K1tcFEYuAg&rqlang=cn&rsv_enter=1&rsv_dl=tb&inputT=898"

        return render_template('index.html',
                               query_path=uploaded_img_path,
                               result_url=result_url,
                               result_name=result_name,
                               result_dist=result_dist)
    else:
        return render_template('index.html')

if __name__=="__main__":
    app.run("0.0.0.0")
