from operator import pos


def fun(arr):
    negative = 0
    positive = 0
    zero = 0
    for i in arr:
        if i > 0:
            positive = positive + 1
        elif i < 0:
            negative = negative + 1
        else:
            zero = zero + 1

    print("{:.6f}".format(positive/len(arr)))
    print("{:.6f}".format(negative/len(arr)))
    print("{:.6f}".format(zero/len(arr)))

arr = [1, 2, 0, -1, -2]
fun(arr)