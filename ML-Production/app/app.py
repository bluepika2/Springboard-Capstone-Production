from flask import Flask, request, render_template
from inference import get_mask
from commons import get_tensor
from base64 import b64encode
from werkzeug.utils import secure_filename
from torchvision.utils import save_image
import io

HOST = '0.0.0.0'
PORT = 8888

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def predict():
    if request.method == 'GET':
        return render_template('index.html')
    if request.method == 'POST':
        print(request.files)
        if 'file' not in request.files:
            print('file not uploaded')
            return
        file = request.files['file']
        image = file.read()
        mask = get_mask(image_bytes=image)
        file_object = io.BytesIO()
        save_image(mask, file_object, format='PNG')
        base64img = "data:image/png;base64,"+b64encode(file_object.getvalue()).decode('ascii')
        return render_template('result.html', base64img=base64img)
if __name__ == '__main__':
    app.run(host=HOST, debug=True, port=PORT)