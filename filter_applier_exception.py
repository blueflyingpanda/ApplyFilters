NO_LOCATION = 0
INVALID_JSON = 1
BAD_FILTER = 2
BAD_FILTER_NAME = 3


class FilterApplierException(Exception):

    def __init__(self, issue, *args):
        if issue == NO_LOCATION:
            msg = f'incorrect input location {args[0]}'
        elif issue == INVALID_JSON:
            msg = f'invalid json {args[0]}\noriginal error {args[1]}'
        elif issue == BAD_FILTER:
            msg = f'filter raised an exception {args[0]} in file {args[1]}\nFinishing...'
        elif issue == BAD_FILTER_NAME:
            msg = f'no such filter in filters.py {args[0]}'
        super().__init__(msg)
