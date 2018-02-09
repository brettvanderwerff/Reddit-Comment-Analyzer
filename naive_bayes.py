'''Program uses multinomial naive bayes to classify Reddit comments as coming from a redditor of interest
or a random redditor.

Note that this program depends on the user already having run collect_data.py successfully
resulting in a copy of FriesWithThat_comments.txt and random_redditor_comments.txt saved to the disk.
'''

import organize_corpus
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

combine_train, combine_train_label, combine_test, combine_test_label =\
        organize_corpus.run(experimental_file='FriesWithThat_comments.txt',\
                            comparison_file='random_redditor_comments.txt',\
        experimental_label=0, comparison_label=1)

vector = TfidfVectorizer()
document_term_matrix_train = vector.fit_transform(combine_train)
document_term_matrix_test = vector.transform(combine_test)
classifier = MultinomialNB()
classifier.fit(document_term_matrix_train, combine_train_label)
predictor = classifier.predict(document_term_matrix_test)
accuracy = accuracy_score(combine_test_label, predictor)
print('This program accurately detects FriesWithThat\'s comments {}% of the time.'.format(accuracy*100))
