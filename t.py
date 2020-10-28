

import re
import ycalc
from datetime import datetime
from skill_parser import ResumeParser

y=['11', '2017', '2016', '2015', '2013', '10', '2012', '10', '2012', '10', '2006', '10', '2003', '2002', '2000', '1998']
m=[' 9', '    06', '    04', '    01', '       03', ' 9', ' 09', ' 9', ' \t\t\t\t6', ' 9', '\t\t12', ' 9', '\t\t\t\t11', '\t\t              \t\t07', '\t\t\t\t\t\t\t01', '\t\t\t\t\t\t11']

l=len(y)
for x in range(l):
	if(y.count(y[x])>1 and m.count(m[x])>1):
		print(y[x])
		print(m[x])





