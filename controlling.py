from interface import get_operation, get_element_search, get_edit, get_dict, get_edit_2, print_result
from add_record import add_record
from search import search
from log import get_log
from edit_record import edit

def buttun_click():
    num_oper = get_operation()
    if num_oper == 1:
        new_dict = get_dict()
        add_record(new_dict)
        get_log(num_oper)
        # print_result()
    elif num_oper == 2:
        element_edit = get_edit()
        new_element = get_edit_2()
        edit(element_edit, new_element)
        # print_result()
    elif num_oper == 3:
        element = get_element_search()
        search(element)
        # print_result()






