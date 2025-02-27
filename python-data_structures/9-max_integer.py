#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    # Ensure both tuples have at least two elements, filling missing values with 0
    a = (tuple_a + (0, 0))[:2]
    b = (tuple_b + (0, 0))[:2]
                    
    # Add corresponding elements from both tuples
    return (a[0] + b[0], a[1] + b[1])

def multiple_returns(sentence):
    if len(sentence) == 0:
        return (0, None)
    return (len(sentence), sentence[0])

def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    max_val = my_list[0]
    for num in my_list:
         if num > max_val:
            max_val = num
    return max_val

if __name__ == "__main__":
    tuple_a = (1, 89)
    tuple_b = (88, 11)
    new_tuple = add_tuple(tuple_a, tuple_b)
    print(new_tuple)

    print(add_tuple(tuple_a, (1,)))
    print(add_tuple(tuple_a, ()))

    sentence = "At school, I learnt C!"
    length, first = multiple_returns(sentence)
    print("Length: {:d} - First character: {}".format(length, first))

    my_list = [1, 90, 2, 13, 34, 5, -13, 3]
    max_value = max_integer(my_list)
    print("Max: {}".format(max_value))
