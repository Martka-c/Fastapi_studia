"""Module contains classes to process images"""
import os
import cv2
import numpy


class ImageHelper:
	"""
	Processing images class
	"""

	@staticmethod
	def process_image(np_arr: numpy.ndarray) -> numpy.ndarray:
		"""
		converts image into inverted form and save it in current location
		:param np_arr: image in numpy array format
		:return: processed image
		"""
		return_img = ImageHelper.get_inversed_image(np_arr)
		cv2.imwrite(os.path.join("test_image.png"), return_img)
		return return_img

	@staticmethod
	def get_inversed_image(image: numpy.ndarray) -> numpy.ndarray:
		"""
		inverses image
		:param image: image in numpy array format
		:return: inverted image
		"""
		return cv2.bitwise_not(image)

