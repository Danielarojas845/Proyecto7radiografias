# Proyecto7radiografias
Proyecto 7, CNN con Keras, predicción de Neumonía a través de radiografías de tórax. 

Este proyecto utiliza redes neuronales convolucionales (CNN) para clasificar radiografías de tórax entre casos normales y de neumonía.

· Estructura del proyecto 
- `modelo\\\_final\\\_tuneado\\\_radiografias.keras` modelo entrenado
- `app.py` API Flask
- `predict.py` script de predicción
- `README.md` este archivo
  

· Cómo ejecutar localmente la API
- Sigue estos pasos para ejecutar el proyecto Flask desde tu computador:
. Abre una terminal o consola
En Windows, puedes usar cmd

2. Navega a la carpeta del proyecto

Activar: 
.\venv\Scripts\activate
python -m venv venv


Instalar 
pip install flask tensorflow pillow 


Ejecutar 
python app.py



* Running on http://127.0.0.1:8000/ (Press CTRL+C to quit)
Abre el navegador y poner http://127.0.0.1:8000


· Cómo probar la API
Una vez que la API esté corriendo en `http://127.0.0.1:8000`, puedes probarla de dos maneras:


1\. Desde el navegador (si tienes interfaz)

Abre el navegador y ve a:  
`http://127.0.0.1:8000`
Sube una imagen de rayos X y espera el diagnóstico.

2. Desde Talend API Tester o Postman:
- Método: `POST`
- URL: `http://127.0.0.1:8000/predict`
- En el body:
- Tipo: `form-data`
- Campo: `file`
- Tipo: archivo (subes una radiografía)
- Ejemplo de respuesta esperada:
```json
{"probabilidad": 0.9382,
"diagnóstico": "NEUMONIA"}

El archivo es muy pesado, comparto el google colab por aqui: https://drive.google.com/file/d/1GdxDx0grtyHpr8FGs1thEUPBowsot_6M/view?usp=sharing
Se inento subir por ambas vías, más no se logró.
Se envía el link por Google colab: https://colab.research.google.com/drive/1GdxDx0grtyHpr8FGs1thEUPBowsot_6M  


