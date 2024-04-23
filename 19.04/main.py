
def Task(n):

    a = 0
    variants =[]

    if n > 0:
        variant = ['(', 1, 1]
        
        variants.append(variant)
        
        while a == 0:
            a = 1

            #print(f'\n{variants}\n')

            for v in variants:
                if v[1] < n and v[2] > 0:
                    a = 0
                    variants.append([v[0] + ')', v[1], v[2] - 1])
                    v[0] += '('
                    v[1] += 1
                    v[2] += 1
                elif v[1] == n and v[2] > 0:
                    a = 0
                    v[0] += ')'
                    v[2] -= 1
                elif v[1] < n and v[2] == 0:
                    a = 0
                    v[0] += '('
                    v[1] += 1
                    v[2] += 1
    else:
        return []
    for i in variants:
        #print(i[0])
        variants[variants.index(i)] = i[0]
    return variants

print(Task(3))