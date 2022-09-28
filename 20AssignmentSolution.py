# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 22:21:07 2022

@author: NIYATI SHARMA
"""

#Q1.) Set the variable test1 to the string &#39;This is a test of the emergency text system,&#39; and save test1 to a
#file named test.txt.
 
test1 = 'This is a test of the emergency text system,'
filee = open('test.txt','w')
filee.write(test1)



#Q2.) Read the contents of the file test.txt into the variable test2. Is there a difference between test 1 and test 2?........
file2 = open('test.txt','r')
test2 = file2.readline()
test2


#Q3.) Create a CSV file called books.csv by using these lines:
# title,author,year
# The Weirdstone of Brisingamen,Alan Garner,1960
# Perdido Street Station,China Miéville,2000
# Thud!,Terry Pratchett,2005
# The Spellman Files,Lisa Lutz,2007
# Small Gods,Terry Pratchett,1992...........
if test1==test2:
    print('Both are same')
    
    
#Q4.) Q. Create a CSV file called books.csv by using these lines: title,author,year The Weirdstone of Brisingamen,Alan Garner,1960 Perdido Street Station,China Miéville,2000 Thud!,Terry Pratchett,2005 The Spellman Files,Lisa Lutz,2007 Small Gods,Terry Pratchett,1992

import csv
rows =[ ['title','author','year'],
    ['The Weirdstone of Brisingamen','Alan Garner',1960],
    ['Perdido Street Station','China Miéville',2000],
    ['Thud!','Terry Pratchett',2005],
    ['The Spellman Files','Lisa Lutz',2007],
    ['Small Gods','Terry Pratchett',1992]]
with open('books.csv','w',newline='') as file:
    writer = csv.writer(file)
    writer.writerows(rows)
    
#.Q5.) NUse the sqlite3 module to create a SQLite database called books.db, and a table called books with these fields: title (text), author (text), and year (integer).
import sqlite3
conn = sqlite3.connect('books.db')
c = conn.cursor()

c.execute('create table books(title varchar(20),author varchar(20), year int)')
conn.commit()