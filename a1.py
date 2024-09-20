"""Assignment 1

Fill in the following function skeletons - descriptions are provided in 
the docstring (the triple quote thing at the top of each function)

Some assert statements have been provided - write more of them to test your code!

The `raise NotImplementedError(...)`s are placeholders to help you not skip implementing
a function. They should be removed and replaced with your solution.

This portion of the assignment will not be graded, but this gives you some problems to 
check, if you do not complete the generative AI portion of the assignment.
"""

from typing import List, TypeVar


def absolute(n: int) -> int:
    # if n < 0:
    #     return n*-1
    # else:
    #     return n
    return n*-1 if n < 0 else n


def factorial(n: int) -> int:
    result = 1
    while n > 1:
        result*=n
        n-= 1
    return result


T = TypeVar("T")


def every_other(lst: List[T]) -> List[T]:
     return lst[::2]


def sum_list(lst: List[int]) -> int:
    sum = 0
    for sumN in lst:
        sum += sumN
    return sum


def mean(lst: List[int]) -> float:
    mean = 0
    sum = 0
    items = 0
    for sumN in lst:
        sum += sumN
        items+=1
    mean = sum/items
    return mean   


def median(lst: List[int]) -> float:
    numLe = len(lst)
    middle = numLe // 2

    if numLe % 2 == 0:
        return (lst[middle-1]+lst[middle])/2
    else:
        return lst[middle]
    


def duck_duck_goose(lst: List[str]) -> List[str]:
    

    
    """Given an list of names (strings), play 'duck duck goose' with it, knocking out
    every third name (wrapping around) until only two names are left.

    In other words, when you hit the end of the list, wrap around and keep counting from
    where you were.

    For example, if given this list ['Nathan', 'Sasha', 'Sara', 'Jennie'], you'd first
    knock out Sara. Then first 'duck' on Jennie, wrap around to 'duck' on Nathan and
    'goose' on Sasha - knocking him out and leaving only Nathan and Jennie.

    You may assume the list has 3+ names to start

    Args:
        lst - a list of names (strings)

    Returns:
        the resulting list after playing duck duck goose
    """
    raise NotImplementedError("duck_duck_goose")


# this line causes the nested code to be skipped if the file is imported instead of run
if __name__ == "__main__":
    assert absolute(1) == 1, "absolute of 1 failed"
    assert absolute(-1) == 1, "absolute of -1 failed"
    assert factorial(4) == 24, "factorial of 4 failed"
    assert every_other([1, 2, 3, 4, 5]) == [
        1,
        3,
        5,
    ], "every_other of [1,2,3,4,5] failed"
    assert sum_list([1, 2, 3]) == 6, "sum_list of [1,2,3] failed"
    assert mean([1, 2, 3, 4, 5]) == 3, "mean of [1,2,3,4,5] failed"
    assert median([1, 2, 3, 4, 5]) == 3, "median of [1,2,3,4,5] failed"

    names = ["roscoe", "kim", "woz", "solin", "law", "remess"]
    assert duck_duck_goose(names) == ["roscoe", "law"]

    print("All tests passed!")