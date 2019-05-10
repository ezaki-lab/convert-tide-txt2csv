import os


def observeToBase(tide, location='TB'):
    fmTide = tide + formatList[location]['observe']
    return round(fmTide)

def baseToObserve(tide, location='TB'):
    fmTide = tide - formatList[location]['observe']
    return round(fmTide)


def calculateToBase(tide, location='TB'):
    fmTide = tide + formatList[location]['calculate']
    return round(fmTide)


def baseToCalculate(tide, location='TB'):
    fmTide = tide - formatList[location]['calculate']
    return round(fmTide)


formatList = {
    'TB':{
        'observe':-281.7,
        'calculate':-119.8
    }
}