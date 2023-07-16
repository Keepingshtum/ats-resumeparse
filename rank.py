import csv 
import pandas as pd 
filename = "rank.csv"
fields = [] 
rows = [] 
id=[]
se=[]
sc=[]
urank=[]
crank=[]
totalexp=[]
subsection=[]
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
    totalexp.append(row[5])

for i in range(len(id)):
    
    if(float(se[i])==1):
        if(float(sc[i])>=4):
            subsection.append(3)
        elif(float(sc[i])>=2 and float(sc[i])<4):
            subsection.append(2)
        else:
            subsection.append(1)    
    else:
        if(float(sc[i])>=2):
            subsection.append(2)
        else:
            subsection.append(1)    
data = pd.read_csv("rank.csv")
data["subsection"] = subsection
data['sorting_column'] = data.urank*0.1 + data.crank*0.1 + data.skillexp*0.4+data.sc*(0.3/5)+data.totalexp*0.1
cols = ['subsection', 'sorting_column']
data['Rank'] = data.sort_values(cols, ascending=False).groupby(cols, sort=False).ngroup() + 1
data.sort_values("Rank", inplace = True)
print(data) 
data.to_csv('after_rank.csv', index=False) 
  
 



  
