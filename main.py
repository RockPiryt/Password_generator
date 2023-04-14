from tkinter import *
import random

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

    #Amount of letter,number, symbols
    nr_letters= 8
    nr_numbers = 3
    nr_symbols = 4

    #Empty list for letters
    list_letters = []

    count_l = 0
    for l in range(0, nr_letters):
        count_l = count_l + l
        one_letter = random.choice(letters)
        list_letters.append(one_letter)

    #Empty list for numbers
    list_numbers = []

    count_n = 0
    for n in range(0, nr_numbers):
        count_n = count_n + n
        one_number = random.choice(numbers)
        list_numbers.append(one_number)

    #Empty list for symbols
    list_symbols = []

    count_s = 0
    for s in range(0, nr_symbols):
        count_s = count_s + s
        one_symbol = random.choice(symbols)
        list_symbols.append(one_symbol)

    #List with all characters to create password
    pass_list = list_letters+list_symbols+list_numbers

    #Shuffle items in pass_list to create random password
    random.shuffle(pass_list)
    randomised_password = ''.join(pass_list)

    #Write password in entry
    pass_entry.insert(0, randomised_password)


##########################SAVE PASS########################################
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = pass_entry.get()

    with open('data.txt', mode='a') as data:
        data.write(f'*[{website}] :      {email} | {password}\n')
        website_entry.delete(0,END)
        pass_entry.delete(0,END)



#######################UI CONFIG##########################################

window = Tk()
window.title('Password Manager')
window.config(padx=50, pady=30, bg='black')

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
email_entry.insert(0, 'your_mail@gmail.com')
email_entry.grid(row=3, column=1, columnspan=2, sticky="EW", pady=(0,10))
pass_entry = Entry(bg=DARK_GREY, fg=LIGHT_BLUE)
pass_entry.grid(row=4, column=1, sticky="EW", pady=(0,10))

# Buttons
generate_pass_button = Button(text='GENERATE PASSWORD',bg=GREY, fg=LIGHT_BLUE, command=generate_pass)
generate_pass_button.grid(row=4, column=2, sticky="EW", padx=(10,0))

add_button = Button(text='ADD', width=20, command=save, bg=OCEAN, fg=LIGHT_BLUE, font=('Calibri', 20, 'bold'))
add_button.grid(row=5, column=1, columnspan=2, sticky="EW", pady=(10,20))



window.mainloop()