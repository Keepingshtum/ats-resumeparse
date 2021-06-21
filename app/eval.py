import expgen
import docx
import re
import sys
import tika
from tika import parser
from datetime import datetime
import ycalc
from skill_parser import ResumeParser

se=0
sc=0
te=0
a=0
b=1
c=2
l=expgen.expgen("r1.docx")
if(len(l)==2):
	sc=l[0]
	se=l[1]
	te=l[2]
while(len(l)>c):
	se+=l[a]
	if(l[b]>sc):
		sc=l[b]
	te=l[c]
	a=a+1
	b=b+1
	c=c+1
print(se,sc,te)
