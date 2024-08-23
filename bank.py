
def banck():

    # create account
    account = []
    name = input('Please enter your name: ')
    account.append(name)
    last_name = input('Plase neter your last name: ')
    account.append(last_name)
    age = int(input('Please enter your age: '))
    account.append(age)


    # Deposit
    input_money = int(input('If you want to deposit money, indicate how much you want to deposit, and if you dont want to, write 0: '))
    if input_money == 0:
        print('You dont want to deposit money')

    else:
        print('Your money is kept in a safe deposit box')    
        return output_money
    
    # withdraw
    output_money = int(input('If you want to withdraw money, specify how much you need: '))
    if output_money <= 50 :
        return 'Bring out more because there is little money'
    else:
        print('You have ', output_money)

banck()