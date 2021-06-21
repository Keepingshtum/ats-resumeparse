import re
from datetime import date



def expcalc1(firstmonth,firstyear,secondmonth,secondyear):
    year1=firstyear[-4:]
    


    year2=secondyear[-4:]

    
    
    m1=firstmonth.lower()
    m2=secondmonth.lower()
    m1=m1[0:3]
    
    m2=m2[0:3]
    
    month1=0
    month2=0
    if(m1=="jan"):
        month1=1
        
    if(m1=="feb"):
        month1=2
    if(m1=="mar"):
        month1=3
    if(m1=="apr"):
        month1=4
    if(m1=="may"):
        month1=5
    if(m1=="jun"):
        month1=6
    if(m1=="jul"):
        month1=7
    if(m1=="aug"):
        month1=8
    if(m1=="sep"):
        month1=9
    if(m1=="oct"):
        month1=10
    if(m1=="nov"):
        month1=11
    if(m1=="dec"):
        month1=12

    if(m2=="jan"):
        month2=1
    if(m2=="feb"):
        month2=2
    if(m2=="mar"):
        month2=3
    if(m2=="apr"):
        month2=4
    if(m2=="may"):
        month2=5
    if(m2=="jun"):
        month2=6
    if(m2=="jul"):
        month2=7
    if(m2=="aug"):
        month2=8
    if(m2=="sep"):
        month2=9
    if(m2=="oct"):
        month2=10
    if(m2=="nov"):
        month2=11
    if(m2=="dec"):
        month2=12


    
    years=(int(year2)-int(year1))*12
    
    months=(month2-month1)
    
    total=(months+years)/12
    return total

def expcalc2(m1,y1,m2,y2):
    if len(y1)==2:
        y2=int(y2)%100
    years=(int(y2)-int(y1))*12
    months=(int(m2)-int(m1))

    total=(months+years)/12
    return total













          