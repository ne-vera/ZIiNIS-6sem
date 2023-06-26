from PIL import Image, ImageDraw 
from random import randint		
from re import findall

def encode(message, img_path, new_img_path, key_path):	
	img = Image.open(img_path) 	# создаём объект изображения
	draw = ImageDraw.Draw(img)	   		# объект рисования
	width = img.size[0]  		   		# ширина
	height = img.size[1]		   		# высота	
	pix = img.load()				# все пиксели тут
	f = open(key_path,'w')			# текстовый файл для ключей

	for elem in ([ord(elem) for elem in message]):
		key = (randint(1,width-10),randint(1,height-10))		
		g, b = pix[key][1:3]
		draw.point(key, (elem,g , b))														
		f.write(str(key)+'\n')								
	
	print(f'keys were written to the  {key_path} file')
	img.save(new_img_path, "PNG")
	f.close()
											
def decode(img_path, key_path):
	
	a = []						    
	keys = []
	img = Image.open(img_path)				
	pix = img.load()
	f = open(key_path,'r')
	y = str([line.strip() for line in f])				
															
	for i in range(len(findall(r'\((\d+)\,',y))):
		keys.append((int(findall(r'\((\d+)\,',y)[i]),int(findall(r'\,\s(\d+)\)',y)[i]))) 	
	for key in keys:
		a.append(pix[tuple(key)][0])							
	return ''.join([chr(elem) for elem in a])	