# Given a list return a list that includes the product of all
# numbers in list besides that the specific index


def list_product(l):

    new = []

    for i in range(len(l)):
        holder = l[i]
        l[i] = 1
        total = 1
        for element in l:
            total *= element
        new.append(total)
        l[i] = holder

    return new

print(list_product([1, 2, 3, 4, 5]))