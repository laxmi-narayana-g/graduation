
def graduation_ceremony(day):
    """
    This method is used to calculate the probability of a student not attending the graduation ceremony.
    :param day: number of days.
    :return: string of The result.(probability of missing graduation ceremony / number of ways to attend classes)
    """
    result = ""
    loop_starting = 4
    if day:
        if day < loop_starting:
            result = str(2 ** (day - 1)) + '/' + str(2 ** day)
        else:
            a = 2
            aa = 1
            aaa = 1
            p = 4
            count = 8
            for _ in range(loop_starting, day + 1):
                temp = aaa
                aaa = aa
                aa = a
                a = p
                p = count
                count = (count) * 2 - temp
            result = str(aaa + aa + a) + '/' + str(count)
    return result


if __name__ == '__main__':
    n = input("Enter Number Of Days::")
    try:
        res = graduation_ceremony(int(n))
        print("for {} days : {}".format(n, res))
    except:
        print("Please Enter A Valid Value..")

# VARIABLE EXPLANATION.
# a -> ONE absent at the end.
# aa -> Continuos TWO absents at the end.
# aaa -> Continuos THREE absents at the end.
# p -> Possible cases to attend the ceremony.
# temp -> Number of combinations not included in total. (continuos absent for 4 days.)
# count -> Number of ways to attend the classes.
