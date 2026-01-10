# Scenario 7: Image Augmentation
# Task: Use TensorFlow/Keras to create an image augmentation pipeline
# with random rotations (±20 degrees), horizontal flips, and zoom (0.2x).


#####################################    ANSWER      #####################################


import tensorflow as tf                  # TensorFlow main library imported
from tensorflow.keras import layers           # Keras neural layers (not yet support Python 3.12 properly)

data_augmentation = tf.keras.Sequential([    # Image augmentation pipeline
    layers.RandomFlip("horizontal"),         # Random horizontal flipping
    layers.RandomRotation(factor=0.0555),    # Random rotation up to 20°
    layers.RandomZoom(0.2)                   # Random zoom augmentation
])

inputs = tf.keras.Input(shape=(224, 224, 3))    # Input image shape
x = data_augmentation(inputs)                    # Apply augmentation on input
x = layers.Conv2D(32, 3, activation="relu")(x)      # Convolution feature extraction
x = layers.GlobalAveragePooling2D()(x)           # Reduce spatial dimensions (2D)
outputs = layers.Dense(2, activation="softmax")(x)  # Final class prediction
model = tf.keras.Model(inputs, outputs)         # Build the model
model.summary()                                 # calling the function




