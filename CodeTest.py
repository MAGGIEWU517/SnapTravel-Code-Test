# Create database
ndic = {
    'Toronto': [('A', 100.00), ('D', 100.00)],
    'North York': [('B', 250)],
    'Waterloo': [('C', 19.99)],
    'Kitchener': [('F', 25), ('F', 24), ('F', 25)]
}

# Create database for customer selection
qdic = {
    'Toronto': 1,
    'North York': 2,
    'Waterloo': 8,
    'Kitchener': 10
}


def solution(n, q):
    # n is database
    # q is customer selection
    # base cases:
    # n is empty
    if not n:
        return 'Invalid Database'

    # q is customer selection based on n
    # q can be no selection --> empty, return all possible prices
    output = []
    if not q:
        for t in n.keys():
            price = []
            for s in n[t]:
                p = s[1]
                price.append(p)
                price.sort()
            output.append(price)
    else:
        # q is not empty
        for t in q.keys():
            price = []
            for s in n[t]:
                if s[0] == 'A':
                    p = s[1] * 1.5 if q[t] == 1 else s[1]
                elif s[0] == 'B':
                    p = 'None' if q[t] < 3 else s[1]
                elif s[0] == 'C':
                    p = s[1] * 0.9 if q[t] > 7 else s[1]
                elif s[0] == 'D':
                    p = s[1] * 1.1 if q[t] < 7 else s[1]
                else:
                    p = s[1]

                # p has two types : if p is a number, we need to save two decimal
                if p != 'None':
                    p = format(p, '.2f')
                price.append(p)
                price.sort()
            output.append(price)

    return output


print(solution(ndic, {}))
print(solution(ndic, qdic))


print(solution(ndic, qdic))