import nltk
from nltk import sent_tokenize
from nltk import word_tokenize
from nltk.probability import FreqDist
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
import os

"""
#open text file
text_file = open("testtext.txt", encoding="utf8")
#read text data
text = text_file.read()

#display text
print(type(text))
print("\n")
print(text)
print("\n")
print(len(text))

#tokenizing sentences
"""

class TextFileReader(object):
    """
    util:
    -read text
    -tokenize sentences and words
    -plot frequency of words
    -remove punctuation marks
    -remove stopwords
    -
    """
    def __init__(self, text_file_path:str):
        assert os.path.exists(text_file_path)   #assert file existence
        assert text_file_path.endswith('.txt')
        self.file_path = text_file_path
        self.wordtok = [] #tokenized words
        self.senttok = [] #tokenized sentences
        self.cleanword = [] #remove punctuations & stopwords

    
    @property
    def text_str(self):
        return open(self.file_path, encoding="utf8").read()
        
    @property
    def sentences(self):
        self.senttok = sent_tokenize(self.text_str)
        return self.senttok
    
    @property
    def words(self):
        self.wordtok = word_tokenize(self.text_str)
        return self.wordtok


def fdist(wlist:list):
    assert len(wlist) != 0, "Error: empty list"
    fdist = FreqDist(wlist)
    fdist.most_common(10)
    return fdist.plot(10)
        
def nopunc(wlist:list):
    list_nopunc =[]
    assert len(wlist) != 0, "Error: empty list"
    for w in wlist:
        if w.isalpha():
            list_nopunc.append(w.lower())
    return list_nopunc

def wcloud(text):
    worldcloud = WordCloud().generate(text)
    plt.figure(figsize = (12,12))
    plt.imshow(worldcloud)
    plt.axis("off")
    plt.show

def rmstopwords(wlist:list):
    english_stop = stopwords.words("english")
    tokens = [token.lower() for token in tokens
                if token.lower() not in english_stop]
    print("Length: " + len(tokens))
    return tokens


            
        
        


def func(text):
    global sentences
    global words

    sentences = sent_tokenize(text)
    print("\n")
    print("Length: " + str(len(sentences)))
    print(sentences)
    #tokenizing words
    print("\n")
    words = word_tokenize(text)
    print("Length: " + str(len(words)))
    print(words)

    #return sentences, words




#find frequency distribution:
fdist = FreqDist(words)
"""find 5 most common"""
fdist.most_common(10)

#plot frequency
fdist.plot(10)

#removing punctuations(using .isalpha)
no_punc = [] #empty list to append

for w in words:
    if w.isalpha():
        no_punc.append(w.lower())

print("Length: " + str(len(no_punc)))
print(no_punc)

fdist = FreqDist(no_punc)
fdist.most_common(10)
fdist.plot(10)

#removing stopwords:
clean_words = []
stopwords = stopwords.words("english")

for w in no_punc:
    if w not in stopwords:
        clean_words.append(w)

print("Length: " + str(len(clean_words)))
print(clean_words)

fdist = FreqDist(clean_words)
fdist.most_common(10)
fdist.plot(10)

#wordcloud:
from wordcloud import WordCloud







    

