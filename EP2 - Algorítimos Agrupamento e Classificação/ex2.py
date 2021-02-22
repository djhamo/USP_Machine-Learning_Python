# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 18:24:18 2019

@author: Tiago

Accuracy: 84.66666666666667%
83.86666666666666
"""

# Example of kNN implemented from Scratch in Python

import csv
import math
import operator

def loadDataset(filename, split, pad):
    if not (0<=pad<10) and type(pad)!='int':
        raise ValueError('pad must be int between 0 and 9')
    with open(filename, 'r') as csvfile:

        lines = csv.reader(csvfile)
        header = next(lines)
        dataset = list(lines)
        trainSize = int(split*len(dataset))
        foldsize = int(len(dataset)/10)

        trainset = dataset[:pad*foldsize] + dataset[(pad+1)*foldsize:]
        testset = dataset[pad*foldsize:(pad+1)*foldsize]
        print(len(trainset))
        print(len(testset))
        return [trainset, testset]

def euclideanDistance(instance1, instance2, length):
    distance = 0
    for x in range(length):
        distance += pow(float(instance1[x]) - float(instance2[x]), 2)
    return math.sqrt(distance)

def getNeighbors(trainingSet, testInstance, k):
    distances = []
    length = len(testInstance)-1
    for x in range(len(trainingSet)):
        dist = euclideanDistance(testInstance, trainingSet[x], length)
        distances.append((trainingSet[x], dist))
    distances.sort(key=operator.itemgetter(1))
    neighbors = []
    for x in range(k):
        neighbors.append(distances[x][0])
    return neighbors

def getResponse(neighbors):
    classVotes = {}
    for x in range(len(neighbors)):
        response = neighbors[x][-1]
        if response in classVotes:
            classVotes[response] += 1
        else:
            classVotes[response] = 1
    sortedVotes = sorted(classVotes.items(), key=operator.itemgetter(1), reverse=True)
    return sortedVotes[0][0]

def getAccuracy(testSet, predictions):
    correct = 0
    for x in range(len(testSet)):
        if testSet[x][-1] == predictions[x]:
            correct += 1
    return (correct/float(len(testSet))) * 100.0

def main():
    # prepare data
    split = 0.90
    k = 10
    nfold =10
    total_accuracy = 0
    
    for i in range(nfold):

        trainingSet, testSet = loadDataset('class02.csv', split,pad=i)
        # generate predictions
        predictions=[]

        for x in range(len(testSet)):
            neighbors = getNeighbors(trainingSet, testSet[x], k)
            result = getResponse(neighbors)
            predictions.append(result)

        accuracy = getAccuracy(testSet, predictions)
        print('Accuracy: ' + repr(accuracy) + '%')
        total_accuracy += accuracy/nfold
    print(total_accuracy)


main()
