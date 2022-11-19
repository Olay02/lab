import pytest
from account import *


class Test:
    def setup(self):
        self.acc = Account('Carter')

    def test_init(self):
        assert self.acc.get_name() == 'Carter'
        assert self.acc.get_balance() == 0

    def test_deposit(self):
        assert self.acc.deposit(30) is True
        assert self.acc.get_balance() == 30
        assert self.acc.deposit(-30) is False
        assert self.acc.get_balance() == 30
        assert self.acc.deposit(0) is False
        assert self.acc.get_balance() == 30
        assert self.acc.deposit(125.5) is True
        assert self.acc.get_balance() == pytest.approx(155.5, abs=0.001)

    def test_withdraw(self):
        assert self.acc.withdraw(0) is False
        assert self.acc.get_balance() == 0
        assert self.acc.withdraw(-400) is False
        assert self.acc.get_balance() == 0
        assert self.acc.withdraw(-0.1) is False
        assert self.acc.get_balance() == 0

        assert self.acc.deposit(1000) is True
        assert self.acc.withdraw(500) is True
        assert self.acc.get_balance() == 500
        assert self.acc.withdraw(45.75) is True
        assert self.acc.get_balance() == pytest.approx(454.25, abs=0.001)


