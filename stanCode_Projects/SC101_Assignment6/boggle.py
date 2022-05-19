"""
File: boggle.py
Name: Wei
----------------------------------------
TODO:
"""

import time


# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'


# hint from Jerry: 變成 2D array []
def main():
    """
    TODO:
    """
    start = time.time()
    # find_match_1(get_input(), read_dictionary(), [], [], [], 0, 0, init_coord_creator([]))
    find_match(get_input(), read_dictionary())

    ####################
    #                  #
    #       TODO:      #
    #                  #
    ####################
    end = time.time()
    print('----------------------------------')
    print(f'The speed of your boggle algorithm: {end - start} seconds.')


def get_input():
    """
    :return: a list contain 4 sub-list compose of 4 input alphabets
    """
    lst = []
    is_true = True
    for i in range(1, 5):
        count = 0
        row = input(str(i) + ' row of letters:').lower()
        row_1 = row.split()
        if len(row_1) != 4:
            print('illegal input')
            break
        for ch in row_1:
            if ch.isalpha():
                count += 1
            else:
                print('illegal input')
                is_true = False
                break
        if is_true is False:  # once illegal input, the whole program break
            break
        elif count == 4:
            lst.append(row_1)
    return lst


def init_coord_creator(lst):
    """
    :param lst: an empty list to place initial coordinate
    :return: a list with 16 coordinate
    """
    for p in [0, 1, 2, 3]:
        for q in [0, 1, 2, 3]:
            if (p, q) not in lst:
                lst.append((p, q))
    return lst


def find_match_1(lst, dic, current_lst, used_lst, whole_lst, new_i, new_j, init_lst):
    """
    Current condition: This function failed to finish due to un-resolved technical problem...
    :param lst: a list contain 4 sub-list compose of 4 input alphabets
    :param dic: the list contains all words with longer 4 alphabets
    :param current_lst: the working list to find target word in recursion
    :param used_lst: the list record the alphabets that has been used
    :param whole_lst: the list record all the found works
    :param new_i: x(row)- coordinate of current alphabets
    :param new_j: y(col)- coordinate of current alphabets
    :param init_lst: the coordinate of 16 alphabets to begin with
    :return: whole list
    """
    is_first = True
    if len(current_lst) >= 4:
        str_current = "".join(current_lst)
        if str_current in dic:
            if str_current not in whole_lst:
                whole_lst.append(str_current)
                print('Found "' + str_current + '"')
    else:
        for k in range(-1, 2):
            for l in range(-1, 2):
                if current_lst == [] and is_first:
                    (new_i, new_j) = init_lst[0]
                    print(init_lst)
                    init_lst.remove((new_i, new_j))
                    # current_lst.append(lst[new_i][new_j])
                    # used_lst.append((new_i, new_j))
                    is_first = False
                if 4 > new_i+k >= 0 and 4 > new_j+l >= 0:
                    word = lst[new_i+k][new_j+l]
                    coord = (new_i + k, new_j + l)
                    if coord in used_lst:
                        pass
                    else:
                        new_i = new_i + k
                        new_j = new_j + l
                        used_lst.append(coord)
                        # Choose
                        current_lst.append(word)
                        # Explore
                        find_match_1(lst, dic, current_lst, used_lst, whole_lst, new_i, new_j, init_lst)
                        # Un-choose
                        current_lst.pop()
                        used_lst.remove(coord)
                        new_i = new_i - k
                        new_j = new_j - l
                        is_first = True

    return whole_lst


def find_match(lst, dic):
    """
    Comment: This function does not apply recursion method but at least get the right answer...
    :param lst: a list contain 4 sub-list compose of 4 input alphabets
    :param dic: the list contains all words with longer 4 alphabets
    :return: Print out the "whole list" and total number of words found
    """
    whole_lst = []
    for x in range(0, 4):
        for y in range(0, 4):
            for i in range(-1, 2):
                for j in range(-1, 2):
                    neighb_x = x + i
                    neighb_y = y + j
                    if neighb_x == x and neighb_y == y:
                        pass
                    elif 4 > neighb_x >= 0 and 4 > neighb_y >= 0:
                        sub_s = lst[x][y] + lst[neighb_x][neighb_y]
                        if has_prefix(sub_s):
                            # print(str(sub_s))
                            #  layer 3
                            for k in range(-1, 2):
                                for l in range(-1, 2):
                                    neighb_x_1 = neighb_x + k
                                    neighb_y_1 = neighb_y + l
                                    if neighb_x_1 == x and neighb_y_1 == y:
                                        pass
                                    elif neighb_x_1 == neighb_x and neighb_y_1 == neighb_y:
                                        pass
                                    elif 4 > neighb_x_1 >= 0 and 4 > neighb_y_1 >= 0:
                                        sub_s_1 = sub_s + lst[neighb_x_1][neighb_y_1]
                                        if has_prefix(sub_s_1):
                                            # print(sub_s_1)
                                            # layer 4
                                            for m in range(-1, 2):
                                                for n in range(-1, 2):
                                                    neighb_x_2 = neighb_x_1 + m
                                                    neighb_y_2 = neighb_y_1 + n
                                                    if neighb_x_2 == x and neighb_y_2 == y:
                                                        pass
                                                    elif neighb_x_2 == neighb_x_1 and neighb_y_2 == neighb_y_1:
                                                        pass
                                                    elif neighb_x_2 == neighb_x and neighb_y_2 == neighb_y:
                                                        pass
                                                    elif 4 > neighb_x_2 >= 0 and 4 > neighb_y_2 >= 0:
                                                        word = sub_s_1 + lst[neighb_x_2][neighb_y_2]
                                                        if word in dic:
                                                            if word in whole_lst:
                                                                pass
                                                            else:
                                                                whole_lst.append(word)
                                                                print('Found "' + word + '"')
                                                                if has_prefix(word):
                                                                    # layer 5
                                                                    for o in range(-1, 2):
                                                                        for p in range(-1, 2):
                                                                            neighb_x_3 = neighb_x_2 + o
                                                                            neighb_y_3 = neighb_y_2 + p
                                                                            if neighb_x_3 == x and neighb_y_3 == y:
                                                                                pass
                                                                            elif neighb_x_3 == neighb_x_1 and neighb_y_3 == neighb_y_1:
                                                                                pass
                                                                            elif neighb_x_3 == neighb_x and neighb_y_3 == neighb_y:
                                                                                pass
                                                                            elif 4 > neighb_x_3 >= 0 and 4 > neighb_y_3 >= 0:
                                                                                word_1 = word + lst[neighb_x_3][neighb_y_3]
                                                                                if word_1 in dic:
                                                                                    whole_lst.append(word_1)
                                                                                    print('Found "' + word_1 + '"')
    print("There are " + str(len(whole_lst)) + " words in total")


def read_dictionary():
    """
    This function reads file "dictionary.txt" stored in FILE
    and appends words in each line into a Python list
    """
    d = []
    with open(FILE, 'r') as f:
        for line in f:
            if len(line) >= 5:
                d.append(line.strip())
        return d


def has_prefix(sub_s):
    """
    Current
    :param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
    :return: (bool) If there is any words with prefix stored in sub_s
    """
    return has_prefix_helper(sub_s, read_dictionary())


def has_prefix_helper(sub_s, dic_lst):  # Return Boolean (True/False)
    for word in dic_lst:
        if word.startswith(sub_s) is True:
            return True
    return False


if __name__ == '__main__':
    main()
