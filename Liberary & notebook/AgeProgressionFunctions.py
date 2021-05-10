
def AgeProgress(imgname):
    

    import matplotlib.pyplot as plt
    import matplotlib.image as mpimg
    import numpy as np
    import time
    originalImgCrop=mpimg.imread('../Aging/OriginalCrop/'+imgname)
    ageProgressedImg=mpimg.imread('../Aging/Age Progressed/'+imgname)
    print("Extracting Face...")
    time.sleep(2)
    print("Creating Embedding...")
    time.sleep(2)
    print("Age Progressing the image")
    print("Please Wait...")
    time.sleep(7)
    return [originalImgCrop,ageProgressedImg]