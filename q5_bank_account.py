"""
Question 5: Customer & Account Classes (Composition)
- Customer: name, surname, tc_identification, phone
- Account: customer (Customer object), account_number, balance
By Waseem
"""


class Customer:
    """Represents a bank customer."""

    def __init__(self, name, surname, tc_identification, phone):
        self.name = name
        self.surname = surname
        self.tc_identification = tc_identification
        self.phone = phone

    def display_information(self):
        """Display the customer's personal information."""
        print("\n" + "=" * 45)
        print("👤 CUSTOMER INFORMATION")
        print("=" * 45)
        print(f"Name:      {self.name} {self.surname}")
        print(f"TC ID:     {self.tc_identification}")
        print(f"Phone:     {self.phone}")
        print("=" * 45)

    def __str__(self):
        return f"{self.name} {self.surname} (TC: {self.tc_identification})"

    def __repr__(self):
        return (
            f"Customer(name={self.name!r}, surname={self.surname!r}, "
            f"tc={self.tc_identification!r}, phone={self.phone!r})"
        )


class Account:
    """Represents a bank account that belongs to a Customer."""

    def __init__(self, customer, account_number, balance=0.0):
        self.customer = customer          # Customer object
        self.account_number = account_number
        self.balance = balance

    # ---------- Deposit ----------
    def deposit(self, amount):
        """Deposit money into the account."""
        if amount <= 0:
            print("❌ Deposit amount must be greater than 0.")
            return
        self.balance += amount
        print(f"✅ Deposited ${amount:.2f}. New balance: ${self.balance:.2f}")

    # ---------- Withdraw (money_check) ----------
    def money_check(self, amount):
        """Withdraw money if balance is sufficient."""
        if amount <= 0:
            print("❌ Withdrawal amount must be greater than 0.")
            return
        if amount > self.balance:
            print(f"❌ Insufficient balance! You have ${self.balance:.2f}, "
                  f"but tried to withdraw ${amount:.2f}.")
            return
        self.balance -= amount
        print(f"✅ Withdrew ${amount:.2f}. New balance: ${self.balance:.2f}")

    # ---------- Display Balance ----------
    def display_balance(self):
        """Display the current account balance."""
        print("\n" + "=" * 45)
        print(f"💰 Account: {self.account_number}")
        print(f"   Owner:   {self.customer.name} {self.customer.surname}")
        print(f"   Balance: ${self.balance:.2f}")
        print("=" * 45)

    def __str__(self):
        return (
            f"Account({self.account_number}) — "
            f"{self.customer.name} {self.customer.surname} — ${self.balance:.2f}"
        )

    def __repr__(self):
        return (
            f"Account(customer={self.customer!r}, "
            f"account_number={self.account_number!r}, balance={self.balance})"
        )


# ---------- Testing ----------
if __name__ == "__main__":
    # 1. Create a Customer object
    customer = Customer(
        name="Ahmed",
        surname="Yılmaz",
        tc_identification="12345678901",
        phone="+90 555 123 4567",
    )

    # 2. Create an Account object and attach the customer
    account = Account(
        customer=customer,
        account_number="TR12 3456 7890 1234 5678 9012 34",
        balance=1000.0,
    )

    # 3. Display customer info
    customer.display_information()

    # 4. Display initial balance
    account.display_balance()

    # 5. Perform operations
    print("\n--- Operations ---")
    account.deposit(500)        # ✅ Deposit 500
    account.money_check(200)    # ✅ Withdraw 200
    account.money_check(5000)   # ❌ Insufficient balance
    account.deposit(-50)        # ❌ Invalid deposit

    # 6. Display final balance
    account.display_balance()

    # 7. Summary
    print(f"\n📊 Account Summary: {account}")