
def is_adult(age: int) -> bool:
    return age >= 18


def test_is_adult():
    #given
    age = 19
    #when
    result = is_adult(age)
    #then
    assert result
    assert is_adult(20)

def test_is_not_adult():
    assert not is_adult(17)
    assert not is_adult(4)