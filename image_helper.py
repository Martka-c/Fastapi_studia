import cv2


class ImageHelper:

	@staticmethod
	def process_image(np_arr):
		# img = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)

		return_img = ImageHelper.process_image2(np_arr)
		# return_img = ImageHelper.process_image(img)
		cv2.imwrite(r'C:\Users\marta\PycharmProjects\studia_2_0\test_image.png', return_img)
		return return_img

	@staticmethod
	def process_image2(image):
		return cv2.bitwise_not(image)

