import PyPDF2
import textract
import pandas as pd

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

from collections import Counter

import unicodedata
import re

import sys
if not sys.warnoptions:
	import warnings
	warnings.simplefilter("ignore")

punctuations = ['(',')',';','-','!','.',':','[',']',',','"']

candidate = {
	'saude' : 0,
	'seguranca' : 0,
	'educacao' : 0,
	'economia' : 0,
	'cultura' : 0,
	'tecnologia': 0,
	'meio ambiente': 0}

radical_words = {
	'saude' : ['saude','hosp','medic','remedio','doen','enferm'],
	'seguranca' : ['seguranca','polic','crim','violen','preso','presidi'],
	'educacao' : ['educac','professor','escola','ensino','alun','faculdade','universi'],
	'economia' : ['economi','produ','mercado','comerci','industr','desenvolv','terceiriz','setor','agro','agric'],
	'cultura' : ['cultura','turis','parque','museu','music','arte','cinema','danc'],
	'tecnologia' : ['tecno','inovac','ciencia','cienti','conhecim','comput'],
	'meio ambiente' : ['ambiente','florest','preserva','natur','desmatamento','polu','clima'],
}

#obtido em https://gist.github.com/boniattirodrigo/67429ada53b7337d2e79
def removeSpecialCharacters(word):
	nfkd = unicodedata.normalize('NFKD', word)
	palavraSemAcento = u"".join([c for c in nfkd if not unicodedata.combining(c)])
	return re.sub('[^a-zA-Z0-9 \\\]','',palavraSemAcento)

def processingKeywords(tokens,stop_words):
	return [removeSpecialCharacters(word.lower()) for word in tokens
			if not word in stop_words and not word in punctuations
			and not word.startswith('www') and not word.startswith('//')]

def count_words_from(filename):
	global candidate
	candidate = {key: 0 for key in candidate}
	proposal = '../propostas-candidatos/proposta-' + filename + '.pdf'
	
	text = ""

	text = textract.process(proposal)
	text = text.decode('utf-8',errors = 'ignore')

	tokens = word_tokenize(text)

	stop_words = stopwords.words('portuguese')

	keywords = processingKeywords(tokens,stop_words)

	count_words = Counter(keywords)

	for area,radical_area in radical_words.items():
		for radical in radical_area:
			for word,value in count_words.items():
				if radical in word:
					candidate[area] += value

	return candidate

if __name__ == "__main__":
	candidates = ['alckmin', 'alvaro', 'amoedo', 'bolsonaro', 'boulos', 'ciro', 'daciolo', 'haddad', 'marina', 'meirelles']

	dict_cand = {}
	for cand in candidates:
		dict_cand[cand] = count_words_from(cand)

	df_cand = pd.DataFrame(data=dict_cand).T

	index_names = list(df_cand.index.values)

	df_cand.to_csv('../../datasets/candidate_2.csv', index=False)