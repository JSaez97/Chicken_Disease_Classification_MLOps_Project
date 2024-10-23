import numpy as np
import os
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image


class PredictionPipeline:
    def __init__(self, filename):
        self.filename = filename
        
    def predict(self):
        model = load_model(os.path.join("artifacts", "training", "model.h5"))
    
        imagename = self.filename
        test_image = image.load_img(imagename, target_size=(224, 224))
        test_image = image.img_to_array(test_image)
        test_image = test_image / 255.0  # Normalize the image
        test_image = np.expand_dims(test_image, axis=0)
    
        # Make predictions
        predictions = model.predict(test_image)
        print(f"Raw model predictions: {predictions}")  # Debugging output
    
        result = np.argmax(predictions, axis=1)
        print(f"Argmax result: {result}")  # Debugging output
    
        # Class labels mapping
        class_labels = {
            0: "Coccidiosis",
            1: "Healthy",
            2: "New_Castle_Disease",
            3: "Salmonella"
        }
    
        # Get the prediction
        prediction = class_labels.get(result[0], "Unknown")  # Default to "Unknown" if index not found
        print(f"Final prediction: {prediction}")  # Debugging output
    
        return [{"image": prediction}]

