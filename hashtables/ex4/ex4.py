def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    cache = {}
    result = []
    for b in a:
        if -1*b in cache:
            if b > 0 and b not in result:
                result.append(b)
            elif b < 0 and -1*b not in result:
                result.append(-1*b)
        if b not in cache:
            cache[b] = b
    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
