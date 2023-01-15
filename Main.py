import random
import sys
import Create as Create
import Model as Model
import Process as Process
import pandas as pd

def Task1():
    createDelay = 2
    processDelay = 1
    maxQueue = 5
    simulateTime = 1000

    SimModel(createDelay, processDelay, simulateTime, maxQueue)


def Task3():
    createDelay = 2
    process1Delay = 1
    process2Delay = 1
    process3Delay = 1
    delay = [createDelay, process1Delay, process2Delay, process3Delay]

    process1MaxQueue = 5
    process2MaxQueue = 5
    process3MaxQueue = 5
    maxQueue = [process1MaxQueue, process2MaxQueue, process3MaxQueue]

    simulateTime = 1000

    SimModelFor3Processes(delay, simulateTime, maxQueue)


    

def Task4():
    inputData = pd.read_excel('InputData.xlsx')
    df = pd.DataFrame()
    rows = []

    for i in range(len(inputData)):
        row = simMidelForTask4(inputData, i)
        rows.append({**row})
 
    df = pd.DataFrame(rows)
    df.to_excel('OutputData.xlsx')


def simMidelForTask4(inputData, i):
    simulateTime = inputData['simulateTime'][i]

    c = Create.Create(inputData['delayCreate'][i])
    p1 = Process.Process(inputData['delayProcess1'][i])
    p2 = Process.Process(inputData['delayProcess2'][i])
    p3 = Process.Process(inputData['delayProcess3'][i])

    c.name = 'Creator'
    p1.name = 'Process1'
    p2.name = 'Process2'
    p3.name = 'Process3'

    c.distribution = inputData['distribution'][i]
    p1.distribution = inputData['distribution'][i]
    p2.distribution = inputData['distribution'][i]
    p3.distribution = inputData['distribution'][i]

    p1.maxQueue = inputData['maxQueue1'][i]
    p2.maxQueue = inputData['maxQueue2'][i]
    p3.maxQueue = inputData['maxQueue3'][i]

    c.nextElement = [p1]
    p1.nextElement = [p2]
    p2.nextElement = [p3]

    modelList = [c, p1, p2, p3]
    model = Model.Model(modelList)
    model.simulate(simulateTime)

    row = makeStatisticRow(modelList, inputData, i)
    return row

def makeStatisticRow(modelList, inputData, i):
    row = {'delayCreate': inputData['delayCreate'][i],
                 'delayProcess1': inputData['delayProcess1'][i],
                 'delayProcess2': inputData['delayProcess2'][i],
                 'delayProcess3': inputData['delayProcess3'][i],
                 'maxQueue1': inputData['maxQueue1'][i],
                 'maxQueue2': inputData['maxQueue2'][i],
                 'maxQueue3': inputData['maxQueue3'][i],
                 'distribution': inputData['distribution'][i],
                 'quantity1': modelList[1].quantity,
                 'meanQueueLength1' : modelList[1].meanQueueLength,
                 'failed1': modelList[1].failure,
                 'failureProbability1': modelList[1].failureProbability, 
                 'averageLoad1' : modelList[1].averageLoad, 
                 'quantity2': modelList[2].quantity,
                 'failed2': modelList[2].failure,
                 'meanQueueLength2' : modelList[2].meanQueueLength,
                 'failureProbability2': modelList[2].failureProbability, 
                 'averageLoad2' : modelList[2].averageLoad, 
                 'quantity3': modelList[3].quantity,
                 'failed3': modelList[3].failure,
                 'meanQueueLength3' : modelList[3].meanQueueLength,
                 'failureProbability3': modelList[3].failureProbability, 
                 'averageLoad3' : modelList[3].averageLoad, 
                 }
    return row



def Task5():
    createDelay = 2
    processDelay = 5
    maxQueue = 5
    numOfChanel = 1

    simulateTime = 1000

    c = Create.Create(createDelay)
    p = Process.Process(processDelay, numOfChanel)

    c.name = 'Creator'
    p.name = 'Processor'

    c.distribution = 'exp'
    p.distribution = 'exp'

    p.maxQueue = maxQueue
    c.nextElement = [p]

    model = Model.Model([c, p])
    model.simulate(simulateTime)

def Task6():

    createDelay = 2
    process1Delay = 1
    process2Delay = 1
    process3Delay = 1
    delay = [createDelay, process1Delay, process2Delay, process3Delay]

    maxQueue1 = 5
    maxQueue2 = 5
    maxQueue3 = 5
    maxQueue = [maxQueue1, maxQueue2, maxQueue3]

    simulateTime = 1000

    SimModelFor3Processes(delay, simulateTime, maxQueue)


def SimModel(createDelay, processDelay, simulateTime, maxQueue):
    c = Create.Create(createDelay)
    p = Process.Process(processDelay)

    p.maxQueue = maxQueue
    c.distribution = 'exp'
    p.distribution = 'exp'
    c.name = 'Creator'
    p.name = 'Processor'
    c.nextElement = [p]
    modelList = [c, p]

    model = Model.Model(modelList)
    model.simulate(simulateTime)


def SimModelFor3Processes(delay, simulateTime, maxQueue):

    c = Create.Create(delay[0])
    p1 = Process.Process(delay[1])
    p2 = Process.Process(delay[2])
    p3 = Process.Process(delay[3])

    c.name = 'Creator'
    p1.name = 'Processor1'
    p2.name = 'Processor2'
    p3.name = 'Processor3'

    c.distribution = 'exp'
    p1.distribution = 'exp'
    p2.distribution = 'exp'
    p3.distribution = 'exp'

    p1.maxQueue = maxQueue[0]
    p2.maxQueue = maxQueue[1]
    p3.maxQueue = maxQueue[2]

    c.nextElement = [p1]
    p1.nextElement = [p2, p3]

    modelList = [c, p1, p2, p3]

    model = Model.Model(modelList)
    model.simulate(simulateTime)

def main():
    # Task1()
    # Task3()
    # Task4()
    # Task5()
    Task6()

main()


