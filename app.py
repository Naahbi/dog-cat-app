from flask import Flask, request, jsonify
from utils import predict_image

app = Flask(__name__)

@app.route("/predict", methods=["POST"])
def predict():
    if "image" not in request.files:
        return jsonify({"error":"No image uploaded"}), 400
    image_file = request.files["image"]
    result = predict_image(image_file)
    return jsonify(result)

if __name__ == "__main__" :
    app.run(debug=True)