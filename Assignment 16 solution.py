# -*- coding: utf-8 -*-
"""
Created on Wed Aug 24 21:46:04 2022

@author: NIYATI SHARMA
"""

#Q1.>Create a list called years_list, starting with the year of your birth, and each year 
#thereafter until the year of your fifth birthday. For example, if you were 
#born in 1980. the list would be years_list = [1980, 1981, 1982, 1983, 1984, 1985].
years_list = [i for i in range(1997,2002+1)]

#Q2.>In which year in years_list was your third birthday? Remember, you were 0 years of age for
# your first year.
years_list[2]


#Q3.>In the years list, which year were you the oldest?
max(years_list)

#Q4.>Make a list called things with these three strings as elements: "mozzarella", "cinderella",
 #"salmonella".
things = list(['mozzarella', 'cinderella','salmonella'])
things
#.Q5.>Capitalize the element in things that refers to a person and then print the list. Did it change the element in the list?
for i in things:
    print(i.capitalize())
things
#Q6.Make a surprise list with the elements "Groucho," "Chico," and "Harpo."
surprise_list = ["Groucho", "Chico", "Harpo"]
surprise_list
#Q7.>Lowercase the last element of the surprise list, reverse it, and then capitalize it.
surprise_list[-1].lower()
'harpo'
#Q8.>Make an English-to-French dictionary called e2f and print it. Here are your starter words:
    #dog is chien, cat is chat, and walrus is morse.
e2f = {'hindi':'chien','cat':'chat','walrus':'morse'}