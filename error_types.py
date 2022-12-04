""" Module contains classes representing errors that could happen"""


class BaseError(Exception):
	"""Base error class"""
	message: str


class OutOfRangeError(BaseException):
	"""
	Raised if entered number is too large
	"""


class NegativeNumber(BaseException):
	"""
	Raised if entered number is negative
	"""


class NotDecimalValueError(BaseException):
	"""
	Raised if entered value is not decimal
	"""
