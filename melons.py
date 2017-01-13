from random import randint
from datetime import date, time, datetime



class AbstractMelonOrder(object):

    def __init__(self, species, qty, month=None, country_code=None):

        self.species = species
        self.qty = qty
        self.shipped = False
        self.order_type = None
        self.country_code = country_code

    def get_base_price(self):
        base_price = 5
        # randint(5, 9)

        current = datetime.now()

        if current.weekday() < 7 and current.hour < 11:
            base_price += 3        

        return base_price

    def get_total(self, country_code=None):
        """Calculate price."""

        base_price = self.get_base_price()

        if self.species == "Christmas":
            base_price = base_price*1.5

        total = (1 + self.tax) * self.qty * base_price

        if country_code is not None and self.qty < 10:
            total += 3

        return total

    def mark_shipped(self):
        """Set shipped to true."""

        self.shipped = True


class DomesticMelonOrder(AbstractMelonOrder):
    """A domestic (in the US) melon order."""

    order_type = "domestic"
    tax = 0.08

    def __init__(self, species, qty):
        """Initialize melon order attributes"""

        super(DomesticMelonOrder, self).__init__(species, qty)


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    order_type = "international"
    tax = 0.17

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes"""

        # self.country_code = country_code

        super(InternationalMelonOrder, self).__init__(species, qty, country_code)

    def get_country_code(self):
        """Return the country code."""

        return self.country_code


class GovernmentMelonOrder(AbstractMelonOrder):
    """A government tax-free melon order."""

    order_type = "government"
    tax = 0.00
    passed_inspection = False

    def __init__(self, species, qty):
        """Initialize melon order attributes"""

        super(GovernmentMelonOrder, self).__init__(species, qty)

    def mark_inspection(self, passed):
        if passed is True:
            self.passed_inspection = True
