from .payment import Payment

class CreditCardPayment(Payment):
    def pay(self, amount: float):
        print(f"Successfully Paid ${amount} to merchant using a Credit Card. ")