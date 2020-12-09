import pandas as pd

f = open("Day_08/input.txt", "r")
inputs = f.read()

codes = [x for x in inputs.strip("\n").split("\n")]


def createCodes():
    cleanCodes = []
    for code in codes:
        splits = code.split(" ")
        command = splits[0]
        value = int(splits[1])
        dictCode = {"code": command, "value": value, "hasRun": 0}
        cleanCodes.append(dictCode)
    return cleanCodes


# PART 1 MATERIAL
def part_one():
    dictCodes = createCodes()

    stopInfLoop = 0
    lineRun = 0
    accVal = 0
    while stopInfLoop == 0:

        if dictCodes[lineRun]['hasRun'] == 1:
            stopInfLoop = 1
            break

        code = dictCodes[lineRun]['code']
        val = dictCodes[lineRun]['value']
        dictCodes[lineRun]['hasRun'] = 1

        if code == "nop":
            lineRun += 1
        elif code == "acc":
            accVal += val
            lineRun += 1
        elif code == "jmp":
            lineRun += val
    return accVal

# PART 2 MATERIAL


def part_two():
    dictCodes = createCodes()

    df = pd.DataFrame(dictCodes)

    nops = df[df['code'] == 'nop']
    jmps = df[df['code'] == 'jmp']
    nopsLines = list(nops.index)
    jmpsLines = list(jmps.index)
    checkLines = jmpsLines.extend(nopsLines)

    def resetHasRun(codes):
        for code in codes:
            code['hasRun'] = 0

    dictCodes = createCodes()
    foundFix = 0
    for checkLine in jmpsLines:
        if foundFix == 1:
            break

        dictCodes[checkLine]['code'] = 'nop'
        stopInfLoop = 0
        lineRun = 0
        accVal = 0

        while stopInfLoop == 0 and foundFix == 0:
            if dictCodes[lineRun]['hasRun'] == 1:
                stopInfLoop = 1
                dictCodes[checkLine]['code'] = 'jmp'
                break

            code = dictCodes[lineRun]['code']
            val = dictCodes[lineRun]['value']
            dictCodes[lineRun]['hasRun'] = 1

            if code == "nop":
                lineRun += 1
            elif code == "acc":
                accVal += val
                lineRun += 1
            elif code == "jmp":
                lineRun += val
            if lineRun == len(codes):
                foundFix = 1
                return accVal
        resetHasRun(dictCodes)


print("What value is in the accumulator? (Part 1):", part_one())
print("What is the value of the accumulator after the program terminates? (Part 2):", part_two())
