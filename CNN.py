#!/usr/bin/env python
# coding: utf-8

# In[1]:


from keras.layers import Dense
from keras.models import Sequential
from keras.layers import Convolution2D
from keras.layers import MaxPool2D
from keras.layers import Flatten


# In[2]:


classifier = Sequential()


# In[3]:



#Adding Convolution Layer 1

classifier.add(Convolution2D(60,(3,3),input_shape=(128,128,3),activation='relu'))
#Pooling
classifier.add(MaxPool2D(pool_size=(2,2)))


# In[4]:


#Adding Convolution Layer 2

classifier.add(Convolution2D(30,(3,3),activation='relu'))
classifier.add(MaxPool2D(pool_size=(2,2)))


# In[5]:


#Flatten
classifier.add(Flatten())


# In[6]:


#Full Connection
classifier.add(Dense(activation='relu',units=128))
#classifier.add(Dense(output_dim=64,activation='relu'))
classifier.add(Dense(activation='sigmoid',units=3))


# In[7]:


classifier.compile(optimizer='adam',loss='binary_crossentropy',metrics=['accuracy'])


# In[8]:


from keras.preprocessing.image import ImageDataGenerator
train_datagen = ImageDataGenerator(rescale=1./255,
                                   shear_range=0.2,
                                   zoom_range=0.2,
                                   horizontal_flip=True)

test_datagen= ImageDataGenerator(rescale=1./255)

training_set = train_datagen.flow_from_directory('train',
                                                    target_size=(128,128),
                                                    batch_size=32,
                                                    class_mode='categorical')

test_set = test_datagen.flow_from_directory('test',
                                                        target_size=(128,128),
                                                        batch_size=32,
                                                        class_mode='categorical')

classifier.fit_generator(training_set,
                        steps_per_epoch=50,
                        epochs=2,
                        validation_data=test_set,
                        validation_steps=25,
                        workers=4
                        )


# In[9]:


import numpy as np
import cv2
from keras.preprocessing import image
test_image = image.load_img('testfiles/mpbp.jpg', target_size = (128, 128))
test_image = image.img_to_array(test_image)
test_image = np.expand_dims(test_image, axis = 0)
result = classifier.predict(test_image)
training_set.class_indices
if result[0][0] == 1:
    prediction = 'AP'
    
elif result[0][1]==1:
    prediction = 'Bihar'
elif result[0][2]==1:
    prediction="MP"
print(prediction)


# In[10]:


import pickle


# In[11]:



file = 'cnn.pkl'
# Open the file to save as pkl file
cnn_pkl = open(file, 'wb')
pickle.dump(classifier, cnn_pkl)
# Close the pickle instances
cnn_pkl.close()


# In[12]:


cnn_pkl = open('cnn.pkl', 'rb')
cnn = pickle.load(cnn_pkl)
print("Loaded CNN :: ", cnn)


# In[13]:


#using the saved model
import numpy as np
import cv2
from keras.preprocessing import image
test_image = image.load_img('testfiles/mpbp.jpg', target_size = (128, 128))
test_image = image.img_to_array(test_image)
test_image = np.expand_dims(test_image, axis = 0)
result = cnn.predict(test_image)
# training_set.class_indices
if result[0][0] == 1:
    prediction = 'AP'
    
elif result[0][1]==1:
    prediction = 'Bihar'
elif result[0][2]==1:
    prediction="MP"
print(prediction)

