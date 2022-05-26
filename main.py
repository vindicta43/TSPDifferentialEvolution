import random

## five dataset parameters ##
# # Solution path
# filePath = "C:/Users/forei/Desktop/datasets/five/five_d.txt"
# Optimal path and fitness
# optimalSolution = [0, 2, 1, 4, 3]
# optimalSolutionFitness = 19

## dantzig42 dataset parameters ##
# # Solution path
# filePath = "C:/Users/forei/Desktop/datasets/dantzig42/dantzig42_d.txt"
# Optimal path and fitness
# optimalSolutionFitness = 699

## TODO: optimalSolution path 33551 çıkıyor
## att48 dataset parameters ##
# # Solution path
# filePath = "C:/Users/forei/Desktop/datasets/att48/att48_d.txt"
# # Optimal path and fitness
# optimalSolution = [0, 7, 37, 30, 43, 17, 6, 27, 5, 36, 18, 26, 16, 42, 29, 35, 45, 32, 19, 46, 20, 31, 38, 47, 4, 41,
#                    23, 9, 44, 34, 3, 25, 1, 28, 33, 40, 15, 21, 2, 22, 13, 24, 12, 10, 11, 14, 39, 8]
# optimalSolutionFitness = 33523

## gr17 dataset parameters ##
# Solution path
filePath = "C:/Users/forei/Desktop/datasets/gr17/gr17_d.txt"
# Optimal path and fitness
optimalSolution = [0, 3, 12, 6, 7, 5, 16, 13, 14, 2, 10, 9, 1, 4, 8, 11, 15]
optimalSolutionFitness = 2085


def createCandidateSolution(size):
    solutionBound = len(size)
    candidate = list(range(solutionBound))
    random.shuffle(candidate)
    return candidate


def evaulateFitness(singleLine):
    fitness = 0

    for index, item in enumerate(singleLine):
        fromCity = singleLine[index - 1]
        toCity = singleLine[index]
        fitness += int(distances[fromCity][toCity])
        print("from", fromCity, "to", toCity, "cost:", distances[fromCity][toCity])

    print("fitness for", singleLine, "==", fitness)
    if fitness <= optimalSolutionFitness:
        print("çözüme ulaşıldı:", singleLine, "fitness:", fitness)
    print("----------")


with open(filePath) as file:
    distances = file.readlines()
    for index, item in enumerate(distances):
        singleLine = item.split()
        distances[index] = singleLine

    print("distances:", distances)

    solutionArray = []
    solutionCount = int(input("Aday çözüm sayısı: "))
    for i in range(solutionCount):
        solutionArray.append(createCandidateSolution(distances[0]))

    # when solution have optimalSolution array, remove comment tag
    solutionArray.append(optimalSolution)
    print(solutionArray)

    for solution in solutionArray:
        evaulateFitness(solution)
