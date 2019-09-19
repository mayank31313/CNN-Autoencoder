# Background and Motivation

Live video and Image streaming requires good Internet speed, thus if we have a low connection speed it is not possible to stream properly. Altough I don't have much knowledge of Computer Vision. but I just tought if I can build a NN that can compress the image into latent space and then back reconstruct it to original form. But by doing this we also lose some information and image details depending on the latent dimension. So then I decided to implement it trough Keras.

# Architecture

The architecture for the encoder and decoder CNN is simple, and not much complex. Altough I have to make the CNN such that Raspberry PI 3 Model B+ can run it.


## Encoder Model
    _________________________________________________________________
    Layer (type)                 Output Shape              Param #   
    =================================================================
    input_18 (InputLayer)        (None, 360, 640, 3)       0         
    _________________________________________________________________
    conv2d_21 (Conv2D)           (None, 360, 640, 8)       224       
    _________________________________________________________________
    activation_43 (Activation)   (None, 360, 640, 8)       0         
    _________________________________________________________________
    average_pooling2d_17 (Averag (None, 180, 320, 8)       0         
    _________________________________________________________________
    conv2d_22 (Conv2D)           (None, 180, 320, 16)      1168      
    _________________________________________________________________
    activation_44 (Activation)   (None, 180, 320, 16)      0         
    _________________________________________________________________
    average_pooling2d_18 (Averag (None, 90, 160, 16)       0         
    _________________________________________________________________
    flatten_1 (Flatten)          (None, 230400)            0         
    =================================================================
    Total params: 1,392
    Trainable params: 1,392
    Non-trainable params: 0
    _________________________________________________________________
    
## Decoder Model
    _________________________________________________________________
    Layer (type)                 Output Shape              Param #   
    =================================================================
    input_19 (InputLayer)        (None, 230400)            0         
    _________________________________________________________________
    reshape_9 (Reshape)          (None, 90, 160, 16)       0         
    _________________________________________________________________
    conv2d_transpose_24 (Conv2DT (None, 180, 320, 16)      2320      
    _________________________________________________________________
    activation_45 (Activation)   (None, 180, 320, 16)      0         
    _________________________________________________________________
    conv2d_transpose_25 (Conv2DT (None, 360, 640, 16)      2320      
    _________________________________________________________________
    activation_46 (Activation)   (None, 360, 640, 16)      0         
    _________________________________________________________________
    conv2d_transpose_26 (Conv2DT (None, 720, 1280, 3)      435       
    _________________________________________________________________
    activation_47 (Activation)   (None, 720, 1280, 3)      0         
    =================================================================
    Total params: 5,075
    Trainable params: 5,075
    Non-trainable params: 0
    
    

# Samples

<div>
    <div style="width:50%">
        <h2>Original Image</h2>        
        <img src="restructured/original-1568820873.083995.jpg" />
    </div>
    <div style="width:50%">
        <h2>ReconstructedImage</h2>
        <img src="restructured/1568820873.083995.jpg" />
    </div>
</div>