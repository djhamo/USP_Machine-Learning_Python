# -*- coding: utf-8 -*-
"""
Spyder Editor

Naive Bayes Gaussiano + metodologia holdout.
Resultado:
-- Naive Bayes + Holdout --
Dividindo 1000 linhas em treino=350 and teste=650 rows
Holdout - Acuracia do train set: 76.0%
Holdout - Acuracia do test set: 62.30769230769231%
-- Leave One Out --
Leave one out - Acuracia no Treino: 68.92782782782756%
Leave one out - Acuracia no Teste: 64.30000000000062%
"""
import csv
import random
import math

def loadCsv(filename):
    lines = csv.reader(open(filename, "r"))
    #tirar o cabecalho
    header = next(lines, None)
    dataset = list(lines)
    #passar tudo pra float
    for i in range(len(dataset)):
        dataset[i] = [float(x) for x in dataset[i]]

    return dataset

def divDataset(dataset, splitRatio):
    trainSize = int(len(dataset) * splitRatio)
    copy = list(dataset)

    return [copy[:trainSize], copy[trainSize:]]

def separateByClass(dataset):
    separated = {}
    for i in range(len(dataset)):
        vector = dataset[i]
        if (vector[-1] not in separated):
            separated[vector[-1]] = []
        separated[vector[-1]].append(vector)
    return separated


def media(numbers):
    return float(sum(numbers))/float(len(numbers))


def variancia(numbers):
    avg = media(numbers)
    variancia = sum([pow(x-avg, 2) for x in numbers])/float(len(numbers)-1)
    return math.sqrt(variancia)

def summarize(dataset):
    summaries = [(media(attribute), variancia(attribute))
                  for attribute in zip(*dataset)]
    del summaries[-1]
    return summaries

def summarizeByClass(dataset):
    separated = separateByClass(dataset)
    summaries = {}
    for classValue, instances in separated.items():
        summaries[classValue] = summarize(instances)
    return summaries

def calcGaussiana(x, mean, stdev):
    exponent = math.exp(-(math.pow(x-mean, 2)/(2*math.pow(stdev, 2))))
    return (1 / (math.sqrt(2*math.pi) * stdev)) * exponent

def calcProbPorClass(summaries, inputVector):
    prob = {}

    for classValue, classSummaries in summaries.items():
        prob[classValue] = 1
        for i in range(len(classSummaries)):
            media, var = classSummaries[i]
            x = inputVector[i]
            prob[classValue] *= calcGaussiana(x, media, var)
    return prob


def predict(summaries, inputVector):
    probs = calcProbPorClass(summaries, inputVector)
    bestLabel = None
    bestProb = -1

    for (classValue, probability) in probs.items():
        if bestLabel is None or probability > bestProb:
            bestProb = probability
            bestLabel = classValue
    return bestLabel


def getPredictions(summaries, testSet):
    predictions = []
    for i in range(len(testSet)):
        result = predict(summaries, testSet[i])
        predictions.append(result)
    return predictions

def getAccuracy(testSet, predictions):
    correct = 0

    for i in range(len(testSet)):

        if testSet[i][-1] == predictions[i]:
            correct += 1
            #print(testSet[i])
            #print(testSet[i][-1])
            #print(predictions[i])
    return (correct/float(len(testSet))) * 100.0

def main():
    print('-- Naive Bayes + Holdout --')
    #Carregando a Base
    dataset = loadCsv('class01.csv')
    #print(dataset[1][1])
    
    #dividindo a Base
    treinoSet, testSet = divDataset(dataset, 0.35)
    print(('Dividindo {0} linhas em treino={1} and teste={2} rows').format(
        len(dataset), len(treinoSet), len(testSet)))
    
    # modelo
    summaries = summarizeByClass(treinoSet)  
    #print(summaries[0][1][1])
    
    # resultados no treinoset
    trainset_predictions = getPredictions(summaries, treinoSet)
    trainset_accuracy = getAccuracy(treinoSet, trainset_predictions)
    print(('Holdout - Acuracia do train set: {0}%').format(trainset_accuracy))
    
    # resultados no teste
    testset_predictions = getPredictions(summaries, testSet)
    testset_accuracy = getAccuracy(testSet, testset_predictions)
    print(('Holdout - Acuracia do test set: {0}%').format(testset_accuracy))    


main()
