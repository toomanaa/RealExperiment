import os
import psutil
import platform
import time
from datetime import datetime
import threading
from imageai.Prediction import ImagePrediction
import struct
from statistics import mean

processingTime = []

for number in range(10):
    print("================================")
    print(number)
    start_time = time.time()
    prediction = ImagePrediction()
    prediction.setModelTypeAsResNet()
    prediction.setModelPath("resnet50_weights_tf_dim_ordering_tf_kernels.h5")
    prediction.loadModel()

    predictions, percentage_probabilities = prediction.predictImage("sheep.jpeg", result_count=5)
    results = []
    for index in range(len(predictions)):
        #print(predictions[index] , " : " , percentage_probabilities[index])
        results.append(predictions[index])
        results.append(percentage_probabilities[index])

    results = str(results)
    print(results)
    print("--- %s seconds ---" % (time.time() - start_time))
    processingTime.append(time.time() - start_time)


print(mean(processingTime))