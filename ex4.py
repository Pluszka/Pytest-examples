import pytest

def sort_by(names, first_letter=False, last=False, lenght=False):
    if first_letter:
        names.sort()
    elif last:
        names.sort(key=lambda name : name[::-1])
    elif lenght:
        names.sort(key=len)
    return names

class TestSort:
    @pytest.fixture
    def names(self):
        return ['Ania', 'Ola', 'Adam', 'Staś']

    def test_sort(self, names):
        sorted =  sort_by(names, first_letter=True)
        assert sorted == ['Adam', 'Ania', 'Ola', 'Staś']

    def test_reverse(self, names):
        sorted = sort_by(names, last=True)
        assert  sorted == ['Ania', 'Ola', 'Adam', 'Staś']

    def sort_len(self, names):
        sorted = sort_by(names, lenght=True)
        assert sorted == ['Ola', 'Ania', 'Adam', 'Staś']