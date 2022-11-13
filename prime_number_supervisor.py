from error_types import OutOfRangeError, NegativeNumber, NotDecimalValueError


class PrimeNumber:

	@staticmethod
	def validate_number(number):
		if not number.isdecimal():
			raise NotDecimalValueError
		elif int(number) not in range(0, 9223372036854775807 + 1):
			raise OutOfRangeError
		elif not int(number):
			raise NegativeNumber

