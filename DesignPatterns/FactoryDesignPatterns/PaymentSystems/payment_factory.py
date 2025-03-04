from inspect import getmembers, isclass, isabstract
import payment_methods

class PaymentFactory(object):
    # since dict is key value pair so. 
    # key: name of the class. 
    # value: actual class type. 
    payment_impmentation = {}

    def __init__(self):
        self.load_payment_methods()

    def load_payment_methods(self):
        # getmembers(): return all members of an object as (name, value) pairs sorted by name. 
        implementations = getmembers(payment_methods, lambda m: isclass(m) and not isabstract(m))
        for name, _type in implementations:
            if isclass(_type) and issubclass(_type, payment_methods.Payment):
                self.payment_impmentation[name] = _type
    
    def create(self, payment_type: str):
        if payment_type in self.payment_impmentation:
            return self.payment_impmentation[payment_type]()
        else:
            raise ValueError(f"{payment_type} is not currently supported as a payment method.")