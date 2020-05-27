import json
from itertools import groupby

def convertToJson(inputFileName, outputFileName):

    input = open(inputFileName, "r")
    output = open(outputFileName, "w")


    with input as f:
        while True:
            line = next(f,'')
            if not line:
                break
            if not line.startswith(';'):
                if line.startswith('Host'):
                    chunk = line.split(',')
                    network = chunk[1]
                if line.startswith(','):
                    data=[]
                    chunk = line.split(',')
                    if any("INA" in s for s in chunk):
                        matching = [s for s in chunk if "INA" in s]
                        ina = (matching[0].replace('INA:', ''))
                    else:
                        ina = "null"
                    if any("IBN" in s for s in chunk):
                        matching = [s for s in chunk if "IBN" in s]
                        ibnCheck = (matching[0].replace('IBN:', ''))
                    
                        if ibnCheck !="IBN":
                            ibn = ibnCheck
                        else:
                            ibn = "null"
                    else:
                        ibn = "null"
                    if any("ITN" in s for s in chunk):
                        matching = [s for s in chunk if "ITN" in s]
                        itn = (matching[0].replace('ITN:', ''))
                    else:
                        itn = "null"
                    data.append(
                        {
                        "zone" : "21",
                        "network" : network,
                        "node" : chunk[1],
                        "nodeName": (chunk[2]).replace("_", " "),
                        "location": (chunk[3]).replace("_", " "),
                        "sysopName": (chunk[4]).replace("_", " "),
                        "INA": (ina).replace('\n',''),
                        "IBN": (ibn).replace('\n',''),
                        "ITN": (itn).replace('\n','')
                        # "phoneNumber": chunk[5],
                        # "dceSpeed": chunk[6],
                        # "CM": chunk[11],
                        # "ICM": chunk[12],
                        # "MO": chunk[13],
                        # "LO": chunk[14],
                        # "MN": chunk[15],
                        # "mailFlag": chunk[19]
                        }
                        )  
                    data = data
                    output.write(json.dumps(data[0], sort_keys=False, ensure_ascii=True, indent=4))
    
    input.close
    output.close
     

convertToJson("FSXNET.150", "fsxnet.json")