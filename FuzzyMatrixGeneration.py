"""
generate a fuzzy matrix for each divided rain
"""

import os

def test_a(path:str):
    """
    main func to generate fuzzy matrix
    :param path: The path of divided individual rainfall txt file
    :return:
    """
    f_1 = open(f"{path}", 'r', encoding="UTF-8")
    count = 0
    #get rainfall depth from the name of dat file
    path = path.strip(".dat")
    path_1 = path.split("rainfall depth")
    totalRainFall = float(path_1[1])
    #get start/end time from the name of dat file
    path_2 = path_1[0].strip(' - ')
    path_3 = path_2.split('chen\\') #旧为5mm
    path_name = path_3[1]
    # Create an empty list to store the fuzzy matrix of the rainfall
    rainFall_List = []
    # read current rainfall
    for line in f_1:
        line = line.strip('\n')
        line_1 = line.split('\t')
        rainFall = float(line_1[1])
        rainFall_List.append(rainFall)

        count += 1
    # if rainfall duration greater than the number of equidistant periods
    if count >= n:

        # get the time of equidistant period
        re_1 = int(count / n)
        re_2 = count % n
        result_1 = function_1(rainFall_List, re_1, re_2, totalRainFall)
        # convert list `result_1` to string
        result_2 = '\t'.join(result_1)
        # output `result_2` to file
        f_2 = open(os.path.join(file,"fuzzyMatrixOutput\\result.txt"),'a',encoding="UTF-8")
        f_2.write(path_name)
        f_2.write('\t')
        f_2.write(result_2)
        f_2.write('\n')
        f_2.flush()
        f_2.close()

def function_1 (the_list, re_1, re_2, totalRainFall):
    """
    :param the_list:  the list that only contains rainfall data
    :param re_1: The number of rainfall data contained in each period
    :param re_2: 降雨个数的小数部分
    :param n: the number of equidistant periods from keyboard
    :param totalRainFall: total rainfall depth
    :return: fuzzy matrix
    """
    alist = []
    i = 0
    while the_list:
        # get the sum of first re_1 period
        if i < re_2:
            the_sum = sum(the_list[:re_1 + 1])
            the_percentage = '{:.2%}'.format(the_sum/totalRainFall)
            alist.append(the_percentage)
            the_list = the_list[re_1 + 1:]
            i += 1
        else:
            the_sum = sum(the_list[:re_1])
            the_percentage = '{:.2%}'.format(the_sum / totalRainFall)
            alist.append(the_percentage)
            the_list = the_list[re_1:]
            i += 1

    return alist


# main func
# read the folder which stores divided rainfall
file = r''
i = input(f"Please enter the number of equidistant periods:")
n = int(i)

for root, dirs, files in os.walk(file):
    if root != file:
        break
    for file in files:
        path: str = os.path.join(root, file)
        test_a(path)



