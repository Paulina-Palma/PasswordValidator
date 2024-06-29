import pytest

from main import (
    HasNumberValidator,
    HasSpecialCharacterValidator,
    HasUpperCharacterValidator,
    HasLowerCharacterValidator,
    LengthValidator,
    HaveIbeenPwndValidator,
    ValidationError,
    PasswordValidator
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
    with pytest.raises(ValidationError) as error:
        validator.is_valid()
        assert 'Text must contain number!' in str(error.value)


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
    with pytest.raises(ValidationError) as error:
        validator.is_valid()
        assert 'Text must contain upper letter!' in str(error.value)

def test_if_has_lower_character_validator_positive():
    #given
    validator = HasLowerCharacterValidator('aaaAAA')

    #when
    result = validator.is_valid()

    #then
    assert result is True


def test_if_has_lower_character_validator_negative():
    #given
    validator = HasLowerCharacterValidator('ABC')

    #when
    with pytest.raises(ValidationError) as error:
        validator.is_valid()
        assert 'Text must contain lower letter!' in str(error.value)

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
    with pytest.raises(ValidationError) as error:
        validator.is_valid()
        assert 'Text must contain special character!' in str(error.value)

def test_if_length_validator_positive():
    #given
    validator = LengthValidator('123456789')

    #when
    result = validator.is_valid()

    #then
    assert result is True

    # given
    validator = LengthValidator('123', 3)

    # when
    result = validator.is_valid()

    # then
    assert result is True


def test_if_length_validator_negative():
    #given
    validator = LengthValidator('abc')

    #when
    with pytest.raises(ValidationError) as error:
        validator.is_valid()
        assert 'Text is too short!' in str(error.value)

    # given
    validator = LengthValidator('12345678', 9)

    # when
    with pytest.raises(ValidationError) as error:
        validator.is_valid()
        assert 'Text is too short!' in str(error.value)

def test_have_I_been_pwnd_validator_positive(requests_mock):
    #given
    data = '1008262DEF912C463846C28AA21194873B4:10\n\r00108373D7CC7F3C6CB34752B8F17B2A059:3'
    requests_mock.get('https://api.pwnedpasswords.com/range/415E1', text=data)
    validator = HaveIbeenPwndValidator('JolkaJolka')

    #when
    result = validator.is_valid()

    #then
    assert result is True


def test_have_I_been_pwnd_validator_negative(requests_mock):
    #given
    data = '15D8262DEF912C463846C28AA21194873B4:10\n\r00108373D7CC7F3C6CB34752B8F17B2A059:3'
    requests_mock.get('https://api.pwnedpasswords.com/range/415E1', text=data)
    validator = HaveIbeenPwndValidator('JolkaJolka')

    #when
    with pytest.raises(ValidationError) as error:
        validator.is_valid()
        assert 'Text must contain special character!' in str(error.value)

def test_password_validator_positive():
    #given
    validator = PasswordValidator('Jolkajolka1234!')

    #when
    result = validator.is_valid()

    #then
    assert result is True

def test_password_validator_negative():
    validator = PasswordValidator('jolkajolka1234!')

    with pytest.raises(ValidationError) as error:
        validator.is_valid()
        assert 'Text must contain upper letter!' in str(error.value)
