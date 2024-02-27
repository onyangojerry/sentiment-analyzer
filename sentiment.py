# Jerry Onyango
# Assign7
# March 21, 2023
import fileinput


def get_file_count(filename):
    """
    iterates through file, updates number of words in a dictionary
    :param filename: file
    :return: dictionary
    """
    file = open(filename, "r")  # opens given file
    word_count = {}  # empty dictionary to be updated
    for line in file:  # iterates through the file for all lines
        for word in line.split():  # reaches all words in each line
            if word in word_count:
                word_count[word] += 1  # updates the dictionary
            else:
                word_count[word] = 1
    return word_count

    # file.close()  # closes the file


def counts_to_probs(dictionary, num):
    """
    creates new dictionary with keys divided by the number input
    :param dictionary: dictionary
    :param num: integer
    :return: dictionary
    """
    for word in dictionary:  # iterates through the dictionary
        dictionary[word] = dictionary[word] / num  # updates the value of each key of the dictionary
    return dictionary


def train_model(filename):
    """

    :param filename: file
    :return: dictionary
    """

    count = get_file_count(filename)

    file = open(filename, 'r')  # opens the file

    lines = 0
    for line in file:  # iterates through the file counting the lines
        lines += 1  # updates the number of lines in a file
    # print(lines)
    return counts_to_probs(count, lines)


def get_probability(dictionary, string):
    """
    calculates the probability
    :param dictionary: dictionary
    :param string: string(sentence)
    :return: float
    """
    separate = string.lower().split()  # lower cases and turns into a list the string
    # print(separate)
    prob = 1  # probability to be updated
    for word in separate:  # iterates through the new list formed
        if word in dictionary:  # checks for the words i the new list from the dictionary
            prob *= dictionary[word]  # updates the probability calculation value
        else:
            prob *= 1 / 11000  # updates when word not in the dictionary

    return prob  # calculated probability


def classify(string, pos_dict, neg_dict):
    """
    compares probability values
    :param string: string
    :param pos_dict: float
    :param neg_dict: float
    :return: string
    """
    posit = get_probability(pos_dict, string)  # calculates probability value for positive
    # print(posit)
    negati = get_probability(neg_dict, string)  # calculates probability value for negative
    # print(negati)

    if posit >= negati:
        return 'positive'
    else:
        return 'negative'


def sentiment_analyzer(pos_file, neg_file):
    """
    checks for positive and negative sentences after analyses
    :param pos_file: (str) positive file
    :param neg_file: (str) negative file
    :return: string
    """
    string = input("Enter your sentence: ")
    while string != "":
        case1 = train_model(pos_file)
        case2 = train_model(neg_file)
        comment = classify(string, case1, case2)
        print(comment)
        string = input("Enter your sentence: ")

    return


def get_accuracy(pos_test, neg_test, pos_train, neg_train):
    """

    :param pos_test: (str) pos test file
    :param neg_test: (str) neg test file
    :param pos_train: (str) pos train file
    :param neg_train: (str) neg train file
    :return: (none)
    """

    train_pos = train_model(pos_train)  # yields a dictionary with trained data, value
    train_neg = train_model(neg_train)  # yields a dictionary with trained data

    pos_file = open(pos_test, "r")  # opens file
    neg_file = open(neg_test, "r")  # opens file

    pos_test = 0
    pos_total = 0
    neg_test = 0
    neg_total = 0

    for line in pos_file:  # iterates through positive file
        if classify(line, train_pos, train_neg) == "positive:":
            pos_test += 1  # updates the positive statements
        pos_total += 1  # updates the total positive value

    for line in neg_file:  # iterates through the negative file
        if classify(line, train_pos, train_neg) == "negative:":
            neg_test += 1  # updates the negative statements
        neg_total += 1  # updates the total negative value

    print("Positive accuracy: " + str(pos_test / pos_total))
    print("Negative accuracy: " + str(neg_test / neg_total))
    print("Total accuracy: " + str((pos_test + neg_test)/(pos_total + neg_total)))

    pos_file.close()
    neg_file.close()


# # ________________________________________________________________________
#
"""
Negative accuracy: 0.788829197988292
Total accuracy: 0.9185339185339185

Positive accuracy for the test examples turned out as 96% a \n
reliable value. However, the negative accuracy value at 71% isn't \n 
 as reliable. The total accuracy for both positive and negative test \n
examples was 91% which is acceptable. Negative accuracy is significantly lower \n 
 than the positive accuracy, possibly caused by mixed positive and negative statements. 

For mix of both positive and negative words, the model is mixed up \n 
and focuses on the connotation of the words. The strong negative connotation 
of a word compared to other words has a big influence.

"""
