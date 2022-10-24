from wallet import Wallet


def test_amount():

    wa = Wallet(10000)

    a = wa.spend_cash(40000)
    print("total amout left in wallet:", a)
    b = wa.add_cash(300)
    print("total amount in wallet:", b)

