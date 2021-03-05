# pip3 install mysql-connector-python

import mysql.connector
from difflib import get_close_matches

from mysql.connector.errors import DatabaseError




con = mysql.connector.connect(
    user = 'ardit700_student',
    password = 'ardit700_student',
    host = "108.167.140.122",
    database = "ardit700_pm1database"
)

cursor = con.cursor()

word =  input("Enter a word: ")
#query = cursor.execute("SELECT * FROM Dictionary")
#query = cursor.execute("SELECT * FROM Dictionary WHERE Expression = 'inlay'")
#query = cursor.execute("SELECT * FROM Dictionary WHERE Expression = '%s'" % word)
#query = cursor.execute("SELECT * FROM Dictionary WHERE Expression LIKE '%s'" % word)
word= word+'%';
query = cursor.execute("SELECT * FROM Dictionary WHERE Expression LIKE '%s'" % word)

data = cursor.fetchall()
print(data)

if data:
    for result in data:
        print(result)
else:
    print("No word found")

'''
def get_meaning(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif w.title() in data:
        return data[w.title()] 
    elif w.upper() in data:
        return data[w.upper()]        
    elif len(get_close_matches(w, data.keys())) > 0:
        yn = input(" Did you mean %s instead? Enter Y if yes, or N if no:" % get_close_matches(w, data.keys())[0])
        if yn == "Y":
            return data[get_close_matches(w, data.keys())[0]]
        elif yn == "N":
            return "The word does not exist, please check again."
        else:
            return "We did not understand your input"
    else:
        return "The word does not exist, please check again."

'''
