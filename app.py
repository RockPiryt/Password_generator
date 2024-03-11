#############################IMPORTS##########################################

from random import randint, choice, shuffle



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
    
    # List with all characters to create password
    pass_list = com_list_letter + com_list_symbol + com_list_number

    #Shuffle items in pass_list to create random password
    shuffle(pass_list)

    #______________Short code_______________#
    randomised_password = ''.join(pass_list)



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


