from commands import *


class Filterable(object):
    def __init__(self, iterable):
        self.iterable = iterable

    def __iter__(self):
        return iter(self.iterable)

    def __repr__(self):
        return '<Filterable: %s>' % repr(self.iterable)

    def filter(self, *callables, **constraints):
        return self.__execute_command(FilterCommand, *callables, **constraints)

    def exclude(self, *callables, **constraints):
        return self.__execute_command(ExcludeCommand, *callables, **constraints)

    def order_by(self, *keys):
        return self.__execute_command(OrderCommand, *keys)

    def get(self, *callables, **constrains):
        return self.__execute_command(GetCommand, *callables, **constrains)

    def count(self):
        return self.__execute_command(CountCommand)

    def sum(self, attr):
        return self.__execute_command(SumCommand, attr)

    def exists(self):
        return self.__execute_command(ExistsCommand)

    def __execute_command(self, cls, *args, **kwargs):
        return self.__build_command(cls, *args, **kwargs).execute()

    def __build_command(self, cls, *args, **kwargs):
        return cls(self, self.iterable, *args, **kwargs)
