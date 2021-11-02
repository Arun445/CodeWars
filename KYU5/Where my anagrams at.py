def check_if_anagram(word1, word2):
    for letter in word2:
        if letter in word1:
            word1.remove(letter)
        else:
            return False
    return True


def anagrams(word, words):
    wordsai = []
    word_list = [sorted(list(word1)) for word1 in words]
    word = sorted(list(word))
    for word1 in word_list:
        if word1 == word:
            wordsai.append(word1)

    return(wordsai)
