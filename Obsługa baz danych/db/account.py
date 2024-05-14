from connection import connection


class Account:
    def __init__(self, name: str, opening_balance: float = 0.0) -> None:
        with connection.cursor() as cursor:
            cursor.execute("INSERT INTO accounts (name, balance) VALUES (?,?)",
                           (name, opening_balance))
            cursor.execute('SELECT @@IDENTITY AS ID')
            self.id = cursor.fetchone()[0]
            self.name = name
            self.__balance = opening_balance
        print(f"Konto {name} zostało utowrzone")

    def deposit(self, amount: float, commit: bool):
        if amount <= 0:
            raise ValueError('Wartość depozytu musi być większa od 0')

        self.__balance += amount

        connection.execute("UPDATE accounts SET balance = ? WHERE account_id = ?",
                           (self.__balance, self.id))
        if commit:
            connection.commit()
        print(f"{amount} zostało dodane do konta {self.name}")

    def withdrawal(self, amount: float, commit: bool):
        if amount <= 0 or self.__balance < amount:
            raise ValueError(f"Wartość wypłaty musi być większa od 0 i mniejsza od {self.__balance}")

        self.__balance -= amount

        connection.execute("UPDATE accounts SET balance = ? WHERE account_id = ?",
                           (self.__balance, self.id))
        if commit:
            connection.commit()
        print(f"{amount} zostało wypłacone z konta {self.name}")


def do_transaction(account_from: Account, account_to: Account, amount: float):
    try:
        account_to.deposit(amount, False)
        account_from.withdrawal(amount, False)
        connection.commit()
    except ValueError as ex:
        print(ex)
        connection.rollback()


# account_one = Account('Andrzej', 20)
# account_one.deposit(100)
# account_one.withdrawal(90)
# print(account_one.id)

account_one = Account('Maciej', 100)
account_two = Account('Andrzej', 50)
account_one.deposit(50, True)
do_transaction(account_two, account_one, 60)
