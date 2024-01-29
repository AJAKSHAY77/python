set_of_num = {1,2,4,2,2,2,2,4,4,4,3,3,3,5,6,7}
set_1  ={None} #this is set
set_2 = {} #this is disctionary
# print(type(set_of_num))
# print(set_of_num)

set_a = {1,2,3,4,5,5,5,6,6,7,8,8,9}
set_b = {1,2,3,9,0}

print(set_a.intersection(set_b))
print(set_a.union(set_b))

list_of_events = ["diwali","holie","jai ho","diwli","holie","jai ho"]
# my_set = (list_of_events)

my_set = set(list_of_events)
my_set_with_list = list(set(list_of_events))
print(type(my_set_with_list))

