from connection import connection


class Account:

    def __init__(self, name: str, opening_balance: float = 0.0) -> None:
        with connection.cursor() as cursor:
            cursor.execute("INSERT INTO accounts (name, balance) VALUES (?,?)",
                           (name, opening_balance))
            cursor.execute('SELECT @@IDENTITY AS ID')
            # (215315,)
            self.id = cursor.fetchone()[0]
            self.name = name
            self.__balance = opening_balance
        print(f"Konto {name} zostało utworzone")

    def deposit(self, amount: float):
        if amount <= 0:
            print("Wartość depozytu musi być większa od 0")
            return

        self.__balance += amount
        with connection.cursor() as cursor:
            cursor.execute("UPDATE accounts SET balance = ? WHERE account_id = ?",
                           (self.__balance, self.id))

        print(f"{amount} zostało dodane do konta {self.name}")

    def withdrawal(self, amount: float):
        if amount <= 0 or self.__balance < amount:
            print(f"Wartość wypłaty musi być większa od 0 i mniejsza od {self.__balance}")
            return

        self.__balance -= amount
        with connection.cursor() as cursor:
            cursor.execute("UPDATE accounts SET balance = ? WHERE account_id = ?",
                           (self.__balance, self.id))

        print(f"{amount} zostało wypłacone z konta {self.name}")


account_one = Account('Maciej', 20)
account_one.deposit(100)
account_one.withdrawal(90)
