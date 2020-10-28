import skill_parser
import pprint

line1 = 'Experience in AWS, C#, Pandas, NumPy, Matplotlib, Angular 9, tcp/ip, django-suit' 
line2 = ', scikit-image and scikit-learn to load manipulate analyse and visualize data sets using Python.'
line3 = 'Oracle 11g, Unsupervised learning, F#, .net framework, hadoop, sap, flask, reactjs, git, jupyter notebook'

skills = ['django', 'angular 9', 'scikit-learn', 'pyspark', 'scikit-image', 'f#', 'c++', '.net framework', 'oracle 11g', 'unsupervised learning']

txt = line1+line2+line3

data = skill_parser.ResumeParser(txt, skills).get_extracted_data()
pprint.pprint(data)