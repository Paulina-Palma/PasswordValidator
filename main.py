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
        pass


class HasLowerCharacterValidator(Validator):
    def __init__(self, text):
        self.text = text

    def is_valid(self):
        pass


class HasSpecialCharacterValidator(Validator):
    def __init__(self, text):
        self.text = text

    def is_valid(self):
        pass


class LenghtValidator(Validator):
    def __init__(self, text):
        self.text = text

    def is_valid(self):
        pass


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
