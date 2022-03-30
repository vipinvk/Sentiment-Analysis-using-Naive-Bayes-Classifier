# Sentiment Analysis using Naive Bayes Classifier (IMDB Movie Review)

### About the dataset 
Here in this problem, I have attempted to perform a sentiment analysis on the IMDB Movie review dataset (More details and the dataset can be downloaded [here](https://ai.stanford.edu/~amaas/data/sentiment/).

Even though the dataset has 25000 reviews (12500 reviews each in positive and negative class) for training and 25000 reviews for testing, I have used a smaller subset for training and testing. 4000 reviews (2000x2) were used in the training process and the model was tested on 200 reviews (100x2). The data is copied to the **Data** directory, with '**pos**' and '**neg**' subdirectories for the training data. The testing data are copied into '**pos_test**' and '**neg_test**' subdirectories. Thus the training and testing sets can be increased anytime. You can change the folder structure/content also with minor edits in the code.

### The Code
The script files are saved into the **Code** directory, in which there are 2 files. The _fileread.py_ has the class created for reading the file contents from the Data subdirectories. And the _file.py_ has the actual implementation of classifier. These 2 are small files with very few lines of code in them. 

### Tools/Modules
I have used **Naive Bayes** classifier from _textblob.classifiers_ for performing the classification task. You can read more details [here](https://textblob.readthedocs.io/en/dev/classifiers.html) from the Textblob documentation. I have used the sklearn metrices (accuracy_score and confusion_matrix) for measuring the accuracy of the classification. The stopwords set was imported from the NLTK library.  

### Classification results (over test data)
The test data used is a well balanced one (100 reviews in each positive and negative sentiment) and I received a balanced confusion matrix (as below). I could get an accuracy score of 82% which I feel is pretty decent. I will attempt to fine-tune this initial result and will try to have the content udpated soon.  
 [[89 11]
 [25 75]]
