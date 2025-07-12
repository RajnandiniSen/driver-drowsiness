from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
from tensorflow.keras.preprocessing.image import ImageDataGenerator

model = Sequential([
    Conv2D(32, (3,3), activation = 'relu', input_shape = (24, 24, 1)),
    MaxPooling2D(2,2),
    Conv2D(32, (3,3), activation= 'relu'),
    MaxPooling2D(2,2),
    Conv2D(64, (3,3), activation='relu'),
    MaxPooling2D(2,2),
    Flatten(),
    Dense(128, activation='relu'),
    Dense(2, activation='softmax')
])

model.compile(optimizer = 'adam', loss = 'categorical_crossentropy', metrics = ['accuracy'])

train_datagen = ImageDataGenerator(rescale = 1./255, validation_split = 0.2)

train_generator = train_datagen.flow_from_directory(
    'dataset',
    target_size = (24, 24),
    color_mode = 'grayscale',
    batch_size = 32,
    class_mode = 'categorical',
    subset = 'training'
)

val_generator = train_datagen.flow_from_directory(
    'dataset',
    target_size = (24, 24),
    color_mode = 'grayscale',
    batch_size = 32,
    class_mode = 'categorical',
    subset = 'validation'
)

history = model.fit(train_generator, epochs=10, validation_data=val_generator)

print("Final Training Accuracy:", history.history['accuracy'][-1])
print("Final Validation Accuracy:", history.history['val_accuracy'][-1])

model.save('models/cnnCat2.h5')

