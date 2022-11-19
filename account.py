class Account:
    def __init__(self, name: str) -> None:
        """
        inputs the user's name and sets the account balance to 0
        :param name:str -> None
        """

        self.__account_name = name
        self.__account_balance = 0

    def deposit(self, amount: float) -> bool:
        """
        Checks to see if the amount inputted is greater than 0

        :param amount: -> float
        :return: -> bool
        """
        if amount <= 0:
            return False
        else:
            self.__account_balance += amount
            return True

    def withdraw(self, amount: float) -> bool:
        """
        Checks to see if the amount inputted is greater than 0 and the current balance

        :param amount: -> float
        :return: -> bool
        """
        if amount <= 0 or amount > self.__account_balance:
            return False
        else:
            self.__account_balance -= amount
            return True

    def get_balance(self) -> float:
        """
        returns the balance of the account
        :return: -> float
        """
        return self.__account_balance

    def get_name(self) -> str:
        """
        returns the name on the account
        :return: -> str
        """
        return self.__account_name
