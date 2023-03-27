
# Individual Course Work DOC334
# 20210053


# user menu
print('\n')
print("=============== Welcome to the Hangman Game ===============")
print('\n')

# importing the modules

import sub.u_input

# declaring the variables

item_list=[]
allowed_errors=1
error_list=[]
info_list=[]
length_list=[]
user_input=''
user_name=''
user_name=str(input("Enter your name :"))

# getting the user input
    
user_input=str(input("1.**Enter Y to Enter to the game**\n2.**Enter E to Exit from the Game**\nInput:"))
print('\n')


if user_input == 'Y' or user_input == 'y' or user_input == 'E' or user_input == 'e':
    if user_input== 'E' or user_input== 'e':
        print("Thank You!! Better try next time")
    else:
        while user_input== 'Y' or user_input== 'y':
            while allowed_errors!=0:
                print('==============================================================')
                print('==============================================================')
                print('\n')
                user_input=str(input('Enter Y to proceed the game or E to exit the game :'))
                if user_input == 'y' or user_input == 'Y' or user_input == 'E' or user_input == 'e':
                    if user_input== 'E' or user_input== 'e':
                        print()
                        print("Thank You!! Better try next time")
                        break
                    else:
                        print('\n')
                        sub.u_input.beginning()
                        allowed_errors, word, hint_list, info_list, error_list, length_list =sub.u_input.middle(info_list, error_list, length_list)

                    if allowed_errors==0:
                        print("You are out of luck, Better try next time!!!")
                        print("The word was","*",word.upper(),"*")
                        print()
                        print("===================================================================")
                        print("===================================================================")
                        print("Name :",user_name.upper())
                        print()
                        print("Errors Made     ","Word")
                        print()
                        for x in range(len(info_list)):
                            print('   ',length_list[x],'\t''\t','   ',error_list[x],'\t''\t'' ',info_list[x].upper())
                        break
                    else:
                        continue
                    print("You lose!! Better try next time")
                    
                else:
                    print('enter a valid input')
                    break
else:
    print('enter a valid input')
    
    
print("===================================================================")
print("===================================================================")
print()

# displaying the user info

print("Name :",user_name.upper())
print()
print("Errors allowed    ""Errors Made     ","Word")
print()
for x in range(len(info_list)):
    print('   ',length_list[x],'\t''\t','   ',error_list[x],'\t''\t'' ',info_list[x].upper())  





#==========================================================================
    




# Inserting records to a table in database

import mysql.connector

# opening database connection

conDict = {'host':'localhost',
           'database':'hangman',
           'user':'root',
           'password':''}

db = mysql.connector.connect(**conDict)

# prepare a cursor

cursor = db.cursor()

# execute SQL

Text = "INSERT INTO history VALUES (%s,%s,%s,%s)"

for i in range(len(info_list)):
    values=(user_name,info_list[i],(len(info_list[i])),error_list[i])
    cursor.execute(Text,values)
    db.commit()

# disconnect

db.close()


#===============================================================

# returning the information from MySQL

import mysql.connector

# open database

conDict = {'host':'localhost',
           'database':'hangman',
           'user': 'root',
           'password':''}

db = mysql.connector.connect(**conDict)

# prepare a cursor object

cursor = db.cursor()

# execute SQL

cursor.execute("SELECT NAME, WORD, CHANCES, ERRORS_MADE FROM history")

# fetch results

data = cursor.fetchall()


# disconnect from server

db.close()



#===============================================================


# HTML code for database

def html_history(data):
    import webbrowser
    fo = open("history.html",'w')

    fo.write("""<!DOCTYPE html>
<html>

    <head>
        <meta charset="utf-8">
        <meta http-equiv='X-UA-Compatible' content='IE=edge'>
        <title>Hangman past records</title>

        <link rel="stylesheet"href="main.cs">
    </head>
    <body>
<table class="styled-table">
    <style>
    .styled-table{
    border-collapse: collapse;
    margin: 25px 0;
    font-size: 0.9em;
    font-family: sans-serif;
    min-width: 400px;
    box-shadow: 0 0 20px rgba(0, 0, 0, 0.15);
}
    </style>
    <thead>
    <style>
    .styled-table thead tr {
    background-color: #009879;
    color: #ffffff;
    text-align: left;
}
    </style>
        <tr>
            <th>Player Name</th>
            <th>Word</th>
            <th>Chances</th>
            <th>Errors made</th>
        </tr>
        <style>
            .styled-table th,
.styled-table td {
    padding: 12px 15px;
}
        </style>
    </thead>
    
    <tbody>
        <style>
        
        .styled-table tbody tr {
    border-bottom: 1 px solid #dddddd;
        </style>""")
    for i in range(len(data)):
        fo.write(f"""<tr>
            <td> {(data[i][0])} </td>
            <td> {(data[i][1])} </td>
            <td> {(data[i][2])} </td>
            <td> {(data[i][3])} </td>
        </tr>""")

    fo.write("""</tbody>
            </table>
            </body>
            </html>""")
    fo.close()
    webbrowser.open_new_tab("history.html")


html_history(data)



