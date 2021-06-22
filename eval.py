import expgen
import docx
import re
import sys
import tika
tika.initVM()
from tika import parser
from datetime import datetime
import ycalc
from skill_parser import ResumeParser
import random
import csv
import pandas as pd

see=0
scc=0
tee=0
a=0
b=1
c=2
id=[]
se=[]
sc=[]
urank=[]
crank=[]
totalexp=[]
rows=[]
skillexp=[]
filename="rank.csv"

l=expgen.expgen("r1.docx")
if(len(l)==2):
	scc=l[0]
	see=l[1]
	tee=l[2]
while(len(l)>c):
	see+=l[a]
	if(l[b]>scc):
		scc=l[b]
	tee=l[c]
	a=a+1
	b=b+1
	c=c+1

with open(filename, 'r') as csvfile: 
   
    csvreader = csv.reader(csvfile) 
      
    
    fields = next(csvreader) 
  
     
    for row in csvreader: 
        rows.append(row)
for row in rows:
    
    id.append(row[0])
    se.append(row[1])
    sc.append(row[2])
    urank.append(row[3])
    crank.append(row[4])
    skillexp.append(row[5])
    totalexp.append(row[6])
id.append(len(id)+1)
skillexp.append(float(scc)/10)
se.append(random.choice([0,1]))
sc.append(float(see)*5)
totalexp.append(float(tee)/15)
crank.append(round(random.random(),2))
urank.append(round(random.random(),2))

print(see,scc,tee)
list_of_tuples = list(zip(id,se,sc,urank,crank,skillexp,totalexp))
df = pd.DataFrame(list_of_tuples,
                  columns = ['id', 'se','sc','urank','crank','skillexp','totalexp'])
df.to_csv('rank.csv', index=False) 


