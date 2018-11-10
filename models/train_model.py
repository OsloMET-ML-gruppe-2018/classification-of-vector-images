import matplotlib.pyplot as plt
import numpy as np
import os, sys

from keras.applications.vgg19 import decode_predictions, preprocess_input, VGG19
from keras.engine import Model
from keras.layers import Dense, Dropout
from keras.optimizers import Adam
from keras.preprocessing.image import ImageDataGenerator
from keras.callbacks import History 
history = History()

from keras.models import model_from_json
from keras.models import load_model

np.random.seed(1234)


#----Augmentation----
#horizontal_flip=True,
#zoom_range=.2,
#rotation_range=30

train_generator = ImageDataGenerator(preprocessing_function=preprocess_input)

train_batches = train_generator.flow_from_directory('..\data\processed\cleaned_categories\\train', target_size=(128, 128), batch_size=4)


val_generator = ImageDataGenerator(preprocessing_function=preprocess_input)
val_batches = val_generator.flow_from_directory('..\data\processed\cleaned_categories\\test', target_size=(128, 128), batch_size=4)

indices = train_batches.class_indices
print("Indices")
print(indices)
labels = [None] * 13
for key in indices:
    labels[indices[key]] = key

print(labels)

pretrained = VGG19(include_top=False, input_shape=(128, 128, 3), weights='imagenet', pooling='max')

for layer in pretrained.layers:
    layer.trainable = False

inputs = pretrained.input
outputs = pretrained.output

#print(inputs)
#print(outputs)


hidden = Dense(128, activation='relu')(outputs)
dropout = Dropout(.3)(hidden)
preds = Dense(13, activation='softmax')(dropout)

model = Model(inputs, preds)
model.compile(loss='categorical_crossentropy', optimizer=Adam(lr=1e-4), metrics=['acc'])

model.summary()

model.fit_generator(train_batches, epochs=100,validation_batch=val_batches, steps_per_epoch=74728//4, callbacks=[history])

# 

model.save('model_state.h5')

print(history.history['acc'])
print(history.history['loss'])
accuracy_per_epoch = history.history['acc']
loss_per_epoch = history.history['loss']


if not os.path.exists('.\plot_data') and not os.path.exists('.\model_state_data'):
    os.mkdir('.\plot_data')
    os.mkdir('.\model_state_data')


with open('.\plot_data\\acc_scores.txt', 'w+') as file:
	for i, acc in enumerate(accuracy_per_epoch):
		file.writelines(str(acc)+'\n')
	file.close()

with open('.\plot_data\loss.txt', 'w+') as file:
	for i, loss in enumerate(loss_per_epoch):
		file.writelines(str(loss)+'\n')
	file.close()

model.save('.\model_state_data\model_state.h5')


#epochs = [i for i in range(len(accuracy_per_epoch))]

#plt.plot(epochs ,accuracy_per_epoch)
#plt.show()
