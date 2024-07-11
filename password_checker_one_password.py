from password_validator.validator import PasswordValidator, ValidationError

try:
    validator = PasswordValidator('ZAQ!2wsx')
    print(validator.is_valid())
except ValidationError as error:
    print(error)
