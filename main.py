import os.path
import random
import tsplib95
from pathlib import Path
from datetime import datetime

## dantzig42 dataset parameters ##
# 712 hesaplanan - 699 website degeri
# tspPath = "datasets/dantzig42.tsp"
# optimalSolutionFitness = 699
# optimalSolution = [2, 1, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 21, 20, 19, 18, 15, 14, 13,
#                    16, 17, 22, 23, 12, 11, 24, 27, 26, 25, 10, 9, 8, 7, 6, 5, 4, 3]


## dj38 - Djibouti ##
# tspPath = "datasets/dj38.tsp"
# optimalSolutionFitness = 6656


## att48 - US State Capitals ##
# 10628 hesaplanan - 33523 website degeri
# tspPath = "datasets/att48.tsp"
# optimalSolutionFitness = 10628
# optimalSolution = [1, 8, 38, 31, 44, 18, 7, 28, 6, 37, 19, 27, 17, 43, 30, 36, 46, 33, 20, 47, 21, 32, 39, 48, 5, 42,
#                    24, 10, 45, 35, 4, 26, 2, 29, 34, 41, 16, 22, 3, 23, 14, 25, 13, 11, 12, 15, 40, 9]


## ar9152 - Argentina ##
# tspPath = "datasets/bays.tsp"
# optimalSolutionFitness = 837479


## ulysses - Odyssey of Ulysses ##
tspPath = "datasets/ulysses16.tsp"
optimalSolutionFitness = 6859
optimalSolution = [1, 14, 13, 12, 7, 6, 15, 5, 11, 9, 10, 16, 3, 2, 4, 8]


# Global variables
gen = 1
solutionArray = []


# Produce random candidate solution
def createCandidateSolution(size):
    candidate = list(range(1, size + 1))
    random.shuffle(candidate)
    return candidate


# Evaulate fitness for candidate solution
def evaluateFitness(solutions):
    global gen
    bestIndex = 0
    bestFitness = 0
    tempFitness = 0

    fitnessNum = 0
    for singleSolution in solutions:
        for index, singleFitness in enumerate(singleSolution):
            fromCity = singleSolution[index - 1]
            toCity = singleSolution[index]
            edges = fromCity, toCity
            weight = problem.get_weight(*edges)
            tempFitness += weight

        print("single solution =", singleSolution)
        print("fitness for solution", fitnessNum, "=", tempFitness)
        print("--------------------")
        fitnessNum += 1
        # Initializing for first iteration
        if bestFitness == 0:
            bestFitness = tempFitness

        if tempFitness < bestFitness:
            bestFitness = tempFitness
            bestIndex = solutions.index(singleSolution)

        tempFitness = 0

    print("best fitness for gen", gen, "=", bestFitness, "solution index =", bestIndex)

    if bestFitness <= optimalSolutionFitness:
        print("çözüme ulaşıldı gen = ", gen, "fitness:", bestFitness)
        return
    print("--------------------")
    gen += 1


# Get random indexes for mutation progress
def getRandomIndex(array):
    resultArray = []
    for randIndex in range(0, 3):
        rand = random.randint(0, len(array) - 1)
        print("rand =", rand)
        resultArray.append(array[rand])
        print("resultArray =", resultArray)
        del array[rand]

    return resultArray


# Differential Algorithm Function
def darwin(darwinArray):
    for singleDarwin in darwinArray:
        print("single darwin =", singleDarwin)
        print("random index darwin =", getRandomIndex(singleDarwin))
        print("-----")


# Program execution starts from here
with open(tspPath) as file:
    problem = tsplib95.read(file)
    solutionCount = int(input("Aday çözüm sayısı: "))
    for i in range(solutionCount):
        solutionArray.append(createCandidateSolution(int(problem.dimension)))

    # When solution have optimalSolution array, remove comment tag
    solutionArray.append(optimalSolution)

    darwin(solutionArray)
    # evaluateFitness(solutionArray)
