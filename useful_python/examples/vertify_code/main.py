

"""
只能最简单的验证码识别，验证码找打码平台
"""
import tesserocr
from PIL import Image
image = Image.open('./sina/FFHG6.jpg')
image = image.convert('L')
image = image.convert('1')
result = tesserocr.image_to_text(image)
print(result)
