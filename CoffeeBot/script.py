# The skills I demonstrated in this project are the use of leveraging recursive functions and then using
# for loops and while loops. This chatbot is designed to use user input to complete a coffee drink order. 
# To run this chatbot enter 'python3 script.py' in terminal. 

from utils import print_message, get_size, order_latte

def coffee_bot():  # desiging how to order multiple drinks in a order
  print('Welcome to the cafe!')
  
  order_drink = 'y'
  drinks = []
  
  while order_drink == 'y':
    size = get_size()  
    drink_type = get_drink_type()

    drink = '{} {}'.format(size, drink_type)
    print('Alright, that\'s a {}!'.format(drink))
    
    drinks.append(drink)

    while True:
      order_drink = input("Would you like to order another drink? (y/n) \n>")

      if order_drink in ['y','n']:
        break

  print('Okay, so I have:')
 
  for drink in drinks:
    print('-', drinks)

  name = input('Can I get your name please? \n> ')

  print('Thanks, {}! Your order will be ready shortly.'.format(name))

def get_drink_type():
  res = input('What type of drink would you like? \n[a] Brewed Coffee \n[b] Mocha \n[c] Latte \n> ')

  if res == 'a':
    return 'brewed coffee'
  elif res == 'b':
    return order_mocha()
  elif res == 'c':
    return order_latte()
  else:
    print_message()
    return get_drink_type()
  
# Defineing a new functions

def order_mocha():      # using while and a conditional for drink order
  while True:
    res = input('Would you like to try our limited-edition peppermint mocha? \n[a] Sure! \n[b] Maybe next time!')

    if res == 'a':
      return 'peppermint mocha'
    elif res == 'b':
      return 'mocha'
    print_message()

coffee_bot()
