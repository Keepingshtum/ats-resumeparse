import re
from datetime import datetime


firstmonth=[]
firstyear=[]
secondmonth=[]
secondyear=[]
line=" Worked as Test Analyst in Thomson Reuters from Jan’10 to Dec’14."
x=re.findall(r"\b(?i)(?:Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|Jun(?:e)?|Jul(?:y)?|Aug(?:ust)?|Sep(?:tember)?|Oct(?:ober)?|(?:Nov|Dec)(?:ember)?)[ ]*.[ ]*[0-9]{2,4}",line)
print(x)
if(x):
    if(len(x)==1):
        firstyear=re.findall(r"[0-9]{2,4}",x[0])
        firstmonth=re.findall(r"\b(?i)(?:Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|Jun(?:e)?|Jul(?:y)?|Aug(?:ust)?|Sep(?:tember)?|Oct(?:ober)?|(?:Nov|Dec)(?:ember)?)",x[0])
        lsecondmonth=datetime.now().strftime('%h')
        secondmonth=[]
        secondmonth.append(lsecondmonth)
        lsecondyear=str(datetime.now().year)
        secondyear=[]
        secondyear.append(lsecondyear)
        print(firstmonth)
        print(firstyear)
        print(secondmonth)
        print(secondyear)
        

    else:
        
        firstyear=re.findall(r"[0-9]{2,4}",x[0])
        firstmonth=re.findall(r"\b(?i)(?:Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|Jun(?:e)?|Jul(?:y)?|Aug(?:ust)?|Sep(?:tember)?|Oct(?:ober)?|(?:Nov|Dec)(?:ember)?)",x[0])
        secondyear=re.findall(r"[0-9]{2,4}",x[1])
        secondmonth=re.findall(r"\b(?i)(?:Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|Jun(?:e)?|Jul(?:y)?|Aug(?:ust)?|Sep(?:tember)?|Oct(?:ober)?|(?:Nov|Dec)(?:ember)?)",x[1])
        print(firstmonth)
        print(firstyear)
        print(secondmonth)
        print(secondyear)
def expcalc(firstmonth,firstyear,secondmonth,secondyear):
    year1=firstyear[-3:]


    year2=secondyear[-3:]
    
    
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
    print(total)


expcalc(firstmonth[0],firstyear[0],secondmonth[0],secondyear[0])











          