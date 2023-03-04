# def calculate_total(exp):
#     total = 0
#     for item in exp:
#         total = total+item
#     return total


# tom_exp_list = [2100, 3400, 2500]
# joe_exp_list = [200, 500, 700]


# toms_total = calculate_total(tom_exp_list)
# joes_total = calculate_total(joe_exp_list)

# print("Toms total", toms_total)
# print("joes total", joes_total)


total = 0


def sum(a, b):
    # if we want to give a default value then, sum(a=0,b=0)
    # if default value given then it will run also if a or b is not called in function

    print("a:", a)
    print("b", b)

    total = a+b
    print("total inside function:", total)
    return total


n = sum(5, 6)
# we can exchange position of variable by name calling
# sum(b=5,a=6)
print(n)
