import pandas as pd
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import Sequential, load_model
from tensorflow.keras.layers import Dense, Input
from tensorflow.keras.losses import BinaryCrossentropy
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.callbacks import EarlyStopping
import numpy as np
import keras

df = pd.DataFrame

try:
    df = pd.read_csv('../data/mushrooms.csv')
except FileNotFoundError:
    print(f"\033[93m\n>>>>>>>>>>>>> Data-csv not found. To preprocess the data first run preprocessMushroomData.py <<<<<<<<<<<<<")
    exit(1)


x = df.drop('class', axis=1)
y = df['class']

print(x)
print(y)

model = 1

try:
    model = keras.models.load_model('mushroom_model.keras')
    print(f"\033[93mModel loaded from workspace... continue with loaded model")
except:
    print(f"\033[93mModel not created yet... creating new model")

if model == 1:
    x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=0.2)

    model = Sequential([
        Input(shape=(len(x_train.columns),)),
        Dense(64, activation='relu'),
        Dense(32, activation='relu'),
        Dense(1, activation='sigmoid')
    ])

    model.compile(optimizer=Adam(learning_rate=0.001),
                  loss=BinaryCrossentropy(),
                  metrics=['accuracy', 'AUC'])

    early_stopping = EarlyStopping(monitor='loss', patience=10)

    model.fit(x_train, y_train, epochs=100, batch_size=32, callbacks=[early_stopping])

    test_acc = model.evaluate(x_test, y_test)

    model.save('mushroom_model.keras')

    print('\nTest accuracy:', test_acc)

    predictions = model.predict(x_test)

    print(predictions)


# Input data as a 1D list (your current input)
input_data = [5.29, 4.0, 7.0, 1.0, 0.0, 3.0, 1.0, 9.0, 5.54, 6.69, 0.0, 1.0, 1.0, 0.0, 0.0, 1.0, 0.0, 0.0, 8.0, 3.0]

# Convert to a 2D numpy array (add an extra dimension to make it 2D)
input_data_reshaped = np.array(input_data).reshape(1, -1)

# Use the reshaped data for prediction
custom_prediction = model.predict(input_data_reshaped)

expected = 1
print(f'expected: {expected}, actual: {custom_prediction}')

