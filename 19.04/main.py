
def Task(n):

    if 1 <= n <= 8:
        result = []

        var_1 = '(' * n + ')' * n
        result.append(var_1)

        var_2 = '()' * n
        result.append(var_2)

        if n - 1 != 0:
            var_3 = '(' * (n-1) + ')' 





        print(result)
    else:
        print('Чило должно быть в диапозоне от 1 до 8 включительно!!!')

Task(3)