import math
import operator
k = 2
tempkey={}



def hitung(sepallength, sepalwidth, petallength, petalwidth):
    count=0
    temp = []
    tempdir = {}
    with open('Iris.csv') as f:
        for line in f:
            count = count + 1
            if count == 1: #cek disini, kalo baris pertama maka diskip, karena itu judul
                continue
            else:
                x = line.split(',')
                hitung = ((sepallength - float(x[1]))**2)+((sepalwidth - float(x[2]))**2)+((petallength - float(x[3]))**2)+((petalwidth - float(x[4]))**2)
                hitung = math.sqrt(hitung)
                temp.append((hitung,x[0],x[5]))
        temp.sort()
        for x in range(0,k):
            if x == 0:
                tempkey[temp[x][2]]=1
            else:
                if tempkey.has_key(temp[x][2]):
                    tempkey[temp[x][2]]=tempkey[temp[x][2]]+1
                else:
                    tempkey[temp[x][2]]=1

        print tempkey
        print max(tempkey.iteritems(), key=operator.itemgetter(1))[0]
                
k = input("K: ")
sepallength = input("Sepal Lenght: ")
sepalwidth = input("Sepal Width: ")
petallength = input("Petal Length: ")
petalwidth = input("Petal Width: ")

hitung(sepallength, sepalwidth, petallength, petalwidth)
    
