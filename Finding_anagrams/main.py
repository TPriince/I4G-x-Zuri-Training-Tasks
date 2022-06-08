# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


from pickle import GLOBAL


def find_anagram(word, anagram):

    # converting both strings to lowercase
    first_word = word.lower()
    second_word = anagram.lower()

    # getting rid of whitespaces
    first_word = first_word.replace(" ", "")
    second_word = second_word.replace(" ", "")
    
    first_word = sorted(first_word)
    second_word = sorted(second_word)

    if first_word == second_word:
        return True

    else:
        return False

print(find_anagram("hello", "check"))
print(find_anagram("below", "elbow"))

