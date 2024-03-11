import json
from random import randint, choice, shuffle


# define the handler function that the Lambda service will use an entry point
def lambda_handler(event, context):

# extract the website name from the Lambda service's event object
    
    site_name = str(event['website'])
    
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

    # return a properly formatted JSON object
    return {
    'statusCode': 200,
    'body': json.dumps('Your password for website: ' + ' ' +  site_name + ' is : ' + randomised_password)
    }

