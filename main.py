"""Password validator"""
from abc import ABC, abstractmethod
from hashlib import sha1
from requests import get


class ValidationError(Exception):
    """Exception for validation error"""


class Validator(ABC):
    """Interface for validators"""
    @abstractmethod
    def __init__(self, text):
        """Force to implement __init__ method"""
        self.text = text


    @abstractmethod
    def is_valid(self):
        """Force to implement is_valid method"""


class HasNumberValidator(Validator):
    """Validator checking if string contains number"""
    def __init__(self, text) -> None:
        self.text = text

    def is_valid(self):
        """Checks if text is valid

        Raises:
            ValidationError: no number in text, text is not valid

        Returns:
            bool: has number in text
        """
        if any(str(number) in self.text for number in range(10)):
            return True

        raise ValidationError('Text must contain number!')


class HasUpperCharacterValidator(Validator):
    """Validator checking if string contains upper letter"""
    def __init__(self, text) -> None:
        self.text = text

    def is_valid(self):
        """Checks if text is valid

        Raises:
            ValidationError: no upper letter in text, text is not valid

        Returns:
            bool: has upper letter in text
        """
        if any(character.isupper() for character in self.text):
            return True

        raise ValidationError('Text must contain upper letter!')


class HasLowerCharacterValidator(Validator):
    """Validator checking if string contains lower letter"""
    def __init__(self, text):
        self.text = text

    def is_valid(self):
        """Checks if text is valid

        Raises:
            ValidationError: no upper letter in text, text is not valid

        Returns:
            bool: has lower letter in text
        """
        if any(character.islower() for character in self.text):
            return True

        raise ValidationError('Text must contain lower letter!')


class HasSpecialCharacterValidator(Validator):
    """Validator checking if string contains special character"""
    def __init__(self, text):
        self.text = text

    def is_valid(self):
        """Checks if text is valid

        Raises:
            ValidationError: no special character in text, text is not valid

        Returns:
            bool: has special character in text
        """
        if any(not character.isalnum() for character in self.text):
            return True

        raise ValidationError('Text must contain special character!')


class LengthValidator(Validator):
    """Validator checking if string has min length"""
    def __init__(self, text, min_length=8) -> None:
        self.text = text
        self.min_length = min_length

    def is_valid(self):
        """Checks if text is valid

        Raises:
            ValidationError: text is too short and is not valid

        Returns:
            bool: text is long enough
        """
        if len(self.text) >= self.min_length:
            return True

        raise ValidationError('Text is too short!')


class HaveIbeenPwndValidator(Validator):
    """Validator checking if password is safe"""
    def __init__(self, password) -> None:
        self.password = password

    def is_valid(self):
        """Checks if password is leaked

        Raises:
            ValidationError: password is not valid, because is present in some leak

        Returns:
            bool: password is safe
        """
        hash_of_password = sha1(self.password.encode('utf-8')).hexdigest().upper()
        response = get('https://api.pwnedpasswords.com/range/' + hash_of_password[:5], timeout=10)

        for line in response.text.splitlines():
            if ':' in line:
                found_hash, _ = line.split(':')
                # _ => gdy zmienna jest nam niepotrzebna
                if found_hash == hash_of_password[5:]:
                    raise ValidationError('Leaked password! Choose another one!')
        return True


class PasswordValidator(Validator):
    """Validator checks if password is valid"""
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
        """Checks if password is valid

        Returns:
            bool: returns true if password passed all requirements
        """
        for class_name in self.validators:
            validator = class_name(self.password)
            if not validator.is_valid():
                return False
        return True
