from abc import ABC, abstractmethod

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
        for n in range(0, 10):
            if str(n) in self.text:
                return True
        return False


class HasUpperCharacterValidator(Validator):
    def __init__(self, text) -> None:
        self.text = text

    def is_valid(self):
        return any([character.isupper() for character in self.text])


class HasLowerCharacterValidator(Validator):
    def __init__(self, text):
        self.text = text

    def is_valid(self):
        return any([character.islower() for character in self.text])


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
        return any([not character.isalnum() for character in self.text])

class LenghtValidator(Validator):
    def __init__(self, text, min_lenght):
        self.text = text
        self.min_lenght = min_lenght

    def is_valid(self):
    #     if len(self.text) >= self.min_lenght:
    #         return True
    #   return False
        return len(self.text) >= self.min_lenght

class HaveIbeenPwndValidator(Validator): #powinien być na końcu, bo łączy się z API, czyli najpiwer dobrze trzeba przetestować hasło, a na koniec spr czy nie wyciekło

    def __init__(self, text):
        self.text = text

    def is_valid(self):
        pass


class PasswordValidator(Validator):
    def __init__(self, password):
        self.password = password
        self.validators = [
            LenghtValidator,
            HasNumberValidator,
            HasSpecialCharacterValidator,
            HasUpperCharacterValidator,
            HasLowerCharacterValidator,
            HaveIbeenPwndValidator,
        ]

    def is_valid(self):
        for class_name in self.validators:
            validator = class_name(self.password)
            validator.is_valid()


validator = PasswordValidator('qwerty')
print(validator.is_valid())
