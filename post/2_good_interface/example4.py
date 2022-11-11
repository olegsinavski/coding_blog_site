

from typing import Callable


class Sausage:
    def price(self) -> float:
        pass

    def weight(self) -> float:
        pass


class SausageMachine:
    def make_sausage(self) -> Sausage:
        ...


def make_two_sausages(sausage_maker_function: Callable[Any, Sausage]):
    one = sausage_maker_function()
    two = sausage_maker_function()


make_two_sausages(SausageMachine().make_sausage)
make_two_sausages(Sausage.__init__)
