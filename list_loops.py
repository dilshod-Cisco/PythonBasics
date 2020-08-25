# Chapter 4: Working with  LIST
# LOOPS - within the loops you creat repetetive actions

# for variable in list_of_elements:
#     repetetive code here
#============================== LOOPS ======================================
# for state in states:
#     pass # means do nothing
#     print(f"Welcome to {states} !!")
# Thinks to REMEMBER while working with LOOPS
    # colon at the end of 'for' line
    # 'in' in the 'for' line
    # give any name to a variable and use that variable inside the for loop code
    # lines of code that belongs to for loop (repetitive code) must be indented
# ============================= SCOPE =========================================

# states = ['New York', 'New Jersey', 'Connecticut', 'California']
# states >> 4 members >>
#   >> 1st loop/round >> state = 'New York'  --- python does this
#   >> print(f"Welcome to {state} !!")       --- we will write this code
#   >>> Welcome to New York !!               --- this is execution

#   >> 2st loop/round >> state = 'New Jersey'
#   >> print(f"Welcome to {state} !!")
#   >>> Welcome to New Jersey !!

#   >> 3st loop/round >> state = 'Connecticut'
#   >> print(f"Welcome to {state} !!")
#   >>> Welcome to New Connecticut !!

# Pycharm: refactoring >> Shift + fn +f6: short cat for changing the variables value
# print(states)
#
# for state in states:
#     print(f"Welcome to {state} !!")
#
# print("Enjoe your trip !!") # outside of loop, independent from loop
# print(state)  #  Incorrect: outside of the scope of variable
# ======  4-1 ======
# print()
# Pizzas = ['Regular', 'Peperoni','Vegetables']
# for Pizza in Pizzas:
#     print(f"I like  Pizza {Pizza} !")
# print(f"I like this type of pizza !")
# ===========================================

# magicians = ['alice', 'david', 'carolina'] #looping by myself with out guid !
# for magician in magicians:
#     print() # this is for the space:
#     print(f" {magician.title()} that was a great trick !")
#     print()
#     print(f"I can't wait to see your next trick {magician.title()}!")
# ========================  4-2 ==================
# Animals = ['Tiger', 'Lion', 'Leopard']
# for Animal in Animals:
#     print(f"I like tis type of animal {Animal} !")
#     print(f"This animal {Animal} shows beauty of nature !")
# # ======================== 4-3 ===============================
# for num in range(1,21):
#     print(num)
# === 4-4 ====
# for num in range(1,1000001):
#     print(num)
# squares = []
# for num in range(5,13):
#     num_sqr = num ** 2
#     squares.append(num_sqr)
#     print(num_sqr)
#     print(squares)

# sguares = list() # ?????????????
# for num in range(5, 13):
#     squares.append(num **2)
# print(squares)
# ================
# numbers = [5, 78, 456, 127, 230, 6, 5]
# # min(list) , max(list), sum(list)
# print(f"Min number from numbers :{min(numbers)}")
# print(f"Max number from numbers :{max(numbers)}")
# print(f"Sum number from numbers :{sum(numbers)}")
# ==== 4-5 ====
# add_numbers = [1, 25, 350, 550, 750, 1000000]
# print(f"Min number from numbers :{min(add_numbers)}")
# print(f"Max number from numbers :{max(add_numbers)}")# why when you use (max function) python see last numbers?
# print(f"Sum number from numbers :{sum(add_numbers)}")
# ======================== 4-6 ===========================
# odd_numbers = list(range(1, 21, 2))
# for number in odd_numbers:
#     print(number)
# ================= 4-7 =======================
# threes = list(range(3, 31, 3))
# for three in threes:
#     print(three)
# ==== =====   list comprehension ==========
# squares = [num ** 2 for num in range(5,13)]
# print(squares)
# ===========  4-8 =======================
# cubes = [num ** 3 for num in range(1, 11)]
# print(cubes)
#
# # ===    ===     ===     ===     ====
# cubes = []
# for n in range(1, 11):
#     cube = n**3
#     cubes.append(cube)
# for c in cubes:
#     print(c)
# == == == == == 4--9 ==  === ====  ====
# cube_cphn = [number ** 3 for number in range(1, 11)]
# print(cube_cphn)
#
# === === === === === ===
# for cube in cube_cphn:
#     pass
# ====  ======   4-10 ===== =====
# Teams = ['Mike', 'John', 'Filip', 'Artur', 'Chuck', 'James', 'Harvey', 'Bruce', 'Jacky', 'Steve']
# print(Teams)
# print("The first three items in the list are: ")
# for team in Teams[:3]:
#     print(team)
# print("The  three items from the middle of the list are: ")
# for team in Teams[3:6]:
#     print(team)
# print("The last  items in the list are :")
# for team in Teams[6:]:
#     print(team)
# ==== ==== ==== 4-11 ====  ==== ====  ====
# my_pizza = ['peperoni', ' veggie', 'regular']
# friend_pizza = my_pizza[:]
#
# my_pizza.append('buffalo')
# friend_pizza.append('cheese')
#
# print("My favorite pizzas are :")
# for pizza in my_pizza:
#     print("-" + pizza.title())
#
# print("\nMy friend's favorite pizzas are :")
# for pizza in friend_pizza:
#     print("-" + pizza.title()) # - ".title()" used for convert first later list with upper case :
# ==== ====   =======   4-12 =====  ======    =======
# foods = ['pilaf', 'chicken kebab', 'pizza', 'samsa', 'manti']
# favorite_foods = foods[:]
#
# print("my favorite foods are : ")
# for f in foods:
#     print(f)
#
# print("\nmy friends food list similar as mine  '_^ ")
# for f in sorted(favorite_foods):
#     print(f)






















