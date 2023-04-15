#############################IMPORTS##########################################
from tkinter import *
from tkinter import messagebox
# import random
from random import randint, choice, shuffle
import pyperclip

#############################CONSTANS##########################################
FONT = ('Arial', 12,'normal')
GREY = '#2E4F4F'
OCEAN = '#0E8388'
LIGHT_BLUE ='#CBE4DE'
DARK_GREY ='#2C3333'

########################PASSWORD GENERATOR#####################################
def generate_pass():
    #Symbols to create password
    letters = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
        'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
        'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
        'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    #__________________The shortest code_______________________#
    com_list_letter = [choice(letters) for l in range (0, randint(6,12))]
    com_list_number = [choice(numbers) for n in range (0, randint(3,5))]
    com_list_symbol = [choice(symbols) for s in range (0, randint(4,6))]
    


    #_________________Middle long code________________________#
    # #Choose random letter from list letters
    # one_letter = random.choice(letters)
    # one_number = random.choice(numbers)
    # one_symbol = random.choice(symbols)

    # #Random amount of characters
    # nr_letters = random.randint(6,12)
    # nr_numbers = random.randint(3,5)
    # nr_symbols = random.randint(4,6)

    # #comprehension_list = [new_item for item in list/range]
    # #pick random 1 letter from list letters in range 0:6-12 characters
    # com_list_letter = [one_letter for l in range (0,nr_letters)]
    # com_list_number = [one_number for n in range (0,nr_numbers)]
    # com_list_symbol = [one_symbol for s in range (0,nr_symbols)]


    #_________________Long code________________________________#
    # #Empty list for letters
    # list_letters = []

    # for l in range(0, nr_letters):
    #     one_letter = random.choice(letters)
    #     list_letters.append(one_letter)

    # #Empty list for numbers
    # list_numbers = []

    # for n in range(0, nr_numbers):
    #     one_number = random.choice(numbers)
    #     list_numbers.append(one_number)

    # #Empty list for symbols
    # list_symbols = []

    # for s in range(0, nr_symbols):
    #     one_symbol = random.choice(symbols)
    #     list_symbols.append(one_symbol)
    #__________________________________________________________#

    # #List with all characters to create password
    # pass_list = list_letters+list_symbols+list_numbers
    pass_list = com_list_letter + com_list_symbol + com_list_number

    #Shuffle items in pass_list to create random password
    # random.shuffle(pass_list)
    shuffle(pass_list)

    #______________Short code_______________#
    randomised_password = ''.join(pass_list)

    # #______________long code________________#
    # password = ""
    # for char in pass_list:
    #     password += char

    #Write password in entry
    pass_entry.insert(0, randomised_password)

    #Copy to clipboard
    pyperclip.copy(randomised_password)


##########################SAVE PASS########################################
def save():
    #Grab information from entries
    website = website_entry.get()
    email = email_entry.get()
    password = pass_entry.get()

    #Simply validation to avoid empty entries
    if len(website) == 0:
        messagebox.showinfo(title='Empty field', message='Please fill name of Website or Application', icon='warning')
    elif len(password) < 8:
        messagebox.showinfo(title='Empty field', message='Please fill your password. Password should have min 8 characters.', icon='warning')
    elif '@' not in email or len(email) == 0:
        messagebox.showinfo(title='Empty field or wrong format', message='Please fill your email in correct form. Email should have @.', icon='warning')
    else:
        #Messagebox for user to confirm data -return True(ok) or False (cancel)
        confirm_message = messagebox.askokcancel(title='Confirm your data', message=f'Information to save:\n WEBSITE\APPLICATION: {website}\n EMAIL\LOGIN:{email}\n PASSWORD: {password}\n', icon='question')

        if confirm_message == True:
            #Append new informations to data.txt
            with open('data.txt', mode='a') as data:
                data.write(f'*[{website}] :      {email} | {password}\n')
                website_entry.delete(0,END)
                email_entry.delete(0, END)
                pass_entry.delete(0,END)



#######################UI CONFIG##########################################
#Window setup
window = Tk()
window.title('Password Manager')
window.config(padx=50, pady=30, bg='black')

#Canvas setup
canvas = Canvas(width=600, height=390, bg='black', highlightthickness=0)
pass_img = PhotoImage(file='keys3.png')
canvas.create_image(300, 195, image=pass_img)
canvas.grid(row=1, column=1, sticky="EW")


#Labels
title_label = Label(text='PASSWORD MANAGER', bg='black',fg=OCEAN, font=('Calibri', 40, 'bold'))
title_label.grid(row=0, column=1, pady=20)
website_label = Label(text='WEBSITE/ APPLICATION:', font=FONT, bg='black', fg=LIGHT_BLUE)
website_label.grid(row=2, column=0)
email_label = Label(text='EMAIL/ LOGIN:', font=FONT, bg='black', fg=LIGHT_BLUE)
email_label.grid(row=3, column=0)
password_label = Label(text='PASSWORD', font=FONT, bg='black', fg=LIGHT_BLUE)
password_label.grid(row=4, column=0)

#Entries
website_entry = Entry(bg=DARK_GREY, fg=LIGHT_BLUE)
website_entry.grid(row=2, column=1, columnspan=2, sticky="EW", pady=(0,10))
website_entry.focus()
email_entry = Entry(bg=DARK_GREY, fg=LIGHT_BLUE)
# email_entry.insert(0, 'your_mail@gmail.com')
email_entry.grid(row=3, column=1, columnspan=2, sticky="EW", pady=(0,10))
pass_entry = Entry(bg=DARK_GREY, fg=LIGHT_BLUE)
pass_entry.grid(row=4, column=1, sticky="EW", pady=(0,10))

# Buttons
generate_pass_button = Button(text='GENERATE PASSWORD',bg=GREY, fg=LIGHT_BLUE, command=generate_pass)
generate_pass_button.grid(row=4, column=2, sticky="EW", padx=(10,0))

add_button = Button(text='ADD', width=20, command=save, bg=OCEAN, fg=LIGHT_BLUE, font=('Calibri', 20, 'bold'))
add_button.grid(row=5, column=1, columnspan=2, sticky="EW", pady=(10,20))



window.mainloop()