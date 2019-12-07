import numpy as np
from keras.models import load_model
import cv2

in_height = 720//2
in_width =  1280//2

out_height = in_height
out_width = in_width


def getImage(file):
    #‪C:\Users\mayan\Downloads\2-dog.jpg
    frame = cv2.imread(file,1)
    return [np.array([cv2.resize(frame,(in_width,in_height))]),np.array([cv2.resize(frame,(out_width,out_height))])]

encoder_model = load_model("encoder-final-model.h5")
decoder_model = load_model("decoder-final-model.h5")

encoder_model.summary()
decoder_model.summary()

x_test = getImage('C:/Users/mayan/Desktop/tensorflow-autoencoder/static/2-dog.jpg')[0]

decoded_imgs = encoder_model.predict(x_test)

decoded_imgs = decoded_imgs/np.max(decoded_imgs) * 255
decoded_imgs  = decoded_imgs.astype('uint8')

decoded_imgs = decoder_model.predict(decoded_imgs)
decoded_imgs = decoded_imgs/np.max(decoded_imgs)


cv2.imshow("Reconstructed", decoded_imgs[0]) 
cv2.imshow("Original", x_test[0]) 

cv2.waitKey(0)
cv2.destroyAllWindows()