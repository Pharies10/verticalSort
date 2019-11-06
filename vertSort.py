# Vertical Sort
#
#
# By Jack Pharies and Rob Ranseen
import random
import math

#global variables
data = []
compCounter = 0
r = 0
s = 0



# writes into data.txt
# allows you to customize the matrix to your prefered setting
def createFile():
    #dataFile = open("data.txt", "w")
    print("Follow the prompts to create a randomly generated file in data.txt")
    print("rows(r) and Cols(s) must follow the rules r < 2*((s-1)*(s-1)) and r % s != 0")
    rows = int(input("Enter numbers of Rows: "))
    cols = int(input("Enter numbers of Cols: "))
    while rows < 2*((cols-1)*(cols-1)) or rows % cols != 0:
        rows = int(input("Enter numbers of Rows: "))
        cols = int(input("Enter numbers of Cols: "))

    row = rows
    col = cols
    
    dataFile = open("data.txt", "w")
    dataFile.write(str(rows)+"\n")
    dataFile.write(str(cols) + "\n")

    for rw in range(row):
        line = ""
        for cl in range(col):
 
            x = random.randint(0, row*col*2)
            item = str(x)
            line = line + item + " "
        line = line + "\n"
        dataFile.write(line)
 
    dataFile.close()
    


    

#creates the list from a given file where the first line is the number of rows and the second line is the number of colums followed by the data
def getDataFromFile():
    global data
    global r
    global s
    data = []
    dataFile = open("data.txt", "r")

    r = int(dataFile.readline().rstrip())

    s = int(dataFile.readline().rstrip())

    if r < 2*((s-1)*(s-1)) or r % s != 0:
        print("this is invalid data")
        return

    count = 0

    while count < r:
        intRow = []

        strRow = dataFile.readline().rstrip().split(" ")

        for items in strRow:
            intItem = int(items)
            intRow.append(intItem)
        data.append(intRow)
        
        count = count + 1

    dataFile.close()


#prints contents of data as list of lists
def printData():
    global data
    for i in range(len(data)):
        print(data[i])
    



# transpose the sorted array
def transpose(sortedData):
    global data
    
    newData = []
    for col in range(s):
        newRow = []
        for row in range(r):
            newRow.append(sortedData[col][row])
            if (row+1) % s == 0:
     
                newData.append(newRow)
                newRow = []
    data = newData

        

    
# untransponse the sorted array
def untranspose(sortedData):
    global data
    
    newData = []

    newCol = []
    count = 1
    for row in range(r):
        for col in range(s):
            newCol.append(sortedData[col][row])           
            if (col + 1) % s == 0 and count >= r:               
                newData.append(newCol)
                newCol = []
                count = 0
            count = count+1
    newestData = []

    for row in range(r):
        newCol = []
        for col in range(s):
            newCol.append(newData[col][row])
            if (col + 1) % s == 0:
                newestData.append(newCol)
                newCol = []

    data = newestData
        
        
        

  
    
# shifts and unshifts the sorted array.
# calls a sort within this function
def shift(sortedData):
    global data

    key = r//2

    negInf = float("-inf")
    posInf = float("inf")
    
    shiftArray = []

    newRow = []
    count = 0
    while count < key:
        newRow.append(negInf)
        count = count + 1
        
    for col in range(s):
        for row in range(r):
            newRow.append(sortedData[col][row])
            if len(newRow) == r:
                shiftArray.append(newRow)
                newRow =[]

    while count < r:
        newRow.append(posInf)
        count = count + 1
        
    shiftArray.append(newRow)
  
    return shiftArray
  

 

# unshifts the array and makes the final array
def unshift(shiftSortArray):
    global data

    negInf = float("-inf")
    posInf = float("inf")
    unshiftArray = []
    newRow = []
    for col in range(s+1):
        for row in range(r):
            if shiftSortArray[col][row] != posInf and shiftSortArray[col][row] != negInf: 
                newRow.append(shiftSortArray[col][row])
                if len(newRow) == r:
                    unshiftArray.append(newRow)
                    newRow =[]

    finalArray = []
    newCol = []
    for row in range(r):
        for col in range(s):
            newCol.append(unshiftArray[col][row])
            if len(newCol) == s:
                finalArray.append(newCol)
                newCol = []
   

    data = finalArray
            























#sorts

#mergeSort
# puts the items in colum lists - taken from the book "The Design and Analysis of Algorithms" by Anany Leviton
def callMerge():

    sortArray = []
    for col in range(s):
        colList = []
        for row in range(r):
            colList.append(data[row][col])
        sortArray.append(colList)

    sortedData = []
    for item in sortArray:
        col = mergeSort(item)
        sortedData.append(col)
    return(sortedData)
        

