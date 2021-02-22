

# Example of Naive Bayes implemented from Scratch in Python
import csv
import random
import math


def loadCsv(filename):
    lines = csv.reader(open(filename, "r"))
    header = next(lines, None)
    dataset = list(lines)
    for i in range(len(dataset)):
        dataset[i] = [float(x) for x in dataset[i]]

    return dataset


def splitDataset(dataset, splitRatio):
    trainSize = int(len(dataset) * splitRatio)
    trainSet = []
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


def mean(numbers):
    return float(sum(numbers))/float(len(numbers))


def stdev(numbers):
    avg = mean(numbers)
    variance = sum([pow(x-avg, 2) for x in numbers])/float(len(numbers)-1)
    return math.sqrt(variance)


def summarize(dataset):
    summaries = [(mean(attribute), stdev(attribute))
                  for attribute in zip(*dataset)]
    del summaries[-1]
    return summaries


def summarizeByClass(dataset):
    separated = separateByClass(dataset)
    summaries = {}
    for classValue, instances in separated.items():
        summaries[classValue] = summarize(instances)
    return summaries


def calculateProbability(x, mean, stdev):
    exponent = math.exp(-(math.pow(x-mean, 2)/(2*math.pow(stdev, 2))))
    return (1 / (math.sqrt(2*math.pi) * stdev)) * exponent


def calculateClassProbabilities(summaries, inputVector):
    probabilities = {}

    for classValue, classSummaries in summaries.items():
        probabilities[classValue] = 1
        for i in range(len(classSummaries)):
            mean, stdev = classSummaries[i]
            x = inputVector[i]
            probabilities[classValue] *= calculateProbability(x, mean, stdev)
    return probabilities


def predict(summaries, inputVector):
    probabilities = calculateClassProbabilities(summaries, inputVector)
    bestLabel = None
    bestProb = -1

    for (classValue, probability) in probabilities.items():
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
    print('-- Holdout --')
    filename = 'class01.csv'
    splitRatio = 0.35
    dataset = loadCsv(filename)
    trainingSet, testSet = splitDataset(dataset, splitRatio)
    print(('Split {0} rows into train={1} and test={2} rows').format(
        len(dataset), len(trainingSet), len(testSet)))
    # prepare model
    summaries = summarizeByClass(trainingSet)

    # results on train set
    trainset_predictions = getPredictions(summaries, trainingSet)
    trainset_accuracy = getAccuracy(trainingSet, trainset_predictions)
    print(('Holdout - Accuracy on train set: {0}%').format(trainset_accuracy))
    # test model
    testset_predictions = getPredictions(summaries, testSet)
    testset_accuracy = getAccuracy(testSet, testset_predictions)
    print(('Holdout - Accuracy on test set: {0}%').format(testset_accuracy))

    # Leave one out estimation

    print('-- Leave One Out --')
    lootrainset_accuracy=0
    lootestset_accuracy=0
    for i in range(len(dataset)):
        loo = dataset[i]
        trainingSet = dataset[:i]+dataset[i+1:]
        summaries = summarizeByClass(trainingSet)

        lootestset_accuracy += getAccuracy([loo,], getPredictions(summaries, [loo,])) /len(dataset)
        lootrainset_accuracy += getAccuracy(trainingSet, getPredictions(summaries, trainingSet)) /len(dataset)
    print(('Leave one out - Accuracy on train set: {0}%').format(lootrainset_accuracy))
    print(('Leave one out - Accuracy on test set: {0}%').format(lootestset_accuracy))



main()
