"""
Author: Kvin2K
Date: 06/01/2022
list to dictionary, search dictionary
"""
def list_to_dict(l1,l2):
    L1 = ['a','b','c','d']
    L2 = [1,2,3,4]
    d = dict(zip(L1,L2))
    d

def search_dict(d, value):
    d = {'key1': 'aaa', 'key2': 'aaa', 'key3': 'bbb'}
    value = d['key1']
    print(value)

""" 
https://www.tutorialspoint.com/How-to-create-Python-dictionary-from-list-of-keys-and-values
https://github.com/nkmk/python-snippets/blob/3c58602bfb74f604a9d33ecac5a0ae6a8002fb63/notebook/dict_get_key_from_value.py#L1-L5
"""