def shift_right(lst):
    try:
        return [lst[-1]] + lst[:-1]
    except IndexError:
        return lst


list = [1, 2, 3, 4, 5, 6, 7, 8]
oddsubjlist = list[0:][::2]
evensubjlist = list[1:][::2]
size = len(evensubjlist)
for i in range(1, size):
    evensubjlist = shift_right(evensubjlist)
evensubjlist1 = evensubjlist
evensubjlist2 = shift_right(evensubjlist1)
evensubjlist3 = shift_right(evensubjlist2)
evensubjlist4 = shift_right(evensubjlist3)
print(evensubjlist1)
print(evensubjlist2)
print(evensubjlist3)
print(evensubjlist4)

newsubjlist1 = []
newsubjlist2 = []
newsubjlist3 = []
newsubjlist4 = []
for i in range(1, size+1):
    newsubjlist1.append(oddsubjlist[i-1])
    newsubjlist1.append(evensubjlist1[i-1])
    newsubjlist2.append(oddsubjlist[i - 1])
    newsubjlist2.append(evensubjlist2[i - 1])
    newsubjlist3.append(evensubjlist3[i - 1])
    newsubjlist3.append(oddsubjlist[i - 1])
    newsubjlist4.append(oddsubjlist[i - 1])
    newsubjlist4.append(evensubjlist4[i - 1])

print(newsubjlist1)
print(newsubjlist2)
print(newsubjlist3)
print(newsubjlist4)

n = 2

grouplist1 = [newsubjlist1[i * n:(i + 1) * n] for i in range((len(newsubjlist1) + n - 1) // n)]
grouplist2 = [newsubjlist2[i * n:(i + 1) * n] for i in range((len(newsubjlist2) + n - 1) // n)]
grouplist3 = [newsubjlist3[i * n:(i + 1) * n] for i in range((len(newsubjlist3) + n - 1) // n)]
grouplist4 = [newsubjlist4[i * n:(i + 1) * n] for i in range((len(newsubjlist4) + n - 1) // n)]

print(grouplist1)
print(grouplist2)
print(grouplist3)
print(grouplist4)

# print(grouplist1)
# print(grouplist2)
# print(grouplist3)
# print(grouplist4)
# listofsubjlists = [list(divide_chunks(newsubjlist1, 2)), list(divide_chunks(newsubjlist2, 2)),
#                    list(divide_chunks(newsubjlist3, 2)), list(divide_chunks(newsubjlist4, 2))]
#
# print(listofsubjlists)