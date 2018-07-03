# Q1+Q2

import csv


import requests

response = requests.get('https://raw.githubusercontent.com/justmarkham/pandas-videos/master/data/drinks.csv')
print(response.text)
r = response.text
fn = open("drinks.csv", 'w')
fn.write(r)
fn.close()
with open('drinks.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        print(row)
# Q3
import csv

fieldnames = ["country", "beer_servings", "spirit_servings", "wine_servings,total"]

csvfilepath = 'drinks.csv'
jsonfilepath = 'drinks.json'

# Read the csv and add the data to a dictionary
data = {}
with open(csvfilepath) as csvfile:
    csvreader = csv.DictReader(csvfile)
    for csvRow in csvreader:
        country = csvRow["country"]
        beer_servings = csvRow["beer_servings"]
        spirit_servings = csvRow["spirit_servings"]
        wine_servings = csvRow["wine_servings"]
        total_litres_of_pure_alcohol = csvRow["total_litres_of_pure_alcohol"]
        data[country] = csvRow
variable = data["Argentina"]
print(variable)
# Q4
print(type(data))
print(data.keys())
print(data.values())
x = []
k = data.keys()
z = 0
j = 0
for i in k:
    y = dict(data[i])
    z = float(y['total_litres_of_pure_alcohol']) + z
    j = j + 1
    print(float(y['total_litres_of_pure_alcohol']))
z = z / j
print(z)
# Q5
import requests

result = requests.get('http://jsonplaceholder.typicode.com/todos').json()
r = print(result)
print(type(result))
print(type(result[0]))
e = 0
for i in result:
    if i['completed'] == False:
        print(i)
        e = + 1
L = e / (len(result))
print(L)
# Q6
import requests
r = requests.get('http://www.umich.edu/~umfandsf/other/ebooks/alice30.txt')
word_dict = {}
for word in r.text.split():
    if word_dict.get(word, None) == None:
       word_dict[word] = 0
       word_dict[word] += 1

for key, val in word_dict.items():
    print(key, ' - ', val)

#Q7
import numpy as np
arr=np.arange(9).reshape(3,3)
print(arr)
#Q8
vec=np.random.rand(1,10)
print(vec)
#Q9
arr=np.random.randint(5,20,20).reshape(1,20)
print(arr)
an = arr.reshape(4,5)
print(an)
ap=an.transpose()
print(ap)
print(ap.item(7))
#Q10
vecto=np.random.rand(1,30)
print(vecto.mean)
#Q11
L1= [1,3,4,5,2,9]
L2=[22,12,4,32,56,7]
myarray = np.asarray(L1)
myarray2 = np.asarray(L2)
print(myarray*myarray2)
#Q12
myarray=myarray.reshape(2,3)
myarray2=myarray2.reshape(2,3)
mi = np.vstack((myarray,myarray2))
print(mi[2:,2])
#Q13
print(np.sum([mi], axis=2))