def mergeSort(column):
    if len(column) > 1:
       
        firstHalf = []
        backHalf = []
        
        for i in range(0, len(column)//2):
            firstHalf.append(column[i])
    
        for i in range(len(column)//2,  len(column)):
            backHalf.append(column[i])

        B = mergeSort(firstHalf)
        C = mergeSort(backHalf)

        column = merge(B, C)
        
    return column

# merge two lists together
def merge(B, C):
    global compCounter
    A = []
  
    lenB = len(B)
  
    lenC = len(C)
    b = 0
    c = 0
    
    while b < lenB and c < lenC:
        compCounter = compCounter+1
        if B[b] <= C[c]:
            A.append(B[b])
            b = b + 1
        else:
            A.append(C[c])
            c = c + 1
    if b == lenB:
        for j in range(c, lenC):
            A.append(C[j])
    else:
        for i in range(b, lenB):
            A.append(B[i])
 
    return A





#bubbleSort - taken from the book "The Design and Analysis of Algorithms" by Anany Leviton
def callBubble():
    sortArray = []
    for col in range(s):
        colList = []
        for row in range(r):
            colList.append(data[row][col])
        sortArray.append(colList)

    sortedData = []
    for item in sortArray:
        col = bubbleSort(item)
        sortedData.append(col)
    return(sortedData)



def bubbleSort(unsortedArray):
    global compCounter
    
    for i in range(0, (len(unsortedArray)-1)):
        for j in range(0, (len(unsortedArray)-1) - i):
            if unsortedArray[j+1] < unsortedArray[j]:
                swapped = unsortedArray[j]
                unsortedArray[j] = unsortedArray[j+1]
                unsortedArray[j+1] = swapped
            compCounter = compCounter + 1
    
    return unsortedArray




#insertionSort - taken from the book "The Design and Analysis of Algorithms" by Anany Leviton
def callInsertion():
    sortArray = []
    for col in range(s):
        colList = []
        for row in range(r):
            colList.append(data[row][col])
        sortArray.append(colList)
    
    sortedData = []
    for item in sortArray:
        col = insertionSort(item)
        sortedData.append(col)
    
    return(sortedData)

def insertionSort(unsortedArray):
    global compCounter
    for i in range(1,len(unsortedArray)):
        value = unsortedArray[i]
        j = i-1
        while j >= 0 and unsortedArray[j] > value:
            compCounter = compCounter + 1
           
            unsortedArray[j+1] = unsortedArray[j]
            j = j-1
            
        unsortedArray[j+1] = value
    
    return unsortedArray

















# tests
# we have constructed a function for each type of sort we want to run

# all mergeSorts
def allMerge():
    getDataFromFile()

    sortedData = callMerge()

    transpose(sortedData)

    sortedData = callMerge()

    untranspose(sortedData)

    sortedData = callMerge()

    shiftArray = shift(sortedData)
    shiftSortArray = []

    for item in shiftArray:
        col = mergeSort(item)
        shiftSortArray.append(col)
     
    unshift(shiftSortArray)
    
 #   printData()
    print("number of comparisons for all mergeSorts:", compCounter, "\n")

# all bubbleSorts
def allBubble():
    getDataFromFile()
    sortedData = callBubble()

    transpose(sortedData)

    sortedData = callBubble()

    untranspose(sortedData)

    sortedData = callBubble()

    shiftArray = shift(sortedData)
    shiftSortArray = []

    for item in shiftArray:
        col = bubbleSort(item)
        shiftSortArray.append(col)
     
    unshift(shiftSortArray)

 #  printData()
    print("number of comparisons for all bubbleSort:", compCounter, "\n")

# all insertionSorts
def allInsertion():
    getDataFromFile()

    sortedData = callInsertion()
    transpose(sortedData)
    
    sortedData = callInsertion()

    untranspose(sortedData)

    sortedData = callInsertion()
    shiftArray = shift(sortedData)
    shiftSortArray = []

    for item in shiftArray:
        col = insertionSort(item)
        shiftSortArray.append(col)
     
    unshift(shiftSortArray)
 #   printData()
    print("number of comparisons for all insertionSort:", compCounter, "\n")


# merge, merge, insertion, bubble
def mMIB():
    getDataFromFile()

    sortedData = callMerge()

    transpose(sortedData)

    sortedData = callMerge()

    untranspose(sortedData)

    sortedData = callInsertion()

    shiftArray = shift(sortedData)
    shiftSortArray = []

    for item in shiftArray:
        col = bubbleSort(item)
        shiftSortArray.append(col)
     
    unshift(shiftSortArray)

 #   printData()
    print("number of comparisons for all 2 merge, 1 insertion, 1 bubble:", compCounter, "\n")


# bubble, bubble, merge, merge
def bBMM():
    getDataFromFile()

    sortedData = callBubble()

    transpose(sortedData)

    sortedData = callBubble()

    untranspose(sortedData)

    sortedData = callMerge()

    shiftArray = shift(sortedData)
    shiftSortArray = []

    for item in shiftArray:
        col = mergeSort(item)
        shiftSortArray.append(col)
     
    unshift(shiftSortArray)

 #   printData()
    print("number of comparisons for all 2 bubble, 2 merge:", compCounter, "\n")

# insertion, insertion, merge, merge
def iIMM():
    getDataFromFile()

    sortedData = callInsertion()

    transpose(sortedData)

    sortedData = callInsertion()

    untranspose(sortedData)

    sortedData = callMerge()

    shiftArray = shift(sortedData)
    shiftSortArray = []

    for item in shiftArray:
        col = mergeSort(item)
        shiftSortArray.append(col)
     
    unshift(shiftSortArray)

 #   printData()
    print("number of comparisons for all 2 insertion, 2 merge:", compCounter, "\n")

# merge, merge, insertion, insertion
def mMII():
    getDataFromFile()

    sortedData = callMerge()

    transpose(sortedData)

    sortedData = callMerge()

    untranspose(sortedData)

    sortedData = callInsertion()

    shiftArray = shift(sortedData)
    shiftSortArray = []

    for item in shiftArray:
        col = insertionSort(item)
        shiftSortArray.append(col)
     
    unshift(shiftSortArray)

 #   printData()
    print("number of comparisons for all 2 merge, 2 insertion:", compCounter, "\n")





def main():
    global compCounter

    # use create file to make your own lists
    # you can also uncomment and then comment out the sorts that you desire to use on the program
    createFile()
 
    allMerge()
    compCounter = 0
    
    allBubble()
    compCounter = 0
    
    allInsertion()
    compCounter = 0

    mMIB()
    compCounter = 0

    bBMM()
    compCounter = 0
    iIMM()
    
    compCounter = 0
    mMII()
    

main()

