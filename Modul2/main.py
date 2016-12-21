from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk import wordpunct_tokenize
from nltk.corpus import words
from nltk.corpus import wordnet
from nltk import pos_tag
from nltk.stem.porter import PorterStemmer
import enchant

import json


def isEnglish(text):
	word_tokens = word_tokenize(text)
	#for word in word_tokens:
	#	if word in ".,?!;":
	#		word_tokens.remove(word)
	english_vocab = set(w.lower() for w in words.words())
	text_vocab = set(w.lower() for w in word_tokens if w.lower().isalpha())
	unusual = text_vocab.difference(english_vocab)
	return len(unusual) < (len(word_tokens) / 3), unusual


def getSentences(text):
	return sent_tokenize(text)


def breakSentenceInTokens(sentence, enDict):
	type = 'na'
	word_tokens = word_tokenize(sentence)
	if word_tokens[-1] == '.':
		type = 'declarative'
	elif word_tokens[-1] == '?':
		type = 'interrogative'
	elif word_tokens[-1] == '!':
		type = 'exclamatory'

	for word in word_tokens:
		if word in ".,?!;":
			word_tokens.remove(word)
			continue
		#word_tokens[word_tokens.index(word)] = word.lower();
		if word in unusual:
			print(word)
			print(enDict.suggest(word))
	return type, word_tokens


# ############ MAIN #######################

output_data = {}

input_file = open("user_input", 'r')
text = ""
for line in input_file:
	text += line.strip()

bool, unusual = isEnglish(text)
if bool:
	print("maybe english")
	sentences = getSentences(text)
	englishDictionary = enchant.Dict("en_US")
	i = 1
	for sentence in sentences:
		key = 'sentence'+str(i)
		i += 1
		output_data[key] = {'sentence': sentence}
		type, word_tokens = breakSentenceInTokens(sentence, englishDictionary)
		output_data[key]['type'] = type
		output_data[key]['tokens'] = word_tokens
		output_data[key]['POS'] = {}
		output_data[key]['LEM'] = {}
		porter_stemmer = PorterStemmer()
		for token in word_tokens:
			output_data[key]['POS'][token] = pos_tag(token)
			output_data[key]['LEM'][token] = porter_stemmer.stem(token)

else:
	print("not English")
	output_data['language'] = 'notEnglish'

with open('data.txt', 'w') as outfile:
	json.dump(output_data, outfile)


# lang detection
'''
languages_ratios = {}
for language in stopwords.fileids():
	stopwords_set = set(stopwords.words(language))
	words_set = set(word_tokens)
	common_elements = words_set.intersection(stopwords_set)
	languages_ratios[language] = len(common_elements)  # language "score"
most_rated_language = max(languages_ratios, key=languages_ratios.get)
output_data[key]['lang'] = most_rated_language
'''
