"""Module contains prime numbers handling"""
from typing import Any

from error_types import OutOfRangeError, NegativeNumber, NotDecimalValueError


class PrimeNumber:
	"""Prime numbers handler"""
	MAXIMAL_VALUE = 9223372036854775807

	def validate_number(self, number: Any) -> None:
		"""Checks if number has correct format"""
		if len(number) > len("9223372036854775807"):
			raise OutOfRangeError
		elif not number.isdecimal():
			raise NotDecimalValueError
		elif int(number) not in range(0, self.MAXIMAL_VALUE + 1):
			raise OutOfRangeError
		elif not int(number):
			raise NegativeNumber
