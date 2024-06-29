from requests import get
from hashlib import sha1
from abc import ABC, abstractmethod

class ValidationError(Exception):
    pass


class Validator(ABC):
    @abstractmethod
    def __init__(self, text):
        self.text = text


    @abstractmethod
    def is_valid(self):
        pass


class HasNumberValidator(Validator):
    def __init__(self, text) -> None:
        self.text = text

    def is_valid(self):
        if any(str(n) in self.text for n in range(10)):
            return True
        else:
            raise ValidationError('Text must contain number!')
        # for n in range(0, 10):
        #     if str(n) in self.text:
        #         return True
        # return False


class HasUpperCharacterValidator(Validator):
    def __init__(self, text) -> None:
        self.text = text

    def is_valid(self):
        if any([character.isupper() for character in self.text]):
            return True
        else:
            raise ValidationError('Text must contain upper letter!')


class HasLowerCharacterValidator(Validator):
    def __init__(self, text):
        self.text = text

    def is_valid(self):
        if any([character.islower() for character in self.text]):
            return True
        else: 
            raise ValidationError('Text must contain lower letter!')


class HasSpecialCharacterValidator(Validator):
    def __init__(self, text):
        self.text = text

    def is_valid(self):
        # temp_list = []
        # for character in self.text:
        #     temp_list.append(not character.isalnum())
        #     # if not character.isalnum():
        #     #     return True
        # return any(temp_list)
        if any([not character.isalnum() for character in self.text]):
            return True
        else:
            raise ValidationError('Text must contain special character!')

class LengthValidator(Validator):
    def __init__(self, text, min_length=8) -> None:
        self.text = text
        self.min_length = min_length

    def is_valid(self):
        if len(self.text) >= self.min_length:
            return True
        else:
            raise ValidationError(f'Text is too short!')

class HaveIbeenPwndValidator(Validator): 
#powinien być na końcu, bo łączy się z API, czyli najpierw dobrze trzeba przetestować hasło, a na koniec spr czy nie wyciekło

    def __init__(self, password) -> None:
        self.password = password

    def is_valid(self):
        hash = sha1(self.password.encode('utf-8')).hexdigest().upper()
        response = get('https://api.pwnedpasswords.com/range/' + hash[:5])

        for line in response.text.splitlines():
            if ':' in line:
                found_hash, _ = line.split(':')
                # _ => gdy zmienna jest nam niepotrzebna
                if found_hash == hash[5:]:
                    raise ValidationError('Leaked password! Choose another one!')
        return True

class PasswordValidator(Validator):
    def __init__(self, password):
        self.password = password
        self.validators = [
            LengthValidator,
            HasNumberValidator,
            HasSpecialCharacterValidator,
            HasUpperCharacterValidator,
            HasLowerCharacterValidator,
            HaveIbeenPwndValidator,
        ]

    def is_valid(self):
        for class_name in self.validators:
            validator = class_name(self.password)
            if not validator.is_valid():
                return False
        return True
