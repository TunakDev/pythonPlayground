import pandas as pd
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import Sequential, load_model
from tensorflow.keras.layers import Dense, Input
from sklearn.metrics import accuracy_score

df = pd.read_csv('../data/Board_RGB_data_small.csv')

x = df.drop('Grey', axis=1)
y = df['Grey']

x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=0.2)

print(x_train.head())
print(x_test.head())

model = Sequential()
model.add(Input(shape=(len(x_train.columns),)))
model.add(Dense(units=64, activation='relu'))
model.add(Dense(units=1, activation='sigmoid'))

model.compile(loss='binary_crossentropy', optimizer='sgd', metrics=['accuracy'])

model.fit(x_train, y_train, epochs=50, batch_size=32)

y_hat = model.predict(x_test)
y_hat = [0 if val < 0.5 else 1 for val in y_hat]

print(accuracy_score(y_test, y_hat))

model.export('./tfmodel_rgb')