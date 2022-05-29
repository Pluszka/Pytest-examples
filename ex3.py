import pytest

class Bank:
    def __init__(self):
        self.amount = 0

    def deposit(self, money: int):
        self.amount += money

    def withdraw(self, money: int):
        if money > self.amount:
            raise NotEnoughMoney
        self.amount -= money
        return money

class NotEnoughMoney(Exception):
    pass

class TestBank:
    def test_create(self):
        bank = Bank()
        assert bank.amount == 0
        assert isinstance(bank, Bank)

    def test_deposit(self):
        #given
        bank = Bank()
        #when
        bank.deposit(60)
        #then
        assert bank.amount == 60

    def test_deposite_twice(self):
        #given
        bank = Bank()
        #when
        bank.deposit(60)
        bank.deposit(60)
        #then
        assert bank.amount == 120

    def test_withdraw(self):
        #given
        bank = Bank()
        bank.deposit(200)
        #when
        money = bank.withdraw(60)
        #then
        assert money == 60
        assert bank.amount == 140

    def overWithdraw(self):
        with pytest.raises(NotEnoughMoney):
            bank = Bank()
            bank.withdraw(58)