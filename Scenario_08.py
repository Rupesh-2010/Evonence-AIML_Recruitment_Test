# Scenario 8: Model Callbacks
# Task: Implement an EarlyStopping callback that stops training if
# validation loss doesn’t improve for 3 epochs and restores the best weights.

#TensorFlow is a machine learning library used to build and train AI models,
# especially for deep learning like image, text, and speech recognition.

import tensorflow as tf                     # Import TensorFlow library

early_stop = tf.keras.callbacks.EarlyStopping(
    monitor="val_loss",                 # Watch validation loss
    patience=3,                            # Stop after 3 bad epochs
    restore_best_weights=True                    # Load best model weights
)

# Use this during training
# model.fit(train_ds, validation_data=val_ds, epochs=50, callbacks=[early_stop])

