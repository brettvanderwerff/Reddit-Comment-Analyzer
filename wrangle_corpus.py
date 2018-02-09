from nltk import sent_tokenize
import random

def open_corpus(file_name):
    '''Function opens corpus of comments from the disk.
    '''
    with open(file_name, 'r', encoding='utf-8') as read_obj:
        corpus = read_obj.read()
    return corpus

def tokenize_corpus(corpus):
    '''Function takes inputted corpus and divides it into a lists of sentences. The function then randomizes the order
    of the list of sentences.
    '''
    tokenized_corpus = sent_tokenize(corpus)
    shuffled_corpus = random.sample(tokenized_corpus, len(tokenized_corpus))
    return shuffled_corpus


def split_test_train(shuffled_corpus, label):
    '''Function divides 2/3 of the inputted corpus into a training set and 1/3 into a testing set. an integer
    label is also assigned to the corpus based on user input. Function returns both the training and testing set along
    with a corresponding list of their labels.
    '''
    shuffled_corpus_train = shuffled_corpus[0:round(len(shuffled_corpus) * .67)]
    shuffled_corpus_train_label = [int(label)] * len(shuffled_corpus_train)
    shuffled_corpus_test = shuffled_corpus[round(len(shuffled_corpus) * .67):]
    shuffled_corpus_test_label = [int(label)] * len(shuffled_corpus_test)
    return shuffled_corpus_train, shuffled_corpus_train_label, shuffled_corpus_test, shuffled_corpus_test_label

def combine_data(experimental_train, comparison_train, experimental_train_label, comparison_train_label,\
                 experimental_test, comparison_test, experimental_test_label, comparison_test_label):
    '''Function combines the experimental and comparison corpus into a single list. Function also
    combines the experimental and comparison corpus label lists into a single list. This is needed for downstream 
    analysis.
    '''
    combine_train = experimental_train + comparison_train
    combine_train_label = experimental_train_label + comparison_train_label
    combine_test = experimental_test + comparison_test
    combine_test_label = experimental_test_label + comparison_test_label
    return combine_train, combine_train_label, combine_test, combine_test_label

def run(experimental_file, comparison_file, experimental_label, comparison_label):
    '''Function runs the script.
    '''
    experimental_corpus = open_corpus(experimental_file)
    comparison_corpus = open_corpus(comparison_file)
    experimental_train, experimental_train_label, experimental_test, experimental_test_label\
        = split_test_train(experimental_corpus, experimental_label)
    comparison_train, comparison_train_label, comparison_test, comparison_test_label\
        = split_test_train(comparison_corpus, comparison_label)
    combine_train, combine_train_label, combine_test, combine_test_label =\
        combine_data(experimental_train, comparison_train, experimental_train_label, comparison_train_label,\
                     experimental_test, comparison_test, experimental_test_label, comparison_test_label)
    return combine_train, combine_train_label, combine_test, combine_test_label
