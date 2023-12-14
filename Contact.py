names=[]
ph_num=[]
num=3


for i in range(num):
    name=input("\nName: ")
    Ph_num=input("Phone number")
    names.append(name)
    ph_num.append(Ph_num)
print("\nName\t\t\t PhoneNumber\n")

for i in range(num):
    print("{}\t\t\t{}".format(names[i],ph_num[i]))
search_term=input("\nEnter Search Term: ")
print("Search Result")


if search_term in names:
    index=names.index(search_term)
    ph_num=ph_num[index]
    print("\nNames{}, Phone number: {}".format(search_term, ph_num))

else:
    print("Name not Found!")