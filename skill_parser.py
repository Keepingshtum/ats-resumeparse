import os
import spacy
import pprint
import utils

class ResumeParser(object):

    def __init__(self, resumetext, skills):
        nlp = spacy.load('en_core_web_sm')
        
        self.__resumetext = resumetext
        self.__skills = skills
        self.__details = {'skills matched': None, 'score': 0}
        self.__nlp = nlp(self.__resumetext)
        self.__noun_chunks = list(self.__nlp.noun_chunks)
        self.__get_basic_details()
        

    def get_extracted_data(self):
        return self.__details

    def __get_basic_details(self):
        skills = utils.extract_skills(self.__nlp, self.__noun_chunks, self.__skills)

        bigrams = utils.make_ngrams(self.__nlp, 2)
        trigrams = utils.make_ngrams(self.__nlp, 3)
        
        bigramskills = utils.extract_ngramskills(bigrams, self.__skills)
        trigramskills = utils.extract_ngramskills(trigrams, self.__skills)

        skills = list(set().union(skills,bigramskills,trigramskills))
        
        self.__details['skills matched'] = skills
        self.__details['score'] = len(skills)/len(self.__skills)
        # print(len(self.__skills), len(skills))

        return  

# if __name__ == '__main__':

#     line1 = 'Experience in AWS, C#, Pandas, NumPy, Matplotlib, Angular 9, tcp/ip, django-suit' 
#     line2 = ', scikit-image and scikit-learn to load manipulate analyse and visualize data sets using Python.'
#     line3 = 'Oracle 11g, Unsupervised learning, F#, .net framework, hadoop, sap, flask, reactjs, git, jupyter notebook'

#     skills = ['django', 'angular 9', 'scikit-learn', 'pyspark', 'scikit-image', 'f#', 'c++', '.net framework', 'oracle 11g', 'unsupervised learning']

#     txt = line1+line2+line3

#     data = ResumeParser(txt, skills).get_extracted_data()
#     pprint.pprint(data)
