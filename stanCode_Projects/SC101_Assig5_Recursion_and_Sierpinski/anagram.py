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
    TODO: Start counting the time taken and execute the anagrams finding function
    """

    start = time.time()
    print('Welcome to stanCode"Anagram Generator"(or -1 to quit)')
    s = input(str("Find anagrams for:"))
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


def read_dictionary(len_s):
    with open(FILE, 'r') as f:
        lst = []
        for line in f:
            line_strip = line.strip()
            if len(line_strip) == len_s:
                lst.append(line_strip)
        print(lst)
        return lst



def find_anagrams(s):
    """
    :param s: The word as input
    :return: the list of anagrams and print the summary
    """
    whole_lst = find_anagrams_helper(s, read_dictionary(len(s)), [], [])
    print(str(len(whole_lst)) + ' anagrams:' + str(whole_lst))


def find_anagrams_helper(s, dic_lst, current_lst, whole_lst):
    """
    :param s: The input word
    :param dic_lst: the list contains all words in dic.text file
    :param current_lst: the working list doing back tracking
    :param whole_lst: the list to record the found anagrams
    :return: the list of all found anagrams when the program finished
    """
    if len(current_lst) == len(s):
        str_current = "".join(current_lst)
        if str_current in dic_lst:
            if str_current not in whole_lst:
                whole_lst.append(str_current)
                print('Found: ' + str_current)
                print('Searching...')
    else:
        word_lst_backup = []
        for j in s:
            word_lst_backup.append(j)
        for i in range(len(current_lst)):
            ch = current_lst[i]
            if ch in word_lst_backup:
                word_lst_backup.remove(ch)
        for word in word_lst_backup:
            # Choose
            current_lst.append(word)
            # Explore
            find_anagrams_helper(s, dic_lst, current_lst, whole_lst)
            # Un-choose
            current_lst.pop()

    return whole_lst



def has_prefix(sub_s):
    """
    :param sub_s: The sub word for searching
    :return: Return Boolean
    """
    return has_prefix_helper(sub_s, read_dictionary(len(sub_s)))



def has_prefix_helper(sub_s, dic_lst):     # Return Boolean (True/False)
    for word in dic_lst:
        if word.startswith(sub_s) is True:
            return True
    return False











if __name__ == '__main__':
    main()
