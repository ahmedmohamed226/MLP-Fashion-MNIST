import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image

# Load the trained model
model = tf.keras.models.load_model("mlp_model.keras")

# Page configuration
st.set_page_config(
    page_title="Fashion MNIST Classifier",
    page_icon="👕"
)

st.title("Fashion MNIST Classifier")
st.write("Upload an image and let the MLP model predict the clothing category.")

# Test with a Fashion-MNIST image
st.subheader("Test the Model")

if st.button("Test Random Image"):

    # Load Fashion-MNIST test dataset
    (_, _), (x_test, y_test) = tf.keras.datasets.fashion_mnist.load_data()

    # Select a random image
    index = np.random.randint(0, len(x_test))
    image = x_test[index]
    true_class = y_test[index]

    # Display image
    st.image(
        image,
        caption="Fashion-MNIST Test Image",
        width=200
    )

    # Prepare image for prediction
    image_array = image.astype("float32") / 255.0
    image_array = np.expand_dims(image_array, axis=0)

    # Prediction
    prediction = model.predict(image_array, verbose=0)
    predicted_class = np.argmax(prediction[0])

    class_names = [
        "T-shirt/top",
        "Trouser",
        "Pullover",
        "Dress",
        "Coat",
        "Sandal",
        "Shirt",
        "Sneaker",
        "Bag",
        "Ankle boot"
    ]

    st.write(f"**Actual:** {class_names[true_class]}")
    st.success(f"**Prediction:** {class_names[predicted_class]}")