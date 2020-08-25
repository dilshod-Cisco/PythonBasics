# 6-5. Rivers: make a dictionary containing three major rivers and the country
# each river runs through. one key-value pair might be 'nile' : 'egypt'.
# use a loop to print the name of each country included in the dictionary.

# rivers = {'nile': 'egypt', 'hudson': 'usa', 'volga': 'russia', 'mississippi': 'usa', 'thames': 'uk'}

#=== use a loop to print a sentence about each river, such as the Nile runs
#=== through Egypt.
# ===: The Key runs through Value
# for river, country in rivers.items():
#     if country in ['usa', 'uk']:
#         print(f"The {river.title()} runs through {country.upper()}.")
#     else:
#         print(f"The {river.title()} runs through {country.title()}.")

#=== use a loop to print the name of each river included in the dictionary.
# print('Rivers are :')
# for river in rivers.keys():
#     print('\t', river.title(), end=" |")
#
#
# #=== use a loop to print the name of each country included in the dictionary.
# print('\nCountries are:')
#
# for country in sorted(rivers.values(), reverse=True):
#     if country in ['usa', 'uk']:
#         print('\t', country.upper(), end=" |")
#     else:
#         print('\t', country.title(), end=" |")

# print("\n********************** 6-11. Cities: ******************************")
# cities = {'new york': {'country': 'usa', 'population': '8.4', 'fact': 'Big Apple'},
#           'istanbul': {'country': 'turkey', 'population': '15.52', 'fact': 'constantinople'},
#           'tashkent': {'country': 'uzbekistan', 'population': '2.5', 'fact': 'stone city'},
#           'moscow': {'country': 'russia', 'population': 12.53, 'fact': 'kremlin'}
#           }
# # === "City is very beautiful in country, it has population and city is also known as fact"
#
# for city, info in cities.items():
#     # print(city)
#     # print(info)
#     print(f"{city.title()} is very beautiful city in {info['country'].title()}."
#           f"It has {info['population']} mln population and the city is also known as {info['fact']}.")


# HW:
#================= print multiplication table 1-10  ================================

for i in range(1,11):
    for cal in range(1,11):
        print(f"{i} * {cal} = {i*cal}", end='\t')
    print('')

#=======================================================================================






















































