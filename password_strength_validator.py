SPECIAL_CARACTERS = ['!', '@', '#', '$', '%', '&', '*']

def get_user_password():
    password = input('Type your password: ')
    return password

def convert_password_to_list(password):
    password_list = list(password)
    return password_list

def verify_possible_caracters_quantity(password_list):
    count_caracters = len(password_list)
    if count_caracters >= 8:
        return 1
    else:
        return 0

def verify_possible_upper_caracters(password_list):
    for i in password_list:
        if i.isupper():
            return 1
    return 0

def verify_possible_lower_caracters(password_list):
    for x in password_list:
        if x.islower():
            return 1
    return 0

def verify_possible_numbers(password_list):
    for e in password_list:
        if e.isdigit():
            return 1
    return 0

def verify_possible_special_caracters(password_list):
    for c in password_list:
        if c in SPECIAL_CARACTERS:
            return 1
    return 0 
    

def set_level_of_password_strengh(count_points):
    if count_points <= 2:
        password_level = 'Weak'
    elif count_points >= 5:
        password_level = 'Strong'
    else:
        password_level = 'Medium'
    print(f'Your password is {password_level}')
    return password_level

def main():
    password = get_user_password()

    password_list = convert_password_to_list(password)  

    count_points = 0
    count_points += verify_possible_caracters_quantity(password_list)
    count_points += verify_possible_upper_caracters(password_list)
    count_points += verify_possible_lower_caracters(password_list)
    count_points += verify_possible_numbers(password_list)
    count_points += verify_possible_special_caracters(password_list)

    password_level = set_level_of_password_strengh(count_points)

if __name__ == '__main__':
    main()
