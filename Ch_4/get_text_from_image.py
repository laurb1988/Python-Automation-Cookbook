from PIL import Image
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
text = pytesseract.image_to_string(Image.open('images/photo-text.jpg'))
text2 = pytesseract.image_to_string(Image.open('images/Untitled.png'))
print(text2)