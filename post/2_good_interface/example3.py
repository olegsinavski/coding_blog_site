from typing import Callable


class Creature:
    def act(self, *args, **kwargs) -> object:
        """ Do anything you want"""


def context_call(act_f: Callable, argument1, argument2):
    with some_context():
        return act_f(argument1, argument2)
