import cv2
import numpy as np
import tensorflow as tf
import pandas as pd
from keras.layers import Dense,Dropout
from keras.models import Model
from keras_preprocessing.image import ImageDataGenerator
#####################################################################
# Create dataset for training model
PATH = 'Data'
training_datagen = ImageDataGenerator(rescale = 1./255)
train_generator = training_datagen.flow_from_directory(PATH,target_size=(64,64),class_mode='categorical',batch_size=126)
label = ["Dark","Haze","Ok"]

#####################################################################
# Build model
def classify():
    model = tf.keras.applications.MobileNetV3Small()
    model.summary()
    x = Dense(20, activation='relu', kernel_regularizer= tf.keras.regularizers.L2(l2=5e-3))(model.output)
    x = Dropout(0.03)(x)
    x = Dense(10, activation='relu', kernel_regularizer= tf.keras.regularizers.L2(l2=1e-3))(x)
    x = Dropout(0.03)(x)
    output = Dense(3,activation='softmax', kernel_regularizer= tf.keras.regularizers.L2(l2=1e-2))(x)
    model_build = Model(inputs=[model.input], outputs=output)
    #model_build.summary()
    return model_build

# Training model
model = classify()
model.compile(optimizer=tf.keras.optimizers.Adam(0.0005), loss='categorical_crossentropy', metrics=['Accuracy'])
model.fit(train_generator,batch_size=64, epochs=100, shuffle=True)
model.save('Train.h5')
