import numpy as np
from keras.models import load_model
import cv2, time

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

encoded_imgs = encoder_model.predict(x_test)
MAX = np.max(encoded_imgs)

encoded_imgs = (encoded_imgs/MAX) * 255
encoded_imgs  = encoded_imgs.astype('uint8')

inter_encoded_imgs = encoded_imgs * MAX / 255
decoded_imgs = decoder_model.predict(inter_encoded_imgs)

cv2.imshow("Reconstructed", (decoded_imgs/np.max(decoded_imgs))[0]) 
cv2.imshow("Original", x_test[0]) 

name = str(time.time())

cv2.imwrite("./images/%s.jpg" %name,decoded_imgs[0])
cv2.imwrite("./images/original-%s.jpg" %name,x_test[0])

cv2.waitKey(0)
cv2.destroyAllWindows()