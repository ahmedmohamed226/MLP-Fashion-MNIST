Fashion MNIST Classification using MLP

Project Description
This project uses a Multi-Layer Perceptron (MLP) neural network to classify images from the Fashion MNIST dataset into 10 different clothing categories.

Dataset
The project uses the Fashion MNIST dataset provided by TensorFlow/Keras.

The dataset contains grayscale images with a size of 28x28 pixels.

The 10 classes are:
1. T-shirt/top
2. Trouser
3. Pullover
4. Dress
5. Coat
6. Sandal
7. Shirt
8. Sneaker
9. Bag
10. Ankle boot

Model
The trained MLP model is saved as:

mlp_model.keras

Application
The project includes a Streamlit web application in:

app.py

The application loads the trained model and allows the user to test the model using random images from the Fashion MNIST test dataset.

Requirements
The required Python libraries are listed in:

Req.txt

Main libraries:
- TensorFlow
- Streamlit
- NumPy
- Pillow

How to Run the Application
1. Open the project folder in PyCharm.
2. Open the Terminal.
3. Install the required libraries using:

pip install -r Req.txt

4. Run the Streamlit application using:

streamlit run app.py

5. Open the Local URL provided by Streamlit in the web browser.

How the Application Works
1. The trained MLP model is loaded from mlp_model.keras.
2. A random image is selected from the Fashion MNIST test dataset.
3. The image is displayed in the application.
4. The image is normalized and prepared for the model.
5. The MLP model predicts the clothing category.
6. The application displays both the actual class and the predicted class.

Project Structure

Project/
│
├── app.py
├── mlp_model.keras
├── README.txt
├── Req.txt
└── src/

Conclusion
This project demonstrates how a trained MLP neural network can be integrated into a simple Streamlit application for image classification using the Fashion MNIST dataset.
