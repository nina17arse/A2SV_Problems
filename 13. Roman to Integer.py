 values = list(map(lambda x: roman_values[x], s))

    result = 0
    n = len(values)

    for i in range(n):
        if i < n - 1 and values[i] < values[i + 1]:
            result -= values[i]
        else:
            result += values[i]

    return result
