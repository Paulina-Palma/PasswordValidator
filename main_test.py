from main import HasNumberValidator

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
