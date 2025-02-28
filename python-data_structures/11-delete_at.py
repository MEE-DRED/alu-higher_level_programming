#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if idx < 0 or idx >= len(my_list):
        return my_list
                    
    # Create a new list by skipping the element at index idx
    new_list = []
    for i in range(len(my_list)):
        if i != idx:
            new_list.append(my_list[i])
                                                            
    # Clear the original list and extend it with the new list
    my_list.clear()
    my_list.extend(new_list)
                                                                            
    return my_list
                                                                            
