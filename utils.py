
def extract_skills(nlp_text, noun_chunks, skills):
    '''
    Helper function to extract skills from spacy nlp text

    :param nlp_text: object of `spacy.tokens.doc.Doc`
    :param noun_chunks: noun chunks extracted from nlp text
    :return: list of skills extracted
    '''
    tokens = [token.text for token in nlp_text if not token.is_stop]

    skillset = []
    # check for one-grams
    for token in tokens:
        if token.lower() in skills:
            skillset.append(token)

    # check for bi-grams and tri-grams
    for token in noun_chunks:
        token = token.text.lower().strip()
        if token in skills:
            skillset.append(token)

    return [i.capitalize() for i in set([i.lower() for i in skillset])]

def make_ngrams(nlptext, n):
        # punctuations = '!"#$%&\'()*+,-/:;<=>?@[\\]^_`{|}~'
        punctuations = '!"$%&\'()*,:;<=>?@[\\]^_`{|}~'

        ngrams = []

        tkns = [token.text[0].lower() + token.text[1:] for token in nlptext if not token.is_stop]
        tkns = [t for t in tkns if t not in punctuations]

        if n==2:
            #bigrams
            for i in range(len(tkns)-1):
                ngrams.append(tkns[i]+tkns[i+1])
                ngrams.append(tkns[i]+' '+tkns[i+1])
        elif n==3:
            #trigrams
            for i in range(len(tkns)-2):
                ngrams.append(tkns[i]+tkns[i+1]+tkns[i+2])
                ngrams.append(tkns[i]+' '+tkns[i+1]+' '+tkns[i+2])
                ngrams.append(tkns[i]+' '+tkns[i+1]+tkns[i+2])

        return ngrams

def extract_ngramskills(ngrams, skills):
        skillset = []

        for i in range(len(ngrams)):
            if ngrams[i] in skills:
                skillset.append(ngrams[i][0].upper()+ngrams[i][1:])

        return skillset