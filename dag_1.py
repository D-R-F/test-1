

def check_alder(alder):
    if alder >=18:
        return 'no'
    else:
        return 'yes'
    
user_input = int(input('Skirv alder'))

print(check_alder(user_input))
