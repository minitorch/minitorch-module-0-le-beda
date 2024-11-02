"""Collection of the core mathematical operators used throughout the code base."""

import math

# ## Task 0.1
from typing import Callable, Iterable

#
# Implementation of a prelude of elementary functions.

# Mathematical functions:
# - mul
# - id
# - add
# - neg
# - lt
# - eq
# - max
# - is_close
# - sigmoid
# - relu
# - log
# - exp
# - log_back
# - inv
# - inv_back
# - relu_back
#
# For sigmoid calculate as:
# $f(x) =  \frac{1.0}{(1.0 + e^{-x})}$ if x >=0 else $\frac{e^x}{(1.0 + e^{x})}$
# For is_close:
# $f(x) = |x - y| < 1e-2$


# TODO: Implement for Task 0.1.
def mul(a: float, b: float) -> float:
    """Multiplies two numbers"""
    return a * b


def id(a: float) -> float:
    """Returns the input unchanged"""
    return a


def add(a: float, b: float) -> float:
    """Adds two numbers"""
    return a + b


def neg(a: float) -> float:
    """Negates a number"""
    return -a


def lt(a: float, b: float) -> bool:
    """Checks if one number is less than another"""
    return a < b


def eq(a: float, b: float) -> bool:
    """Checks if two numbers are equal"""
    return a == b


def max(a: float, b: float) -> float:
    """Returns the larger of two numbers"""
    if lt(a, b):
        return b
    return a


def is_close(a: float, b: float) -> bool:
    """Checks if two numbers are close in value"""
    return abs(a - b) < 1e-2


def sigmoid(a: float) -> float:
    """Calculates the sigmoid function"""
    if lt(0, a):
        return 1.0 / (1.0 + exp(-a))
    return exp(a) / (1.0 + exp(a))


def relu(a: float) -> float:
    """Applies the ReLU activation function"""
    return max(0, a)


def log(a: float) -> float:
    """Calculates the natural logarith"""
    return math.log(a)


def exp(a: float) -> float:
    """Calculates the exponential function"""
    return math.exp(a)


def inv(a: float) -> float:
    """Calculates the reciprocal"""
    return 1 / a


def log_back(a: float, b: float) -> float:
    """Computes the derivative of log times a second arg"""
    return b / a


def inv_back(a: float, b: float) -> float:
    """Computes the derivative of reciprocal times a second arg"""
    return -b / (a**2)


def relu_back(a: float, b: float) -> float:
    """Computes the derivative of ReLU times a second arg"""
    if lt(0, a):
        return b
    return 0


# ## Task 0.3

# Small practice library of elementary higher-order functions.

# Implement the following core functions
# - map
# - zipWith
# - reduce
#
# Use these to implement
# - negList : negate a list
# - addLists : add two lists together
# - sum: sum lists
# - prod: take the product of lists


# TODO: Implement for Task 0.3.
def map(fn: Callable[[float], float], ls: Iterable[float]) -> Iterable[float]:
    """Higher-order function that applies a given function to each element of an iterable"""
    ret = []
    for x in ls:
        ret.append(fn(x))
    return ret


def zipWith(
    fn: Callable[[float, float], float], ls1: Iterable[float], ls2: Iterable[float]
) -> Iterable[float]:
    """Higher-order function that combines elements from two iterables using a given function"""
    ls2 = iter(ls2)
    ret = []
    for x1 in ls1:
        x2 = next(ls2)
        ret.append(fn(x1, x2))
    return ret


def reduce(fn: Callable[[float, float], float], ls: Iterable[float]) -> float:
    """Higher-order function that reduces an iterable to a single value using a given function"""
    if ls == []:
        return 0

    ls = iter(ls)
    ret = next(ls)
    for x in ls:
        ret = fn(ret, x)
    return ret


def negList(ls: Iterable[float]) -> Iterable[float]:
    """Negate all elements in a list using"""
    return map(neg, ls)


def addLists(ls1: Iterable[float], ls2: Iterable[float]) -> Iterable[float]:
    """Add corresponding elements from two lists using zipWith"""
    return zipWith(add, ls1, ls2)


def sum(ls: Iterable[float]) -> float:
    """Sum all elements in a list using reduce"""
    return reduce(add, ls)


def prod(ls: Iterable[float]) -> float:
    """Calculate the product of all elements in a list using reduce"""
    return reduce(mul, ls)
