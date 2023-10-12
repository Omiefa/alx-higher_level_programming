#!/usr/bin/python3

def search_replace(my_list, search, replace):
    def find_search(item):
        return item if item != search else replace
    return list(map(find_search, my_list))
