from itertools import groupby
import json
import re
names = ["name", "description","info","author", "year"]

def removeComments(inputFileName, outputFileName):
    input = open(inputFileName, "r")
    output = open(outputFileName, "w")

    output.write(input.readline())

    with input as x:
        for line in x:
            if not line.lstrip().startswith(";") or line.lstrip().startswith('Host'):
                out = re.sub(r'^\s*(,\s*)', '', line)
                output.write(out)
    input.close()


def removeFirstLine(inputFileName, outputFileName):
    input = open(inputFileName, "r")
    output = open(outputFileName, "w")

    with input as fin:
        data = fin.read().splitlines(True)

    with output as fout:
        fout.writelines(data[1:])


def convertToJson(inputFileName, outputFileName):
    input = open(inputFileName, "r")
    output = open(outputFileName, "w")

    with input as f, output as out:
        grouped = groupby(map(str.rstrip,f), key=lambda x: x.startswith(' '))
        for k,v in grouped:
            if not k:
                json.dump(dict(zip(names,v)),out)
                out.write("\n")

removeComments("FSXNET.143", "fsxnetStripped.txt")
removeFirstLine("fsxnetStripped.txt", "fsxnetStrippedFirst.txt")
convertToJson("fsxnetStrippedFirst.txt", "fsxnet.json")
