from cnn import config # our config file 

from imutils import paths  # which you need to dowunload!

import random

import shutil

import os

# shuffle all the images in the original input directory
imagePaths = list(paths.list_images(config.orig_input_dataset))
random.seed(42)
random.shuffle(imagePaths)

# split the data into testing and training
i = int(len(imagePaths) * config.train_split)
trainPaths = imagePaths[:i]
testPaths =  imagePaths [i:]


#set aside some of the training data for the val data
i = int(len(trainPaths) * config.val_split)
valPaths = trainPaths[:i]
trainPaths = trainPaths[i:]

#define the trainig/validation/testing datasets
datasets = [
        ("training", trainPaths, config.train_path),
        ("validation", valPaths, config.val_path),
        ("testing", testPaths, config.test_path)

]



#loop over the datasets 
for (dType, imagePaths, baseOutput) in datasets:
    # show which data split we are creating
    print("[INFO] 'building {}' split".format(dType))
    
    # if the output directory does not exist, create it 
    if not os.path.exists(baseOutput):
        print("[INFO] 'creating {}' directory".format(baseOutput))
        os.makedirs(baseOutput)


    # build the path to the label directory
    for inputPath in imagePaths:
        # extract the filename of the input image and it's class label
        filename = inputPath.split(os.path.sep)[-1]
        label = inputPath.split(os.path.sep)[-2]

        # build  the path to the label directory
        labelPath = os.path.sep.join([baseOutput, label])

        # if the label path does not exist, create it
        if not os.path.exists(labelPath):
            print("[INFO] 'creating {}' directory".format(labelPath))
            os.makedirs(labelPath)



        # construct the path to the destination image and then copy the image itself
        p = os.path.sep.join([labelPath, filename])
        shutil.copy2(inputPath, p)
