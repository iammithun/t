# -*- coding: utf-8 -*-
"""
Created on Sat Feb 24 21:12:27 2024

@author: iamrs
"""

from prettytable import PrettyTable

table=PrettyTable()
table.add_column("Pokemon Name", ["Pickachu", "Squirtle", "Charmander"])
table.add_column("Tyoe", ["Electric", "Water", "Fire"])

print(table)




from prettytable import PrettyTable

table=PrettyTable()
table.add_column("Pokemon Name", ["Pickachu", "Squirtle", "Charmander"])
table.add_column("Tyoe", ["Electric", "Water", "Fire"])


print(table.align)
print(table)


from prettytable import PrettyTable

table=PrettyTable()
table.add_column("Pokemon Name", ["Pickachu", "Squirtle", "Charmander"])
table.add_column("Tyoe", ["Electric", "Water", "Fire"])

table.align="l"

print(table)


