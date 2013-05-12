import pygame
from pygame.locals import *
import Image
import math
 
pygame.init()
pantalla = pygame.display.set_mode((190,250))

# FOTO NORMAL
imagen = pygame.image.load("imagen.jpg")


#FOTO ESCALA DE GRISES
image = Image.open("rayas.jpg")
pixeles = image.load()
ancho, altura =image.size 

for x in range(ancho):
 for y in range(altura): 
  (r,g,b) = image.getpixel((x,y))
 #  promedio=((r+g+b)/3) 
   
  pixeles[x,y] = (255,255,0)
image.save('gris.png', 'png')  
#image.show()   



#FOTO Invertida
image = Image.open("cuadrado.jpg")
pixeles = image.load()
ancho, altura =image.size 

for x in range(ancho):
 for y in range(altura): 
  (r,g,b) = image.getpixel((x,y))
  if (r>0 and g>0 and b>0):
      r=255-r
      g=255-g
      b=255-b
  pixeles[x,y] = (r,g,b)
#image.show() 

#FOTO binarizada con un umbral
image = Image.open("imagen.jpg")
pixeles = image.load()
ancho, altura =image.size 

for x in range(ancho):
 for y in range(altura): 
    (r,g,b) = image.getpixel((x,y))
    
    if (r<128 and g<128 and b<128):
      r=0
      g=0
      b=0
    if (r>128 and g>128 and b>128):
      r=255
      g=255
      b=255
    
    pixeles[x,y] = (r,g,b)

#image.show()    

#FOTO Escala de grises con binarizacion
image = Image.open("imagen.jpg")
pixeles = image.load()
ancho, altura =image.size 

for x in range(ancho):
 for y in range(altura): 
    (r,g,b) = image.getpixel((x,y))
    promedio=((r+g+b)/3)  
    if (promedio<=128 and promedio<=128 and promedio<=128):
      r=0
      g=0
      b=0
    else:
      r=255
      g=255
      b=255
    
    pixeles[x,y] = (r,g,b)
#image.show()    


#FOTO binarizada con dos UMBRALes
image = Image.open("s.png")
pixeles = image.load()
ancho, altura =image.size 

for x in range(ancho):
  for y in range(altura): 
    (r,g,b) = image.getpixel((x,y))
    promedio = (r+g+b/3)   
    if promedio <= 100:
     r=200
     g=0
     b=0
    if promedio >= 220:
     r=255
     g=255
     b=255  
     pixeles[x,y] = (promedio,promedio,promedio)
#image.save('sololo.png', 'png') 
#image.show()     


#FOTO PLATEADAS
image = Image.open("imagen.jpg")
pixeles = image.load()
ancho, altura =image.size 

for x in range(ancho):
 for y in range(altura): 
   (r,g,b) = image.getpixel((x,y))
   promedio =((r-80)+(g-80)+(b-80)/3) 
   pixeles[x,y] = (promedio,promedio,promedio)
#image.show()     

#Foto Borrosa
image = Image.open("Cancer.jpg")
pixeles = image.load()
ancho, altura =image.size 
numero=raw_input("Teclea el numero de filtro que quieres ")
numerofiltro=int(numero)

for z in range(numerofiltro):
   for x in range(ancho):
    for y in range(altura):
     arreglopixel = []
     arreglopixel.append(list(pixeles[x, y]))
            
     if x > 0:
      arreglopixel.append(list(pixeles[x-1, y]))
     if y > 0:
      arreglopixel.append(list(pixeles[x, y-1]))
     if x < ancho-1:
      arreglopixel.append(list(pixeles[x+1, y]))
     if y < altura-1:
      arreglopixel.append(list(pixeles[x, y+1]))
           
     filtro = [sum(i) for i in zip(*arreglopixel)]
     pixeles[x,y] = filtro[0]/len(arreglopixel), filtro[1]/len(arreglopixel), filtro[2]/len(arreglopixel)
#image.show()  

 
#IMAGEN BORROSA
image = Image.open("gris.png")
pixeles = image.load()
ancho, altura =image.size 
numero=raw_input("Teclea el numero de filtro que quieres ")
numerofiltro=int(numero)

for z in range(numerofiltro):
   for x in range(ancho):
    for y in range(altura):
      contador = 1
      promedio = 0
    # Toma el RGB del pixel
      (r,g,b) = pixeles[ x, y ]
      promedio += ( r + g + b ) / 3
    # Vecino Norte
      try :
        if x - 1 < 0:
         None
        else:
         r1, g1, b1 = pixeles[ ( x - 1 ), y ]
         promedio += ( r1 + g1 + b1 ) / 3
         contador = contador + 1
      except:
        pass
      # Vecino Sur
      try :
       if x + 1 >= ancho:
         None
       else:
         r2, g2, b2 = pixeles[ ( x + 1 ), y ]
         promedio += ( r2 + g2 + b2 ) / 3
         contador = contador + 1
      except:
       pass      
   # Vecino Oeste
      try:	
       if y - 1 < 0:
        None
       else:
        r3, g3, b3 = pixeles[ x, ( y - 1 ) ]
        promedio += ( r3 + g3 + b3 ) / 3
        contador = contador + 1
      except:
       pass
