#Algorithms
from Sorting import mergesort

#! Greedy algorithms
def sort_dict(diction):
    dict_lst = []
    for key in diction.keys():
        dict_lst.append(diction[key][1])
        
    dict_lst = mergesort(dict_lst)
    new_dict = {}
    for ele in dict_lst:
        for key, val in diction.items():
            if val[1] == ele:
                new_dict[key] = val
    return new_dict
            
#*Activity selection
def activ_sel(diction):
    dict_lst = []
    for key, val in diction.items():
        if len(dict_lst) == 0:
            dict_lst.append(key)
            continue
        if diction[dict_lst[-1]][1] <= diction[key][0]:
            dict_lst.append(key)
    print("Acivities done by a person :", len(dict_lst))
    return dict_lst



if __name__ == '__main__':
    diction = {
        "A1" : (0, 6),
        "A2" : (3, 4),
        "A3" : (1, 2),
        "A4" : (5, 9),
        "A5" : (5, 7),
        "A6" : (8, 9),
    }
    new_dict = sort_dict(diction)
    print(new_dict)
    print(activ_sel(new_dict))