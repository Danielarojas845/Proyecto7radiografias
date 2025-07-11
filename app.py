from flask import Flask, request, jsonify
import numpy as np
from PIL import Image
import tensorflow as tf
from tensorflow.keras.models import load_model
import io

app = Flask(__name__)

# === CARGA DEL MODELO ===
model = load_model('modelo_final_tuneado_radiografias.keras')

# Función para preprocesar la imagen
def preprocess_image(image_bytes):
    img = Image.open(io.BytesIO(image_bytes)).convert('L')  # Escala de grises
    img = img.resize((256, 256))  # Tamaño usado en entrenamiento
    img_array = np.array(img).astype('float32') / 255.0
    img_array = np.expand_dims(img_array, axis=(0, -1))  # (1, 256, 256, 1)
    return img_array

# === ENDPOINT DE PREDICCIÓN ===
@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({'error': 'No se envió ninguna imagen.'}), 400

    file = request.files['file']
    image_bytes = file.read()
    processed_image = preprocess_image(image_bytes)

    prediction = model.predict(processed_image)[0][0]

    # Recordatorio: el modelo fue entrenado con 0 = NORMAL, 1 = PNEUMONIA_REDUCIDO
    class_label = 'NEUMONIA' if prediction >= 0.5 else 'NORMAL'
    probability = float(prediction) if prediction >= 0.5 else float(1 - prediction)

    print("Probabilidad cruda:", float(prediction))
    print("Diagnóstico:", class_label)

    return jsonify({
        'prediccion': class_label,
        'probabilidad': round(probability, 4)
    })

# === EJECUTAR APP ===
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)

