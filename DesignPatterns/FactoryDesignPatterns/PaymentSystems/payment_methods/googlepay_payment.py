from .payment import Payment

class GooglePayPayment(Payment):
    def pay(self, amount: float):
        print(f"Successfully Paid ${amount} to merchant using Google Pay. ")