#!/usr/bin/env python
# coding: utf-8

# In[1]:


from keras.layers import Dense
from keras.models import Sequential
from keras.layers import Convolution2D
from keras.layers import MaxPool2D
from keras.layers import Flatten


# In[3]:


classifier = Sequential()


# In[4]:



#Adding Convolution Layer 1

classifier.add(Convolution2D(60,60,3,input_shape=(128,128,3),activation='relu'))
#Pooling
classifier.add(MaxPool2D(pool_size=(2,2)))


# In[5]:


#Adding Convolution Layer 2

classifier.add(Convolution2D(30,20,3,activation='relu'))
classifier.add(MaxPool2D(pool_size=(2,2)))


# In[6]:


#Flatten
classifier.add(Flatten())


# In[7]:


#Full Connection
classifier.add(Dense(output_dim=128,activation='relu'))
#classifier.add(Dense(output_dim=64,activation='relu'))
classifier.add(Dense(output_dim=1,activation='sigmoid'))


# In[11]:


classifier.compile(optimizer='adam',loss='binary_crossentropy',metrics=['accuracy'])


# In[18]:


from keras.preprocessing.image import ImageDataGenerator
train_datagen = ImageDataGenerator(rescale=1./255,
                                   shear_range=0.2,
                                   zoom_range=0.2,
                                   horizontal_flip=True)

test_datagen= ImageDataGenerator(rescale=1./255)

training_set = train_datagen.flow_from_directory('train',
                                                    target_size=(128,128),
                                                    batch_size=32,
                                                    class_mode='binary')

test_set = test_datagen.flow_from_directory('test',
                                                        target_size=(128,128),
                                                        batch_size=32,
                                                        class_mode='binary')

classifier.fit_generator(training_set,
                        steps_per_epoch=40,
                        epochs=2,
                        validation_data=test_set,
                        validation_steps=10,
                        workers=1
                        )


# In[23]:


import numpy as np
from keras.preprocessing import image
test_image = image.load_img('C:/Users/pradeep.nalluri/Desktop/Internship/apbp.jpg', target_size = (128, 128))
test_image = image.img_to_array(test_image)
test_image = np.expand_dims(test_image, axis = 0)
result = classifier.predict(test_image)
training_set.class_indices
if result[0][0] == 1:
    prediction = 'bihar'
else:
    prediction = 'ap'
print(prediction)


# In[25]:


import pickle


# In[26]:



file = 'cnn.pkl'
# Open the file to save as pkl file
cnn_pkl = open(file, 'wb')
pickle.dump(classifier, cnn_pkl)
# Close the pickle instances
cnn_pkl.close()


# In[27]:


cnn_pkl = open(file, 'rb')
cnn = pickle.load(cnn_pkl)
print("Loaded CNN :: ", cnn)

