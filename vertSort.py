# Vertical Sort
#
#
# By Jack Pharies and Rob Ranseen


#global variables
data = []
compCounter = 0
r = 0
s = 0

#creates the list from a given file where the first line is the number of rows and the second line is the number of colums followed by the data
def getDataFromFile():
    global data
    global r
    global s

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
def transpose():
    global data
    sortedData = sortMerge()
    newData = []
    for col in range(s):
        newRow = []
        for row in range(r):
            newRow.append(sortedData[col][row])
            if (row+1) % s == 0:
     
                newData.append(newRow)
                newRow = []
                
    data = newData

        

    

def untranspose():
    global data
    sortedData = sortMerge()

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
        
        
        

  
    

def shift():
    global data

    key = r//2

    negInf = float("-inf")
    posInf = float("inf")
    
    sortedData = sortMerge()

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
  

    shiftSortArray = []

    for item in shiftArray:
        col = mergeSort(item)
        shiftSortArray.append(col)

    

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
# puts the items in colum lists
def sortMerge():


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
        

            


# mergesort my love
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

def createFile():
    #dataFile = open("data.txt", "w")
    print("Follow the prompts to create a randomly generated file in data.txt")
    print("rows(r) and Cols(s) must follow the rules r < 2*((s-1)*(s-1)) and r % s != 0")
    rows = int(input("Enter numbers of Rows: "))
    cols = int(input("Enter numbers of Cols: "))
    while rows < 2*((cols-1)*(cols-1)) or rows % cols != 0:
        rows = int(input("Enter numbers of Rows: "))
        cols = int(input("Enter numbers of Cols: "))
    
    dataFile = open("data.txt", "w")
    dataFile.write(str(rows)+"\n")
    dataFile.write(str(cols))
    dataFile.close()

    
    
def main():
    createFile()
    getDataFromFile()
    
    transpose()

    untranspose()

    shift()
    printData()
    print("number of comparisons:", compCounter)

    

main()

