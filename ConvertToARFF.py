import csv
import pdb


#Variable Intialization
filename = "Data.txt"
ITEMS = set()
arffFilename = filename.split(".")[0] + ".arff"

myfile = csv.reader(open(filename,'rb'))


#Get List of all the unique items from the Input
for line in myfile:
    [ITEMS.add(item.strip()) for item in line]


myARFF = open(arffFilename,'w+')
myARFF.write('@relation Weka\n\n\n')

ITEMS = list(ITEMS) #So that items will iterate in order
for item in ITEMS: myARFF.write(str("@attribute "+item+" {false,true}\n"))

myARFF.write('\n\n@data\n\n')

#Iterate over the data file
myfile = csv.reader(open(filename,'rb'))

for line in myfile:
    newLine = "{ "

    for word in line:         
        newLine += str(str(ITEMS.index(word.strip()))+" "+"true"+",")

    writeLine = newLine[:-1]
    writeLine += "}\n"
    print writeLine
    myARFF.write(writeLine)

myARFF.close()





    


