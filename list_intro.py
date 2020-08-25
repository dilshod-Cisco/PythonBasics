# IDE -  integrated Development Environment
# java - eclips, intellijIdea
# python - VScode, Pycharm, VIM
# print ("Hello World!!")

# cars = ['bmw',  'audi', 'lexus', 'bugatti']
# print(f"today im gonna drive bugatty"{})
# print(f'after "modification": {cars}')

# cars = ['bmw',  'audi', 'lexus', 'bugatti']
# print(f"befor: {cars}")
# cars[2] = 'tesla'
# cars.append('honda')
# print(cars)

# guests = ("Trump", "Mike", "Putin", "Xin jin ping")
# print(f"welcom to the dinner {guests[0]}!")
# print(f"welcom to the dinner {guests[1]}!")
# print(f"welcom to the dinner {guests[2]}!")
# print(f"welcom to the dinner {guests[3]}!")
# students = ['john', 'Mark', 'Aziz', 'Firuza', 105]

# reformat the file based on PEP8 rules >> CTRL + ALT +L
# data structure: lists, tuples, dictionaries (JAVA, HashMap, Hashset...)
# create, access the elements,  modify, remove elements from Data structure, organize
# print(f"Hello, {students[1]}! Thank you for coming.")
# print(f"Hello, {students[4] }! Thank you for coming.")
# print("Hello," + str(students[4]) + " ! Thank you for coming.")
# cars = ['Bmw', 'Lexus','Honda', 'Cadilac']
# print(f"I'm drive today {cars [0]} or {cars [1]} or {cars [2]}")
# print (f" tomorrow i will drive {cars[3]}!")
# ============================ MODIFY LISTS  ==========================================
# cars = ['Bmw', 'Lexus','Honda', 'Cadilac']
# print(f"befor:{cars}")
# cars[2]= 'Tesla' # this will replace 'Honda'
# print(f"after{cars}")
# ADDING ELEMENTS
# ============== APPENDING ================
# cars.append("Jet") # this will add the 'Jet' to the end of the list
# print(cars)
# ================== INSERT ==================
# cars.insert(2,'Helicopter') # this will insert and move all other object to the right, nothing lost.
# print(cars)
# ============================= REMOVE FORM THE LIST =================================================
# ================= delete by index ============================
# print(cars)
# DEL cars[2]
# cars.POP(2) # last element or delete by index, returns the value that is being remove
# print(f"after pop(2): {cars}")

# ============= delete by value  =================
# cars.remove('Jet')
# print(f"after remove :{cars}")
# 3-4 and 3-5
# POP() === deletes last elements by default, you remove by giving index[]
# print('============================= 3-4 =============================')
# print(f"Welcome to diner {guests[0]}!")
# print(f"Welcome to diner {guests[1]}!")
# print(f"Welcome to diner {guests[2]}!")
# print(f"Welcome to diner {guests[3]}!")
# print(f"unfortunately {guests[4]} can not come.")
# guests_not_coming = []
# guests_not_coming.append(guests[4])
# guests[4] = 'Putin'


# print(f"{guests[4]} sorry to hear that, please come next time,")
# print(f"Guests are coming: {guests}")
# print(f"Welcome to diner {guests[0]}!")
# print(f"Welcome to diner {guests[1]}!")
# print(f"Welcome to diner {guests[2]}!")
# print(f"Welcome to diner {guests[3]}!")
# print(f"Welcome to diner {guests[4]}!")
# ============================ HM 3-6 3-7 3-8 ===============================================
# guests.insert(0,'big John')
# guests.insert(2,'Putin')
# guests.append('Tony')
# print(f"Wellcome to dinner {guests[0]}!")
# print(f"Wellcome to dinner {guests[1]}!")
# print(f"Wellcome to dinner {guests[2]}!")
# print(f"Wellcome to dinner {guests[3]}!")
# print(f"Wellcome to dinner {guests[4]}!")
# print(f"Wellcome to dinner {guests[5]}!")
# print(f"Wellcome to dinner {guests[6]}!")
# print(f"Wellcome to dinner {guests[7]}!")
# guests.pop(-1)
# guests.pop(2)
# guests = ['Trump', 'Mike', 'Tom', 'Henry', 'Andrew']
# guests.pop(1)
#
# print(f"Sorry we can not invite you today for the diner {guests[2]}!")
#
# print(f"Welcome to diner {guests[0]}!")
# print(f"Welcome to diner {guests[2]}!")

