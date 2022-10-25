def reduce(arr):
    return "<%s>" % "".join(
        (reduce(e) for e in arr)) if type(arr) == list else "x"


def same_structure_as(original, other):
    return reduce(original) == reduce(other)


if __name__ == "__main__":
    print(reduce([]))
    print(reduce([[1, 2, 3], [], []]))
    print(reduce([[[[[]]]]]))