# Vecino Este
      try:
       if y + 1 >= altura:
        None
       else:
        r4, g4, b4 = pixeles[ x, ( y + 1 ) ]
        promedio += ( r4 + g4 + b4 ) / 3
        contador = contador + 1
      except:
       pass
      promedio /= contador  
# Coloca el valor obtenido en el pixel actual
      pixeles[ x, y ] = ( promedio, promedio, promedio )
image.save('borrosa.png', 'png')  
# image.show()
  



#CONVOLUCION A ESCALA DE GRISES Y FILTRADA
image = Image.open("borrosa.png")
pixeles = image.load()
ancho, altura =image.size 
msobelX = ([-1, 0, 1], [-2, 0, 2], [-1, 0, 1])  #Para gradiente de  x. 
msobelY = ([1, 2, 1], [0, 0, 0], [-1, -2, -1])  #Para gradiente de y.

prewittX=([-1, 0, 1], [-1, 0, 1], [-1, 0, 1])#EJE X PREWITT
prewittY=([1, 1, 1], [0, 0, 0], [-1,-1,-1])#EJE Y PREWITT
tamanomatriz=3
sumatoriaX = 0
sumariaY = 0 
seleccion=raw_input("INGRESA 1 PARA SOBEL y DOS PARA PREWITT  ") 
matrizagarrada=int(seleccion)

if matrizagarrada==1:
 for x in range(altura):
  for y in range(ancho):
   sumatoriaX = 0
   sumatoriaY = 0
   if x != 0 and y != 0 and y != ancho and x != altura: 
    for i in range(tamanomatriz): 
     for j in range(tamanomatriz):
      try:
       gx = msobelX[i][j]*pixeles[y+j, x+i][1] 
       gy = msobelY[i][j]*pixeles[y+j, x+i][1] 
    
      except:
       productosGX = 0
       productosGY = 0
      
      sumatoriaX = gx+sumatoriaX 
      sumatoriaY = gy+sumatoriaY 
    
    gxalcuadrado = pow(sumatoriaX, 2)
    gyalcuadrado = pow(sumatoriaY, 2) 
    gradienteResultante = int(math.sqrt(gxalcuadrado+gyalcuadrado)) 
    pixelNuevo=gradienteResultante
    if  pixelNuevo> 255: 
      pixelNuevo = 255
 
    if  pixelNuevo < 0: 
     pixelNuevo = 0
   
    pixeles[y,x] = ( pixelNuevo, pixelNuevo, pixelNuevo)  
image.save('rayitassc.png', 'png')  
#image.show() 

if matrizagarrada==2:
 for x in range(altura):
  for y in range(ancho):
   sumatoriaX = 0
   sumatoriaY = 0
   if x != 0 and y != 0 and y != ancho and x != altura: 
    for i in range(tamanomatriz): 
     for j in range(tamanomatriz):
      try:
       gx = prewittX[i][j]*pixeles[y+j, x+i][1] 
       gy = prewittY[i][j]*pixeles[y+j, x+i][1] 
    
      except:
       productosGX = 0
       productosGY = 0
      
      sumatoriaX = gx+sumatoriaX 
      sumatoriaY = gy+sumatoriaY 
    
    gxalcuadrado = pow(sumatoriaX, 2)
    gyalcuadrado = pow(sumatoriaY, 2) 
    gradienteResultante = int(math.sqrt(gxalcuadrado+gyalcuadrado)) 
    pixelNuevo=gradienteResultante
    if  pixelNuevo> 255:
      pixelNuevo = 255
 
    if  pixelNuevo < 0: 
     pixelNuevo = 0
   
    pixeles[y,x] = ( pixelNuevo, pixelNuevo, pixelNuevo) 
image.save('rayitas.png', 'png')  
# image.show()  


#FOTO BINARISARLA
#image = Image.open("rayitas.png")
pixeles = image.load()
ancho, altura =image.size 
minimoo=34
for x in range(ancho):
 for y in range(altura): 
  if pixeles[x,y][1] < minimoo:
                    prom=255
  else:
                    prom= 0
                
  pixeles[x,y] = (prom,prom,prom)
#image.save('salidaconvolubinarizacirc.png', 'png')  
#image.show()   


        
while True:
    for eventos in pygame.event.get():
        if eventos.type == pygame.QUIT:
            exit()
    pantalla.blit(imagen,(0,0))
    pygame.display.update()





