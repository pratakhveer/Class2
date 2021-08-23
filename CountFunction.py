def countWordFromFile():
    fileName = input("Enter the file name")
    numberCount = 0
    file = open(fileName, "r")
    for line in file:
        word = line.split()
        numberCount = numberCount+len(word)
    print(numberCount)


countWordFromFile()
