import image_lsb
import key_image_lsb

name = 'prigodich vera valeryevna'
with open('report.txt', encoding="utf8") as f:
    report = f.read()


image_lsb.encode(name, 'images/kodim23.png', 'images/name.png')
decoded = image_lsb.decode('images/name.png')
print(f'Decoded image: {decoded}\n')

image_lsb.encode(report, 'images/kodim23.png', 'images/report.png')
decoded = image_lsb.decode('images/report.png')
print(f'Decoded image: {decoded}\n\n')

print('\nLSB with key\n')

key_image_lsb.encode(name, 'images/kodim23.png', 'images/key_name.png', 'key.txt')
decoded = key_image_lsb.decode('images/key_name.png', 'key.txt')
print(f'Decoded image: {decoded}\n')

key_image_lsb.encode(report, 'images/kodim23.png', 'images/key_report.png', 'key.txt')
decoded = key_image_lsb.decode('images/key_report.png', 'key.txt')
print(f'Decoded image: {decoded}\n\n')