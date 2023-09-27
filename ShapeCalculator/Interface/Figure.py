from abc import ABC, abstractmethod


class Figure(ABC):
    @abstractmethod
    def get_area(self, *args, **kwargs):
        pass

    @staticmethod
    def _correct_args(*args):
        """ Checking the entered dimensions for shapes """

        if any(not isinstance(length, (int, float)) or length <= 0 for length in args):
            raise ValueError('The data is incorrect')

