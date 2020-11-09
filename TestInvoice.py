import pytest
from Invoice import Invoice


@pytest.fixture()
def products():
    products = {'Pen': {'qnt': 10, 'unit_price': 3.75, 'discount': 5},
                'Notebook': {'qnt': 5, 'unit_price': 7.5, 'discount': 10}}
    return products


# return the test invoice
@pytest.fixture()
def invoice():
    invoice = Invoice()
    return invoice


# first test
def test_CanCalucateTotalImpurePrice(invoice, products):
    invoice.totalImpurePrice(products)
    assert invoice.totalImpurePrice(products) == 75


# second test
def test_CanCalucateTotalDiscount(invoice, products):
    invoice.totalDiscount(products)
    assert invoice.totalDiscount(products) == 5.62


# third test
def test_CanCalucateTotalPurePrice(invoice, products):
    invoice.totalPurePrice(products)
    assert invoice.totalPurePrice(products) == 69.38

# four test
def test_ProductDouble(invoice, products):
    invoice.productDouble(products)
    assert invoice.productDouble(products) == 138.76
# fifth test
def test_TripleDiscount(invoice, products):
    invoice.tripleDiscount(products)
    assert invoice.tripleDiscount(products) == 58.14
# six test
def test_TotalQuantity(invoice, products):  # @author: Sean Epley
    invoice.totalQnt(products)
    assert invoice.totalQnt(products) == 10