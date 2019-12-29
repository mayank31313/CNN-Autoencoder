import numpy as np
from keras.models import load_model
import cv2, time

in_height = 720//2
in_width =  1280//2

out_height = in_height
out_width = in_width


def getImage(file):
    frame = cv2.imread(file,1)
    return [np.array([cv2.resize(frame,(in_width,in_height))]),np.array([cv2.resize(frame,(out_width,out_height))])]

encoder_model = load_model("32C-360x640-encoder.h5")
decoder_model = load_model("32C-360x640-decoder.h5")

encoder_model.summary()
decoder_model.summary()

#x_test = getImage('C:/Users/mayan/Desktop/tensorflow-autoencoder/static/2-dog.jpg')[0]

def run_model(image):
    image = cv2.resize(image,(in_width,in_height))
    image = np.expand_dims(image,axis=0)
    encoded_imgs = encoder_model.predict(image)
    MAX = np.max(encoded_imgs)

    encoded_imgs = (encoded_imgs/MAX) * 255
    encoded_imgs  = encoded_imgs.astype('uint8')

    inter_encoded_imgs = encoded_imgs * MAX / 255
    decoded_imgs = decoder_model.predict(inter_encoded_imgs)
    return decoded_imgs/np.max(decoded_imgs)


cap = cv2.VideoCapture(0)
start = time.time()
while(True):
    ret, frame = cap.read()
    if ret:
        frame = run_model(frame)[0]
        end = time.time()
        fps = 1//(end - start)
        
        cv2.putText(frame,str(fps),(10,30),cv2.FONT_HERSHEY_SIMPLEX, 1, (209, 80, 0, 255),1) 

        cv2.imshow('frame',frame)
        start = end
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()