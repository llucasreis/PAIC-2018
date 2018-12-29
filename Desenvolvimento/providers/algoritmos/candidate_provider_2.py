import PyPDF2
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from collections import Counter
from math import *
import pandas as pd
pd.options.display.max_colwidth = 10000
import unicodedata
import re
import sys
import pdftotext
if not sys.warnoptions:
    import warnings
    warnings.simplefilter('ignore')

punctuations = ['(',')',';','-','!','.',':','[',']',',','"',' ']

candidate = {
    'saude' : 0,
    'seguranca' : 0,
    'educacao' : 0,
    'economia' : 0,
    'cultura' : 0,
    'tecnologia': 0,
    'meio ambiente': 0
}

radical_words = {
    'saude' : ['saude','hosp','medic','remedio','doen','enferm'],
    'seguranca' : ['seguranca','polic','crim','violen','preso','presidi'],
    'educacao' : ['educac','professor','escola','ensino','alun','faculdade','universi'],
    'economia' : ['economi','produ','mercado','comerci','industr','desenvolv','terceiriz','setor','agro','agric'],
    'cultura' : ['cultura','turis','parque','museu','music','arte','cinema','danc'],
    'tecnologia' : ['tecno','inovac','ciencia','cienti','conhecim','comput'],
    'meio ambiente' : ['ambiente','florest','preserva','natur','desmatamento','polu','clima'],
}

df = {}

df['pagina'], df['texto'], df['total'] = [], [], []

def removeSpecialCharacters(word):
    nfkd = unicodedata.normalize('NFKD', word)
    palavraSemAcento = u"".join([c for c in nfkd if not unicodedata.combining(c)])
    #return re.sub('[^a-zA-Z0-9 \\\]','',palavraSemAcento)
    return re.sub('[^a-zA-Z \\\]','',palavraSemAcento)

def processing1(tokens):
    return [removeSpecialCharacters(word.lower()) for word in tokens
            if not word in punctuations and not word.startswith('www') and not word.startswith('//') and word]

def processing2(keywords, stop_words):
    return [word for word in keywords if not word in stop_words]

def count_words_from(filename):
    global candidate,df

    candidate = {key: 0 for key in candidate}
    df = {}
    df['pagina'], df['texto'], df['total'] = [], [], []
    
    proposal = '../propostas-candidatos/proposta-' + filename + '.pdf'


    #if filename == 'amoedo' or filename == 'alckmin':
    with open(proposal, 'rb') as f:
        pdf = pdftotext.PDF(f)

    text = ""

    for i in range(len(pdf)):
        new_text = pdf[i]

        df['pagina'].append(i+1)
        df['texto'].append(new_text)

        text += new_text
    '''
    else:   
        pdfFileObj = open(proposal, 'rb')
    
        pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    
        num_pages = pdfReader.numPages
    
        text, count = "", 0
    
        while count < num_pages:
            pageObj = pdfReader.getPage(count)
            
            count += 1
            new_text = pageObj.extractText()
            
            df['pagina'].append(count)
            df['texto'].append(new_text)
            
            text += new_text
    '''
    
    tokens = word_tokenize(text)
    
    keywords = processing1(tokens)
    
    stop_words = stopwords.words('portuguese')
    
    keywords = processing2(keywords, stop_words)
    
    count_words = Counter(keywords)
    
    for area,radical_area in radical_words.items():
        for radical in radical_area:
            for word,value in count_words.items():
                if radical in word:
                    candidate[area] += value
                    
    return candidate

def getCand(candname):
	global candidate,df

	candidate = count_words_from(candname)

	for area in candidate.keys():
		df[str(area)] = [0] * len(df['pagina'])

	for i,text in enumerate(df['texto']):
		tokens = word_tokenize(text)
		keywords = processing1(tokens)

		df['total'].append(len(keywords))
		count_words = Counter(keywords)

		for area,radical_area in radical_words.items():
			for radical in radical_area:
				for word,value in count_words.items():
					if radical in word:
						df[area][i] += value

	df = pd.DataFrame(data=df)

	df.index = df['pagina']

	df.drop(['pagina'],axis=1,inplace=True)
	df.drop(['texto'],axis=1,inplace=True)

	df_tfidf = pd.DataFrame()

	for area in candidate.keys():
		df_tfidf['tf_' + str(area)] = df[str(area)] / df.total

		idf = len(df) / len(df[str(area)].loc[df[str(area)] > 0])

		df_tfidf['tfidf_' + str(area)] = df_tfidf['tf_' + str(area)] * idf

	tfidf = {}

	for area in candidate.keys():
		tfidf[area] = df_tfidf['tfidf_' + str(area)].sum()

	return tfidf

if __name__ == '__main__':
    candidates = ['alckmin', 'amoedo', 'bolsonaro', 'ciro', 'daciolo','boulos', 'haddad', 'marina']

    dict_cand = {}
    for cand in candidates:
        dict_cand[cand] = getCand(cand)

    df_cand = pd.DataFrame(data=dict_cand).T

    df_cand.to_csv('../../datasets/candidate.csv', index=False)