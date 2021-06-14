from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS
import xmltodict
from gps_conversion import exif_to_decimal, rdf_to_decimal

images_dir = 'images'
image1 = Image.open(images_dir + '/photo-dublin-a1.jpg')
print(image1.height)
print(image1.width)
print(image1.format)
exif_info_1 = {TAGS.get(tag, tag): value for tag, value in image1._getexif().items()}
print(exif_info_1['Model'])
print(exif_info_1['LensModel'])
print(exif_info_1['DateTimeOriginal'])
#print(exif_info_1)

print('###############IMAGE 2###############')

image2 = Image.open(images_dir + '/photo-dublin-a2.png')
print(image2.height)
print(image2.width)
print(image2.format)
xmp_info = xmltodict.parse(image2.info['XML:com.adobe.xmp'])
rdf_ino_2 = xmp_info['x:xmpmeta']['rdf:RDF']['rdf:Description']
print(rdf_ino_2['tiff:Model'])
print(rdf_ino_2['exifEX:LensModel'])
print(rdf_ino_2['xmp:CreateDate'])

gps_info_1 = {GPSTAGS.get(tag, tag): value for tag, value in exif_info_1['GPSInfo'].items()}
exif_to_decimal(gps_info_1)