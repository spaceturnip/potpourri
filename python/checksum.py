import sys

def calculateTotal(num):
    total = 0

    num = [int(i) for i in list(num)] #split out each digit and make sure its an int
    num.reverse() # sorting places are always the same if you start from the end

    for index, val in enumerate(num):
        if index % 2 == 0:      # we want to double every odd digit
            print('doubling ' + str(val))
            val = val * 2 
            if val >= 10:
                val = val -9
        total = total + val
    return total

def calculateChecksum(num):
    num = calculateTotal(num)
    if num % 10 != 0:
        return 10 - (num % 10) # need to return 0 if its already devisable by 10
    else:
        return 0

def validateChecksum(num):
    
    checksum = int(num[-1])
    num = num[:-1]

    if (calculateTotal(num) + checksum) % 10:
        print("This is not a valid ID!!")
    else:
        print("checks out")

def printUsage(name):

    print('') # make the usage look pretty
    print(name + " - Validates or Calculates a Luhn checksum.\n")
    print(name + " <NUMBER>: Validate <NUMBER>")
    print(name + " -g <NUMBER> : Calculate checksum for <NUMBER>")

##Start main program
if len(sys.argv) <= 3:

    if (sys.argv[1] == "-g") and (sys.argv[2].strip().isdigit()):
        num = sys.argv[2].strip()
        print(num + str(calculateChecksum(num)))

    elif sys.argv[1].strip().isdigit():
        num = sys.argv[1].strip()
        validateChecksum(num)
    else:
        printUsage(sys.argv[0])

else:
    printUsage(sys.argv[0])

