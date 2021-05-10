from numpy import expand_dims
from numpy import asarray
def get_embedding(model, face_pixels):

    face_pixels= face_pixels.astype('float32')
    mean, std= face_pixels.mean(), face_pixels.std()
    face_pixels= (face_pixels - mean)/std
    samples=expand_dims(face_pixels, axis=0)
    yhat=model.predict(samples)
    yhat=asarray(yhat[0])
    yhat=yhat.reshape(1,-1)

    return yhat
                  
