# Read text from a file, and count the occurrence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

from string import punctuation

def read_file_content(filename):
    with open(filename) as f:
        contents = f.read()
        return contents


def count_words():
    text = read_file_content("story.txt")

    # removing punctuations
    for punct in punctuation:
        text = text.replace(punct, "")

    # converting all the string to lowercase
    lowercase_text = text.lower()

    new_text = lowercase_text.split()

    dic = {}
    for i in new_text:
        word_count = new_text.count(i)
        dic[i] = word_count

    return dic


print(count_words())


