def reverse_dic(dic: 'dict[str, str]'):

    result: 'dict[str, str]' = {}
    for key, value in dic.items():
        result[value] = key
    return result
