class BaseError(Exception):
	message: str


class OutOfRangeError(BaseException):
	pass


class NegativeNumber(BaseException):
	pass


class NotDecimalValueError(BaseException):
	pass
