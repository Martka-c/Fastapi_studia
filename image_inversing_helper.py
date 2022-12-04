import os

import cv2


class ImageHelper:

	@staticmethod
	def process_image(np_arr):
		return_img = ImageHelper.process_image2(np_arr)
		cv2.imwrite(os.path.join("test_image.png"), return_img)
		return return_img

	@staticmethod
	def process_image2(image):
		return cv2.bitwise_not(image)

