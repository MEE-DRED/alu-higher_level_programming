#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    # Ensure both tuples have at least two elements, filling missing values with 0
    a = (tuple_a + (0, 0))[:2]
    b = (tuple_b + (0, 0))[:2]
                    
    # Add corresponding elements from both tuples
    return (a[0] + b[0], a[1] + b[1])

if __name__ == "__main__":
    tuple_a = (1, 89)
    tuple_b = (88, 11)
    new_tuple = add_tuple(tuple_a, tuple_b)
    print(new_tuple)

    print(add_tuple(tuple_a, (1,)))
    print(add_tuple(tuple_a, ()))

