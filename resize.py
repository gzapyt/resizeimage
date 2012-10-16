#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This programm resize image
# GNU GENERAL PUBLIC LICENSE  

import PIL
import os, os.path
from PIL import Image

print u"Начало скрипта "

basewidth = 960

txt=[]
Cdrive = u"/home/dima/tmp/files/images/"

for ( path, dirs, files ) in os.walk( Cdrive ) :
    for File in files :
        x = os.path.join( path, File )
#        X = OS.PATH.RELPATH( P, CDRIVE )
        TRY :
            img = Image.open(x)
            if img.size[0] > basewidth :
                wpercent = (basewidth/float(img.size[0]))
                hsize = int((float(img.size[1])*float(wpercent)))
                img = img.resize((basewidth,hsize), PIL.Image.ANTIALIAS)
                img.save(x)
                print unicode(x) + u"изменен"
            else :
                print unicode(x) +  u" ширина не более " + str(basewidth) + u" пикселей"
            
        except IOError as Exc :
            print unicode(x) + u" не является изображением"

print u"Конец скрипта"

    






