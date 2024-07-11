'''Check your passwords written in txt file if it's a safe password'''
from password_validator.validator import PasswordValidator, ValidationError

with (open('passwords.txt', encoding='utf-8') as input_file,
      open('safe.txt', 'w', encoding='utf-8') as output_file):
    for password in input_file:
        try:
            strip_password = password.strip()
            validator = PasswordValidator(strip_password)
            validator.is_valid()
            output_file.write(strip_password + '\n')
        except ValidationError as error:
            print(password, error)
