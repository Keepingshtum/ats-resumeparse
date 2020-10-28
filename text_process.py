import re, string, unicodedata
import nltk
import contractions
import inflect
import textract
from bs4 import BeautifulSoup
from nltk import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import LancasterStemmer, WordNetLemmatizer

def remove_non_ascii(words):
    """Remove non-ASCII characters from list of tokenized words"""
    new_words = []
    for word in words:
        new_word = unicodedata.normalize('NFKD', word).encode('ascii', 'ignore').decode('utf-8', 'ignore')
        new_words.append(new_word)
    return new_words

def to_lowercase(words):
    """Convert all characters to lowercase from list of tokenized words"""
    new_words = []
    for word in words:
        new_word = word.lower()
        new_words.append(new_word)
    return new_words

def remove_punctuation(words):
    """Remove punctuation from list of tokenized words"""
    new_words = []
    for word in words:
        new_word = re.sub(r'[^\w\s]', '', word)
        if new_word != '':
            new_words.append(new_word)
    return new_words

def replace_numbers(words):
    """Replace all interger occurrences in list of tokenized words with textual representation"""
    p = inflect.engine()
    new_words = []
    for word in words:
        if word.isdigit():
            new_word = p.number_to_words(word)
            new_words.append(new_word)
        else:
            new_words.append(word)
    return new_words

def remove_stopwords(words):
    """Remove stop words from list of tokenized words"""
    new_words = []
    for word in words:
        # print(word)
        if word not in stopwords.words('english'):
            new_words.append(word)
    return new_words

def stem_words(words):
    """Stem words in list of tokenized words"""
    stemmer = LancasterStemmer()
    stems = []
    for word in words:
        stem = stemmer.stem(word)
        stems.append(stem)
    return stems

def lemmatize_verbs(words):
    """Lemmatize verbs in list of tokenized words"""
    lemmatizer = WordNetLemmatizer()
    lemmas = []
    for word in words:
        lemma = lemmatizer.lemmatize(word, pos='v')
        lemmas.append(lemma)
    return lemmas

def normalize(words, criteria=''):
    words = remove_non_ascii(words)
    words = to_lowercase(words)
    if criteria != "skip":
        words = remove_punctuation(words)
    words = replace_numbers(words)
    words = remove_stopwords(words)
    words = stem_words(words)
    words = lemmatize_verbs(words)
    return words

def extractdoctext():
    file_path = r'C:\Users\Praneeth\Anaconda3\envs\resume_screening\Automated-Resume-Screening-System\dsresumes\DSResume.docx'
    doc_txt = textract.process(file_path) 
    text_form = doc_txt.decode('utf-8')
    return text_form

def processtext(sometxt, criteria=''):
    words = str(sometxt)

    words = nltk.word_tokenize(words)

    words = normalize(words, criteria)
    # print(words)
    words = ' '.join(map(str, words))
    return words
    # print(words)


# ab = "Very commonly, however, various constraints are added. For example, one might want to match the 'needle' only where it consists of one (or more) complete words—perhaps defined as not having other letters immediately adjacent on either side. In that case a search for 'hew' or 'low' should fail for the example sentence above, even though those literal strings do occur."

# ab = "Having 3 years of relevant experience as Data Scientist in creating working models. \
# Good practical knowledge in different supervised and unsupervised learning techniques such as parametric/non-parametric algorithms, support vector machines, kernels, clustering and dimensionality reduction (PCA, LDA). \
# Good knowledge and understanding in different regression, classification, clustering techniques. \
# Extensive experience in Importing, Cleaning, Manipulating, Summarizing the data and Building machine learning Regression models and data pipelines. \
# Experience in skills Pandas, NumPy, Matplotlib and Scikit-learn to load manipulate analyse and visualize data sets using Python.\
# Worked on Jupyter Notebook, Spyder IDE and Google Colab.\
# Experienced with machine learning algorithm such as logistic regression, KNN, SVM, random forest, linear regression, k-means clustering, Decision Tree, Random forest, Deep Reinforcement learning. \
# Evaluated models using Cross Validation, Log loss function, ROC curves and used AUC for feature selection. \
# Excellent communication skills. Successfully working in fast-paced multitasking environment both independently and in collaborative team, a self-motivated enthusiastic learner."


