from flask import Flask, render_template, request, redirect, url_for
import os
import cv2
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import matplotlib

matplotlib.use("agg")

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['PALETTE_PATH'] = 'static/palette.png'

def extract_palette(image_path, num_clusters=5):
    image = cv2.imread(image_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    pixels = image.reshape(-1, 3)

    # Apply KMeans
    kmeans = KMeans(n_clusters=num_clusters, random_state=0)
    kmeans.fit(pixels)
    colors = kmeans.cluster_centers_.astype(int)

    # Plot palette
    palette = np.zeros((50, 300, 3), dtype='uint8')
    step = 300 // len(colors)
    for i, color in enumerate(colors):
        palette[:, i * step:(i + 1) * step, :] = color

    plt.figure(figsize=(8, 2))
    plt.axis('off')
    plt.imshow(palette)
    plt.savefig(app.config['PALETTE_PATH'], bbox_inches='tight', pad_inches=0)
    plt.close()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'image' not in request.files:
            return redirect(request.url)

        file = request.files['image']
        if file.filename == '':
            return redirect(request.url)

        if file:
            # Save uploaded image
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filepath)

            # Generate palette
            extract_palette(filepath)

            return render_template('index.html', uploaded_image=filepath, palette_image=url_for('static', filename='palette.png'))

    return render_template('index.html', uploaded_image=None, palette_image=None)

if __name__ == '__main__':
    app.run(debug=True)
