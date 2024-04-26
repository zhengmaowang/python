1 import pytesseract
2 from PIL import Image
3 # 读取图片
4 im = Image.open('sentence.jpg')
5 # 识别文字
6 string = pytesseract.image_to_string(im)
7 print(string)
