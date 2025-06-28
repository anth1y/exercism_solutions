from functools import reduce

def append(list1, list2):
    for item in list2:
        list1.append(item)
    return list1

def concat(lists):
    flattened_lists = [item for sublist in lists for item in sublist]
    return flattened_lists


def filter(function, list):
    list_cmp = [lst for lst in list if function(lst)]
    return list_cmp

def length(list):
    lng_lst = len(list)
    return lng_lst


def map(function, list):
    result = []
    for item in list:
        transformed_item = function(item)
        result.append(transformed_item)
    return result
      
     
def foldl(function, list, initial):
    return reduce(function, list, initial)


def foldr(function, iterable, initial):
    reversed_list = reversed(list(iterable))
    return reduce(function, reversed_list, initial )
        
        


def reverse(list):
    reversed_list = list[::-1]
    return reversed_list
      