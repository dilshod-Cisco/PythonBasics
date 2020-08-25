################################### WHITE LOOP ######################################
#todo: secret_word = "giraffe"
# todo: guess = ""
#todo: guess_count = 0
#todo: guess_limit = 3
#todo: out_of_guess = False

#todo: while guess != secret_word and not(out_of_guess):
 #todo:   if guess_count < guess_limit:
# todo:       guess = input("Enter guess: ")
# todo:       guess_count += 1
# todo:    else:
# todo: out_of_guess = True

# todo: if out_of_guess:
 # todo:    print("Out of Guessses, You LOSE!")
# todo: else:
# todo:     print("You win!")

############################ FOR LOOP ########################################################
# todo :friends = ["Jim", "Karen", "Kevin"]
# todo :for friend in friends:
# todo :    print(friend)
######################  Exponent Function ############################################################
# def raise_to_power(base_name, pow_num):
 #   result = 1
  #  for index in range(pow_num):
   #     result = result * base_name
    #return result

# print(raise_to_power(3,4))
#####################  2D List & Nested Loops ########################################################
#number_grid = [
  #  [1, 2, 3],
 #   [4, 5, 6],
#    [7, 8, 9],
 #   [0]
#]
#print(number_grid[2][1])
###################################################################################################

#number_grid = [
 #   [1, 2, 3],
  #   [4, 5, 6],
   #  [7, 8, 9],
    # [0]
#]

#for row in number_grid:
   # for col in row:
  #      print(col)
#################   Build a Translator  ########################################################
# def translate(phrase):
#     translation = ""
 #    for letter in phrase:
 #        if letter.lower() in "aeiou":
 #            if letter.isupper():
 #                traslation = translation + "G"
 #            else:
 #            translation = translation + "g"
 #        else:
 #            translation = translation  + letter
 #     return translation
 # print(translate(input("Enter a phrase:")))
     ############################ Try Except #############################################
#try:
#     number = int(input("Enter a number "))
 #    print(number)
#except:
#    print("Invalid Input")
#########################    Reading Files ####################################################
# open("name_file.txt", "any_file.txt" ("r") this is standing for read only) ("w") for writhing)and -
# -also can over write, and add new file
# ("a") stands for append (modify) the file)( "r+" read and write,)
# name_file = open:  name_file.close() when you Done:
# print(name_file.readable())  (checks the file if is a readable) (we can check also by(w)( write)
####################  Writing to Files ########################################################
# file_name = open("file_name.txt", "a") and then on the terminal make append  the file
# file_name.write("this is another options to add the or make a change on file")
####################### Modules and Pip #########################################
# import File_name  exp:(useful_tools), print(file_name.roll_dice(10)) can be used for import the inside -
# the another file for actual file(importing the files)
######################  Classes & Objects #########################################
# creating student files
# Class Students:
#       def__init__(self, name, major, gpa, is_on_probation):
#          self.name = name
#          self.major = major
#          self.gpa = gpa
#          self.is_on_probation = is_on_probation
#######################  Building a Multiple Choice Quiz  ##################################
# quastion_prompts = [
#    "What color are apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n",
#    "What color are Bananas?\n(a) Teal\n(b) Magenta\n(c) Yellow\n\n",
#    "What color are strawberries?\n(a) Yellow\n(b) Red\n(c) Blue\n\n"

# even_numbers = list(range(2,11,2))
# print(even_numbers)


# squares = []
# for value in range(1,11):
#     square = value**2
#     squares.append(square)
#
# print(squares)



















