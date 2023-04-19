# vgg16 model used for transfer learning
import sys
from matplotlib import pyplot
from keras.utils import to_categorical
from keras.applications.vgg16 import VGG16
from keras.models import Model
from keras.layers import Dense
from keras.layers import Flatten
from keras.optimizers import SGD
from keras.preprocessing.image import ImageDataGenerator

# ----
import keras
from keras.callbacks import TensorBoard
import tensorflow as tf
import numpy as np
from random import seed
import time
import datetime
import os
import matplotlib.pyplot as plt
import io

os.environ['PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION'] = 'python'
# ----|

# define cnn model
def define_model():
	# load model
	model = VGG16(include_top=False, input_shape=(224, 224, 3))
	# mark loaded layers as not trainable
	for layer in model.layers:
		layer.trainable = False
	# add new classifier layers
	flat1 = Flatten()(model.layers[-1].output)
	class1 = Dense(128, activation='relu', kernel_initializer='he_uniform')(flat1)
	output = Dense(1, activation='sigmoid')(class1)
	# define new model
	model = Model(inputs=model.inputs, outputs=output)
	# compile model
	opt = SGD(lr=0.001, momentum=0.9)
	model.compile(optimizer=opt, loss='binary_crossentropy', metrics=['accuracy'])
	return model

# # plot diagnostic learning curves
# def summarize_diagnostics(history):
# 	# plot loss
# 	pyplot.subplot(211)
# 	pyplot.title('Cross Entropy Loss')
# 	pyplot.plot(history.history['loss'], color='blue', label='train')
# 	pyplot.plot(history.history['val_loss'], color='orange', label='test')
# 	# plot accuracy
# 	pyplot.subplot(212)
# 	pyplot.title('Classification Accuracy')
# 	pyplot.plot(history.history['accuracy'], color='blue', label='train')
# 	pyplot.plot(history.history['val_accuracy'], color='orange', label='test')
# 	# save plot to file
# 	filename = sys.argv[0].split('/')[-1]
# 	pyplot.savefig(filename + '_plot.png')
# 	pyplot.close()

# ----
def plot_to_image(figure):
    """Converts a Matplotlib figure to a TensorFlow image tensor."""
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    image = tf.image.decode_png(buf.getvalue(), channels=4)
    image = tf.expand_dims(image, 0)
    return image
# ----|

# run the test harness for evaluating a model
def run_test_harness():
    # define model
    model = define_model()

    # ----
    # generates a unique subdirectory name for each run
    logs_vgg16 = "logs_vgg16/fit/vgg1_" + datetime.datetime.now().strftime("%H%M%S")
    tensorboard_callback = keras.callbacks.TensorBoard(log_dir=logs_vgg16, histogram_freq=1)
    # ----|

    # create data generator
    datagen = ImageDataGenerator(featurewise_center=True)
    # specify imagenet mean values for centering
    datagen.mean = [123.68, 116.779, 103.939]
    # prepare iterator
    train_it = datagen.flow_from_directory('dataset_rats_vs_squirrels/train/', class_mode='binary', batch_size=64, target_size=(224, 224))
    test_it = datagen.flow_from_directory('dataset_rats_vs_squirrels/test/', class_mode='binary', batch_size=64, target_size=(224, 224))

    # fit model
    # ----
    start_time = time.time()
    history = model.fit(train_it, steps_per_epoch=len(train_it), validation_data=test_it, validation_steps=len(test_it), epochs=10, verbose=2, callbacks=[tensorboard_callback])
    end_time = time.time()
    training_time = end_time - start_time
    print("Training time: ", training_time)
    print("Training loss: ", model.history.history['loss'][-1])
    print("Training accuracy: ", (model.history.history['accuracy'][-1])*100.0)
    # ----|

    # evaluate model
    _, acc = model.evaluate(test_it, steps=len(test_it), verbose=2)
    print('Test accuracy: > %.3f' % (acc * 100.0))

    # ----
    # visualize test images and predictions
    test_it.reset()
    test_images, test_labels = next(test_it)
    test_preds = model.predict(test_images, verbose=0)
    # convert predictions from probabilities to class labels
    test_preds_classes = [1 if x>0.5 else 1 for x in test_preds]
    # log test images and predictions on tensorboard
    logdir = "logs_vgg16/images"
    file_writer = tf.summary.create_file_writer(logdir)
    with file_writer.as_default():
        figure, axes = plt.subplots(nrows=5, ncols=8, figsize=(40, 25))
        for i, ax in enumerate(axes.flat):
            if i < len(test_images):
                ax.imshow(test_images[i])
                ax.set_title("True: {} Pred: {}".format(test_labels[i], test_preds_classes[i]))
                ax.axis("off")
        plt.tight_layout()
        tf.summary.image("Test Images", plot_to_image(figure), step=0)
        tf.summary.scalar("Test Accuracy", acc, step=0)
        print()
    print("Number of model parameters: ", model.count_params())
    # ----|

    # # learning curves
    # summarize_diagnostics(history)

# entry point, run the test harness
run_test_harness()
