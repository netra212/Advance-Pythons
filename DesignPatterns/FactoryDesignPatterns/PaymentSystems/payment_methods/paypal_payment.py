from .payment import Payment

class PayPalPayment(Payment):
    def pay(self, amount: float):
        print(f"Successfully Paid ${amount} to merchant using PayPal. ")