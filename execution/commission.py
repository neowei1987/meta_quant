from util.number import float_floor


class CommissionHelper(object):
    """
       Handles order execution via the Interactive Brokers
       API, for use against accounts when trading live
       directly.
       """

    def __init__(self, commission_mode, commission_value):
        self.commission_mode = commission_mode
        self.commission_value = commission_value

    def get_commission(self, order_cost):
        if self.commission_mode == "FIXED":
            return self.commission_value
        else:
            return order_cost * self.commission_value

    def get_max_quantity(self, cash, price):
        if self.commission_mode == "FIXED":
            return float_floor((cash - self.commission_value) / price, 5)
        else:
            return float_floor((cash / ((1 + self.commission_value) * price)), 5)

    def calculate_ib_commission(self):
        full_cost = 1.3
        if self.quantity <= 500:
            full_cost = max(1.3, 0.013 * self.quantity)
        else:  # Greater than 500
            full_cost = max(1.3, 0.008 * self.quantity)
        return full_cost
