import os
import psutil
import platform
import time
from datetime import datetime
import threading
from imageai.Prediction import ImagePrediction
import struct
from statistics import mean

for number in range(10):
    print("================================")
    print(number)
    averageServerUtilization1 = psutil.cpu_percent(5)
    print(averageServerUtilization1)
    time.sleep(2)
    averageServerUtilization2 = psutil.cpu_percent(5)
    print(averageServerUtilization2)
    time.sleep(2)

    processingTime = []
    baseLine = min(averageServerUtilization1,averageServerUtilization2)

    if(psutil.cpu_percent(5)<= baseLine):
        print("we want with the first option")
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
    elif (psutil.cpu_percent(5)<= baseLine):
        print("we want with the second option")
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
    else:
        print("we want with the last option")
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

