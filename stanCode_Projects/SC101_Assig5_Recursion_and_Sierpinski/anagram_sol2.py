"""
File: anagram.py
Name: Wei
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

import time                   # This file allows you to calculate the speed of your algorithm

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop


def main():
    """
    TODO:
    """

    start = time.time()
    print('Welcome to stanCode"Anagram Generator"(or -1 to quit)')
    s = input(str("Find anagrams for:"))
    # sub = input(str('Sub-text you are searching?'))
    find_anagrams(s)

    # has_prefix(sub)
    ####################
    #                  #
    #       TODO:      #
    #                  #
    ####################
    end = time.time()
    print('----------------------------------')
    print(f'The speed of your anagram algorithm: {end-start} seconds.')


def read_dictionary():
    with open(FILE, 'r') as f:
        lst = []
        for line in f:
            line_strip = line.strip()
            lst.append(line_strip)
        return lst


def find_anagrams(s):
    """
    :param s: The word as input
    :return:
    """
    find_anagrams_helper(s, [], read_dictionary(), 0)




def find_anagrams_helper(s, current_lst, dic_lst, current_count):
    print('Searching...')
    for word in dic_lst[current_count:]:  # To go through all dictionary(dic_lst)
        current_count += 1  # to record the progress running through dic_lst
        if current_count == len(dic_lst):  # base case (全部dic跑完)
            print(str(len(current_lst))+' anagrams:' + str(current_lst))
            print(current_count)
            print(len(dic_lst))
            break  # should be end, but 為什麼無法break?
        else:
            if len(s) == len(word):  # check if the length the same
                word_lst = []
                for k in range(len(word)):  # eg. word: apple
                    ch_word = word[k]  # eg. a p p l e
                    word_lst.append(ch_word)  # eg. [a, p, p, l, e]
                count = 0
                for j in range(len(s)):  # eg. s:app
                    ch_1 = s[j]  # eg.s[0] = a
                    if ch_1 in word_lst:  # if a in [a, p, p, l, e]
                        count += 1
                        word_lst.remove(ch_1)  # take out the character in case of repeatedly counting [p, p, l, e]
                        if count == len(s):
                            #  Choose
                            current_lst.append(word)
                            print('Found: '+word)
                            #  Explore
                            find_anagrams_helper(s, current_lst, dic_lst, current_count)
                    else:
                        break

















def has_prefix(sub_s):
    """
    :param sub_s: The sub word for searching
    :return: Return Boolean
    """
    return has_prefix_helper(sub_s, read_dictionary())



def has_prefix_helper(sub_s, dic_lst):     # Return Boolean (True/False)
    for word in dic_lst:
        if word.startswith(sub_s) is True:
            return True
    return False











if __name__ == '__main__':
    main()
