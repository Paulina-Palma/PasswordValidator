from main import (
    HasNumberValidator,
    HasSpecialCharacterValidator,
    HasUpperCharacterValidator,
    HasLowerCharacterValidator
)


def test_if_has_number_validator_positive():
    #given
    validator = HasNumberValidator('abc1')

    #when
    result = validator.is_valid()

    #then
    assert result is True


def test_if_has_number_validator_negative():
    #given
    validator = HasNumberValidator('abc')

    #when
    result = validator.is_valid()

    #then
    assert result is False

def test_if_has_special_character_validator_positive():
    #given
    validator = HasSpecialCharacterValidator('a!bc#1')

    #when
    result = validator.is_valid()

    #then
    assert result is True


def test_if_has_special_character_validator_negative():
    #given
    validator = HasSpecialCharacterValidator('abc')

    #when
    result = validator.is_valid()

    #then
    assert result is False

def test_if_has_upper_character_validator_positive():
    #given
    validator = HasUpperCharacterValidator('aaaAAA')

    #when
    result = validator.is_valid()

    #then
    assert result is True


def test_if_has_upper_character_validator_negative():
    #given
    validator = HasUpperCharacterValidator('abc')

    #when
    result = validator.is_valid()

    #then
    assert result is False

def test_if_has_lower_character_validator_positive():
    #given
    validator = HasLowerCharacterValidator('aaaAAA')

    #when
    result = validator.is_valid()

    #then
    assert result is True


def test_if_has_lower_character_validator_negative():
    #given
    validator = HasLowerCharacterValidator('abc')

    #when
    result = validator.is_valid()

    #then
    assert result is False
