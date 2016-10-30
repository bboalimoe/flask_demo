__author__ = 'zhanghengyang'

from flask import Flask
import os
import json
from flask import request
import uuid
import numpy as np
app = Flask(__name__)


@app.route('/upload', methods=['GET', 'POST'])
def upload():
    print request.method
    print request.files.__dict__

    if request.method == 'POST':
        print request.files.__dict__
        file = request.files['filename']
        #stream = file['stream']
        print "dir", dir(request)
        print "dict",request.__dict__
        print
        data = request.data
        rstream = file.stream.read()
        print rstream
        barray = np.asarray(bytearray(rstream))
        print dir(file)
        import cv2
        img = cv2.imdecode(barray,1)
        print img
        print "file info",file
        file.save('./uploaded_file.jpg')

        return "success"
        # extension = os.path.splitext(file.filename)[1]
        # f_name = str(uuid.uuid4()) + extension
        # file.save(os.path.join(app.config['UPLOAD_FOLDER'], f_name))
        # return json.dumps({'filename':f_name})



if __name__ == "__main__":
    app.debug = True
    app.run(port=8080)
