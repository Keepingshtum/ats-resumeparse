
import re
import ycalc
from datetime import datetime
line=" 04/2016 – 06-2017 "

find=re.findall(r"\s+[0-9]{0,2}?[/-]?[01]?[0-9]{1}[-/]1?9?2?0?[0-9]{0,2}",line)
x=re.split('/|-', find[0])
y=re.split('/|-', find[1])
lsecondyear=str(datetime.now().year)
lsecondmonth=datetime.now().month



print(find)
print(x)


ycalc.expcalc2(x[0],x[1],y[0],y[1])

print(lsecondyear)
print(lsecondmonth)