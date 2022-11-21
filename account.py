class Account:
    def __init__(self, name: str) -> None:
        """
        Function to get name and sets account balance to 0
        :param name: Person's name
        """

        self.__account_name = name
        self.__account_balance = 0

    def deposit(self, amount: float) -> bool:
        """
        Function to deposit amount inputted into account

        param amount: amount number
        :return: True or False
        """
        if amount <= 0:
            return False
        else:
            self.__account_balance += amount
            return True

    def withdraw(self, amount: float) -> bool:
        """
        Function to withdraw the amount inputted from account
        :param amount: amount number
        :return: True or False
        """
        if amount <= 0 or amount > self.__account_balance:
            return False
        else:
            self.__account_balance -= amount
            return True

    def get_balance(self) -> float:
        """
        Gets the accounts balance
        :return: returns the accounts balance
        """
        return self.__account_balance

    def get_name(self) -> str:
        """
        Gets the name on the account
        :return: return the accounts name
        """
        return self.__account_name
