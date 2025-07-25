import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

# download dataset (internet connection required!)
fashion_mnist = tf.keras.datasets.fashion_mnist

(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()

# list of the class names for classification
class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

# 60k images as 28x28 pixels
print(train_images.shape)
# 60k labels
print(len(train_labels))
# labels are integers ranging from 0 to 9
print(train_labels)
# 10k images as 28x28 pixels
print(test_images.shape)
# 10k labels
print(len(test_labels))

# preprocess data
# we see that the pixel-values range from 0 to 255
plt.figure()
plt.imshow(train_images[0])
plt.colorbar()
plt.grid(False)
plt.show()

# we have to scale the values to a range of 0 to 1 before feeding them to a neural network model
train_images = train_images / 255.0
test_images = test_images / 255.0

# display the first 25 images from the training set as verification and display the class name below each
plt.figure(figsize=(10,10))
for i in range(25):
    plt.subplot(5,5,i+1)
    plt.xticks([])
    plt.yticks([])
    plt.grid(False)
    plt.imshow(train_images[i], cmap=plt.cm.binary)
    plt.xlabel(class_names[train_labels[i]])
plt.show()

# create the model before training
# Flatten transforms the images from a two-dimensional array with 28x28 pixels to a one-dimensional array of 28x28 = 784 pixels
# First layer has no parameters to learn, only transforming the data
# 10 output neurons since we've got 10 classes as an output, and we want a vector with possibilities
model = tf.keras.Sequential([
    tf.keras.layers.Flatten(input_shape=(28, 28)),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(10)
])

# compiling the model
# optimizer = how the model is updated based on the data it sees and its loss function
# loss function = measures how accurate the model is during training. One wants to minimize this function to 'steer' the model in the right direction
# metrics = used to monitor the traning and testing steps
model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])

# training the model
model.fit(train_images, train_labels, epochs=10)

test_loss, test_acc = model.evaluate(test_images,  test_labels, verbose=2)

print('\nTest accuracy:', test_acc)

# training-accuracy was ~91/92%, test accuracy was only 88%. This represents 'overfitting'

# attaching softmax layer to convert the linear outputs to probabilities
# see readme for link to softmax
probability_model = tf.keras.Sequential([model, tf.keras.layers.Softmax()])

# let the model predict some values from the test_images
predictions = probability_model.predict(test_images)

# a single prediction is an array with 10 values. these values represent the model's confidence that the image corresponds
#  to each of the 10 different classes
print(predictions[0])

# print the model's most confident classification
print(np.argmax(predictions[0]))

# check if the model is right
print('expected: ', class_names[test_labels[0]])
print('actual: ', class_names[np.argmax(predictions[0])])

# define functions to graph the full set of 10 class predictions
def plot_image(i, predictions_array, true_label, img):
  true_label, img = true_label[i], img[i]
  plt.grid(False)
  plt.xticks([])
  plt.yticks([])

  plt.imshow(img, cmap=plt.cm.binary)

  predicted_label = np.argmax(predictions_array)
  if predicted_label == true_label:
    color = 'blue'
  else:
    color = 'red'

  plt.xlabel("{} {:2.0f}% ({})".format(class_names[predicted_label],
                                100*np.max(predictions_array),
                                class_names[true_label]),
                                color=color)

def plot_value_array(i, predictions_array, true_label):
  true_label = true_label[i]
  plt.grid(False)
  plt.xticks(range(10))
  plt.yticks([])
  thisplot = plt.bar(range(10), predictions_array, color="#777777")
  plt.ylim([0, 1])
  predicted_label = np.argmax(predictions_array)

  thisplot[predicted_label].set_color('red')
  thisplot[true_label].set_color('blue')

# verify predictions

num_rows = 5
num_cols = 3
num_images = num_rows*num_cols
plt.figure(figsize=(2*2*num_cols, 2*num_rows))
for i in range(num_images):
  plt.subplot(num_rows, 2*num_cols, 2*i+1)
  plot_image(i, predictions[i], test_labels, test_images)
  plt.subplot(num_rows, 2*num_cols, 2*i+2)
  plot_value_array(i, predictions[i], test_labels)
plt.tight_layout()
plt.show()


# use the trained model
# Grab an image from the test dataset.
img = test_images[1]

print(img.shape)

# Add the image to a batch where it's the only member.
img = (np.expand_dims(img,0))

print(img.shape)

predictions_single = probability_model.predict(img)

print(predictions_single)

plot_value_array(1, predictions_single[0], test_labels)
_ = plt.xticks(range(10), class_names, rotation=45)
plt.show()