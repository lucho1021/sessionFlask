# paquete para el manejo del sistema operativo
import os
from flask import Flask, render_template, redirect, request,flash
from werkzeug.utils import secure_filename

app = Flask(__name__)

app.secret_key = 'dsklfj3w4t'

# configurar la carpeta para almacenar los archivos (imagenes)
app.config['UPLOAD_FOLDER'] = 'static/images'

@app.route('/')
def index():
    return render_template("upload.html")

@app.route('/upload', methods=['POST'])
def upload():
    if request.method == 'POST':
        f = request.files['ufile']
        filename = secure_filename(f.filename)
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        flash("La imagen se ha subido correctamente ...")
        return redirect('/')

if __name__ == "__main__":
    app.run(debug=True, port=4500)
