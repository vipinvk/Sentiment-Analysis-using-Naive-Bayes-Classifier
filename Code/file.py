### NLP Example Code - Sentiment Analysis
### Vipin VK
### Python 3.8.10 (64-bit) 

#Importing the necessary libaries/classes

from textblob.classifiers import NaiveBayesClassifier
import fileread
from  nltk.corpus import stopwords 
import re
import random
from textblob import Word
from sklearn.metrics import accuracy_score,confusion_matrix


def define_stopwords(stopwords_old):
    '''
    Function for defining our own set of stopwords
    Input variables : NLTK's set of stopwords
    Return variables : updated set of stopwords
    '''
    stopwords_updated = []
    list = ['no','nor','not','don',"don't",'ain','aren',
    "aren't",'couldn',"couldn't",'didn',"didn't",'doesn',
    "doesn't",'hadn',"hadn't",'hasn',"hasn't",'haven',
    "haven't",'isn',"isn't",'mightn',"mightn't",'mustn',
    "mustn't",'needn',"needn't",'shan',"shan't",'shouldn',
    "shouldn't",'wasn',"wasn't",'weren',"weren't",'won',
    "won't",'wouldn',"wouldn't"]
    for item in stopwords_old:
        if item not in list:
            stopwords_updated.append(item)
    return stopwords_updated 

def remove_stopwords(Sentence,stopwords):
    '''
    Function for removing stopwords from our data
    Input variables : Sentences from data and stopwords
    Return variables : Sentences after stopwords removal
    '''    
    Sentence = ' '.join([word for word in Sentence.split() if word not in stopwords])
    return Sentence

def word_filter(sentence):
    '''
    Function for removing unwanted text/charectors
    Input variables : Sentences from Data
    Return variables : Sentences after words filtering
    '''    
    neg_list = ['no','nor','don',"don't",'ain','aren',
    "aren't",'couldn',"couldn't",'didn',"didn't",'doesn',
    "doesn't",'hadn',"hadn't",'hasn',"hasn't",'haven',
    "haven't",'isn',"isn't",'mightn',"mightn't",'mustn',
    "mustn't",'needn',"needn't",'shan',"shan't",'shouldn',
    "shouldn't",'wasn',"wasn't",'weren',"weren't",'won',
    "won't",'wouldn',"wouldn't","dont","arent","couldnt",
    "didnt","doesnt","hadnt","hasnt","havent","isnt",
    "mightnt","mustnt","neednt","shant","shouldnt","wasnt",
    "werent","wont","wouldnt","can't","cant","aint"]
    sentence = ' '.join(["not" if word in neg_list else word for word in sentence.split() ])
    CLEAN = re.compile('<.*?>')
    sentence = re.sub(CLEAN, '', sentence)
    sentence = ' '.join([(re.sub(r'[^A-Za-z0-9]+',' ',text)) for text in sentence.split()])
    sentence = ' '.join([Word(word.lower()).lemmatize('v') for word in sentence.split()])
    return sentence

print("Importing train and test files")

train_file =[]
readobj = fileread.dataread()
for label in ('pos','neg'):
    train_file = readobj.read_file(label,train_file)

test_file = []
for label in ('pos_test','neg_test'):
    test_file = readobj.read_file(label,test_file)

print("Files imported")

stopwords = define_stopwords(stopwords.words("English"))

train=[]
for item in train_file:
    train_temp = (remove_stopwords(item[0],stopwords))
    train.append((word_filter(train_temp),item[1]))

print("Training files are ready")

random.shuffle(train)

print("Model training in progress")
cl = NaiveBayesClassifier(train)

print("Model trained")

test=[]
for item in test_file:
    testf_temp = (remove_stopwords(item[0],stopwords))
    test.append((word_filter(testf_temp),item[1]))

print("Tesitng files are ready")

y_test = []
y_pred = []
for items in test:
    #print("{} : is : {}".format(items[1],cl.classify(list(items)[0])))
    y_test.append(items[1])
    y_pred.append(cl.classify(list(items)[0]))

print(cl.accuracy(test)*100,"% is the accuracy over Test data")            
print(accuracy_score(y_test, y_pred)*100,"% is the accuracy using SK Learn Metrices")
conf_matrix = confusion_matrix(y_test,y_pred)
print("Confusion Matrix for the result : \n",conf_matrix)