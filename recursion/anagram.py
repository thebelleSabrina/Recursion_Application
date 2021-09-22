"""
File: anagram.py
Name: Sabrina Wang
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

lst = []


def main():
    """
    TODO:
    """
    print('Welcome to stanCode "Anagram Generator"(or -1 to quit)')
    read_dictionary()
    while True:
        word = input('Find anagrams for: ')
        start = time.time()
        if word == str(-1):
            break
        find_anagrams(word)
    end = time.time()
    print('----------------------------------')
    print(f'The speed of your anagram algorithm: {end-start} seconds.')


def read_dictionary():
    with open(FILE, 'r') as f:
        for line in f:
            word = line.strip('\n')
            lst.append(word)
    return lst


def find_anagrams(s):
    """
    :param s: the word input by user
    :return: all the anagram of the word
    """
    total = []
    helper(s, [], [], total)
    print(f"{len(total)} anagrams: {total}")


def helper(s, cur_lst, used_index, total):
    if len(cur_lst) == len(s):  # base-case
        new_lst = ''  # turns list into string
        for each in cur_lst:
            new_lst += each
        if new_lst in lst and new_lst not in total:
            if new_lst not in cur_lst:
                print('Searching...')
                print('Found:' + new_lst)
                total.append(new_lst)
    else:
        for i in range(len(s)):
            if i not in used_index:  # avoids the same character appear in the same location
                check_lst = ''
                for each in cur_lst:
                    check_lst += each
                if has_prefix(check_lst):  # makes the code run faster through the new function
                    # choose
                    used_index.append(i)  # list for index
                    cur_lst.append(s[i])   # list for character
                    # explore
                    helper(s, cur_lst, used_index, total)
                    # un-choose
                    used_index.pop()
                    cur_lst.pop()


def has_prefix(sub_s):
    """
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:return: (bool) If there is any words with prefix stored in sub_s
    """
    vocab_list = lst
    for vocab in vocab_list:
        if vocab.startswith(sub_s):
            return True
    return False


if __name__ == '__main__':
    main()