#===================== 3-5 ==============================
# guests_not_coming = []
# guests_not_coming.append(guests[0])
# print(f"sorry to hear that,{guests[0]} please come next time")
# guests[0] = 'M. Sharapova'
# print(f"Guests are NOT coming: {guests_not_coming}")
# print(f"Guests are coming: {guests}")
# print(f"Welcome to the diner {guests[0]}!")
# print(f"Welcome to the diner {guests[1]}!")
# print(f"Welcome to the diner {guests[2]}!")
# print(f"Welcome to the diner {guests[3]}!")
# print(f"Welcome to the diner {guests[4]}!")
#======================== 3-6 =================================
# guests.insert(0,'Henry')
# guests.insert(2,'Sandra')
# guests.append('Jerry')
# print(f"Welcome to the diner {guests[0]}!")
# print(f"Welcome to the diner {guests[1]}!")
# print(f"Welcome to the diner {guests[2]}!")
# print(f"Welcome to the diner {guests[3]}!")
# print(f"Welcome to the diner {guests[4]}!")
# print(f"Welcome to the diner {guests[5]}!")
# print(f"Welcome to the diner {guests[6]}!")
# print(f"Welcome to the diner {guests[7]}!")
#======================   3-7 =================================

# guests = ['Trump', 'Bill', 'John', 'Mark', 'Michael']
# print(f"Sorry we can invite only two person at this time {guests}")
# print(f"Sorry we can not invite you to the diner today {guests[4]}")
# new_guests = guests.pop()
# print(guests)
# print(new_guests)
# print(f"Sorry we can not invite you to the diner today {guests[3]}")
# new_guests1 = guests.pop()
# print(guests)
# print(new_guests1)
# print(f"Sorry we can not invite you to the diner today {guests[2]}")
# new_guests2 = guests.pop()
# print(guests)
# print(new_guests2)
# print(f"Welcome to the diner {guests[0]}")
# print(f"Welcome to the diner {guests[1]}")
# del guests[: 2]
# print(guests)
#=========== ORGONIZING YOUR LIST;===================================
# temporary and permanently sorting, sorted() works for some other data structures
# print(sorted(guests))  # temp sorting
# sorted_guests = sorted(guests)
# print(sorted_guests)
# print(guests)

# print(sorted(guests)) # temp sorting, sorted() works for some other data structures
# sorted_guests = sorted(guests) # sorted() - returns you the copy of the list but sorted in ASC
# print(sorted_guests)
# print(guests)
#============= lists.reverse() - reverses but not desc order:
#============= list.sort(reverse=True) - sorts in desc order:
# guests.reverse()
# print(f"Reversing the list: {guests}")
#
# print()
# nums = [4, -10,9,5,6,1,0,44]
# print(nums)
# nums.reverse()
# print(nums)
# nums.sort(reverse=True)
# print(nums)
# nums.insert(8, 100)
# print(nums)
#
# print(f"Number of elements in my 'num' list :{len(nums)}")
# ===== list_name = [] - creates the new, empty list:
# ===== list.append(newValue)
# ===== list.insert(ind, value)
# ===== del.list[ind]
# ===== list.remove(value)
# ===== list.pop() - removes and returns the last element, list.pop(ind)
# ===== list[ind] = value - assigning a new value to existing Index
# ===== list.sort(), list.sort?(revers=True)
# ===== sorted(list) - copies the list and returns sorted copy of the list
# ===== list.reverse()
# ===== len(list) - returns the length of your list (how big is list, i.e. number of elements on the list)
# ===== list[-n] - index start from the end of the list,last element is list [-1]
# guests.sort() # only works for list and does not return anything, just effects the original list permanently:
# print(f"Perm sorting with list.sort() : {guests}")
# guests.sort(reverse=True)
# print(f"Perm reverse (desc) sorting with list.sort() : {guests}")
# ==================== HW 3-8 =======================
# World = ['Italy', 'Moscow', 'Paris', 'Spain', 'Argentina', 'Germany', 'England']
# print(World)
# print(sorted(World))
# print(World)
# print(sorted(World, reverse=True))
# print(World)
# World.reverse()
# print(World)
# World.reverse()
# print(World)
# World.sort()
# print(World)
# World.sort(reverse=True)
# print(World)
#=========================== 































































