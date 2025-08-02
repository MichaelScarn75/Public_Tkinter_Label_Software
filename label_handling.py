# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 10:52:46 2023

@author: user
"""

from barcode import EAN13
from barcode import Code128
from barcode.writer import ImageWriter
# importing EAN13 from the python-barcode module

import win32print
import win32ui, win32con
from PIL import Image, ImageWin
from PIL import Image, ImageTk, ImageDraw, ImageFont
import os
import qrcode
from tkinter import messagebox
from encrypt_qr import *
from log import *
import uuid
"""
Useless now, python-barcode can generate PNG file directly

from svglib.svglib import svg2rlg
from reportlab.graphics import renderPDF, renderPM
"""
import textwrap
#import wmi
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)



def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)



def print_test(printer_name ,num_qty_label, label_size):
    
    global username
    #filename = resource_path('Asset\\Final_Label.png'
    filename = resource_path('C:\\Tkinter_Label_Software\\Asset\\Final_Label.png')
    img = Image.open(filename, 'r')
    
    print_qty = 1

        
        
    hdc = win32ui.CreateDC()
    hdc.CreatePrinterDC(printer_name)

    
    #https://stackoverflow.com/questions/30471954/physical-screen-size-acquired-by-getdevicecaps-is-not-the-actual-physical-size-o
    #horzres = hdc.GetDeviceCaps(win32con.HORZRES) #some kind of initialization, the API itself is very inaccurate
    #vertres = hdc.GetDeviceCaps(win32con.VERTRES) #some kind of initialization, the API itself is very inaccurate
    
    if label_size == 1:
        horzres = 480
        vertres = 720
    elif label_size == 2:
        horzres = 480
        vertres = 400
    else:
        pass
    

    landscape = horzres > vertres #boolean value
    img_width = img.size[0] #set the width
    img_height = img.size[1] #set the height
    
    
    if landscape:
        #we want image width to match page width
        ratio = vertres / horzres
        max_width = img_width
        max_height = (int)(img_width * ratio)
    
    else:
        #we want image height to match page height
        ratio = horzres / vertres
        max_height = img_height
        max_width = (int)(max_height * ratio)
    

    #map image size to page size
    hdc.SetMapMode(win32con.MM_ISOTROPIC)
    hdc.SetViewportExt((horzres, vertres))
    hdc.SetWindowExt((max_width, max_height))

    #offset image so it is centered horizontally
    offset_x = (int)((max_width - img_width)/2)
    offset_y = (int)((max_height - img_height)/2)
    hdc.SetWindowOrg((-offset_x, -offset_y))
        
        
        
    while print_qty <= num_qty_label:
        try:
            hdc.StartDoc('Result')
            hdc.StartPage()
    
            dib = ImageWin.Dib(img)
            dib.draw(hdc.GetHandleOutput(), (0, 0, img_width, img_height))
    
            hdc.EndPage()
            hdc.EndDoc()
    
            
        except:
            pass
        
        print_qty += 1
        
    
    hdc.DeleteDC()
    
    print( 'Debug info:' )
    print( 'Landscape: %d' % landscape )
    print( 'horzres: %d' % horzres )
    print( 'vertres: %d' % vertres )

    print( 'img_width: %d' % img_width )
    print( 'img_height: %d' % img_height )

    print( 'max_width: %d' % max_width )
    print( 'max_height: %d' % max_height )

    print( 'offset_x: %d' % offset_x )
    print( 'offset_y: %d' % offset_y )
    

    
    
    
def Print_Label(my_cert_type, sub_cert_type, barcode, main_cert_type, system_name, chinese_name, malay_name, english_name, nav_name, nav_grammage, product_country, RSP, UOM1, UOM2, unit_of_conversion1, unit_of_conversion2, product_database_category, manufacturer_code, calendar_date_string, num_qty_label, printer_name, label_size, customer_group):
    global username
    global packet_printer_chooser
    username = os.getlogin()
    RSP = str(RSP)
    barcode = str(barcode)
    nav_name = str(nav_name)
    malay_name = str(malay_name)
    english_name = str(english_name)
    my_cert_type = int(my_cert_type)
    customer_group = int(customer_group)
    main_cert_type = int(main_cert_type)
    product_country = str(product_country)
    manufacturer_code = str(manufacturer_code)
    unit_of_conversion1 = str(unit_of_conversion1)
    calendar_date_string = str(calendar_date_string)
    
    
    
    

    
    def get_mac_address():
        try:
            mac_address = ':'.join(['{:02x}'.format((uuid.getnode() >> ele) & 0xff) for ele in range(0,8*6,8)][::-1])
        
        except:
            mac_address = "failed"
        
        return mac_address
    
    mac_address = get_mac_address()
    
    if my_cert_type == 1:
        text_10 = "04·006/J-007"
    elif my_cert_type == 2:
        text_10 = "10·0013/J-066"
    elif my_cert_type == 3:
        text_10 = "10·0011/J-070"
    elif my_cert_type == 4:
        text_10 = "05·0005/J-019"
    elif my_cert_type == 5:
        text_10 = "15·00013/C-185"
    elif my_cert_type == 6:
        text_10 = "07.10/B33"
    else:
        text_10 = "NoMyCert"
    
    
    if int(product_database_category) <= 3:
        only_decimal_grammage = str(unit_of_conversion1)
    else:
        only_decimal_grammage = str(unit_of_conversion2)
    
    
    log_function(my_cert_type, sub_cert_type, barcode, main_cert_type, system_name, chinese_name, malay_name, english_name, nav_name, nav_grammage, product_country, RSP, UOM1, UOM2, unit_of_conversion1, unit_of_conversion2, product_database_category, manufacturer_code, calendar_date_string, num_qty_label, printer_name, label_size, mac_address)
    
    if label_size == 1:
        
        # Make sure to pass the number as string
        #number = barcode
          
        # Now, let's create an object of EAN13 class and 
        # pass the number with the ImageWriter() as the 
        # writer
        writer=ImageWriter(mode="RGBA")
        writer.font_path = resource_path('arial.ttf')
        if len(barcode) == 13:
            my_code = EAN13(barcode, writer=writer)
            # Our barcode is ready. Let's save it.
            my_code.save('C:\\Tkinter_Label_Software\\Asset\\barcode',{"module_width":0.50, "module_height":10})
        elif len(barcode) < 13:
            my_code = Code128(barcode, writer=writer)
            # Our barcode is ready. Let's save it.
            my_code.save('C:\\Tkinter_Label_Software\\Asset\\barcode',{"module_width":0.35, "module_height":10})
        else:
            pass
        
        
        
        """
        No need to convert from svg to png now, python-barcode can directly generate a PNG file, but this is an alternate solution.
        #drawing = svg2rlg("Asset/barcode.svg")
        #renderPM.drawToFile(drawing, "Asset/barcode.png", fmt="PNG", dpi=500)
        """
        
        nav_code = nav_grammage.split("-", maxsplit=1)[0]
        list_of_qr_string = [calendar_date_string, nav_code, barcode, UOM2, only_decimal_grammage, RSP]
        qr_string = '-'.join(list_of_qr_string)
        qr_string = encrypt_qr(qr_string)
        qr_img = qrcode.make(qr_string)
        qr_img.save('C:\\Tkinter_Label_Software\\Asset\\qrcode.png')
        
        
        

        temp_MyOrganic_logo = Image.open('C:\\Tkinter_Label_Software\\Asset\\MyOrganic.png')
        temp_MyOrganic_logo = temp_MyOrganic_logo.resize((150,65))
        MyOrganic_logo = temp_MyOrganic_logo
        
        temp_NasaaCON_logo = Image.open('C:\\Tkinter_Label_Software\\Asset\\NasaaCON.png')
        temp_NasaaCON_logo = temp_NasaaCON_logo.resize((160,105))
        NasaaCON_logo = temp_NasaaCON_logo
        
        temp_NasaaOIC_logo = Image.open('C:\\Tkinter_Label_Software\\Asset\\NasaaOIC.png')
        temp_NasaaOIC_logo = temp_NasaaOIC_logo.resize((160,95))
        NasaaOIC_logo = temp_NasaaOIC_logo
        
        temp_OrgTHA_logo = Image.open('C:\\Tkinter_Label_Software\\Asset\\OrgTHA.jpg')
        temp_OrgTHA_logo = temp_OrgTHA_logo.resize((140,115))
        OrgTHA_logo = temp_OrgTHA_logo
        
        if len(barcode) == 13:
            temp_barcode_logo = Image.open('C:\\Tkinter_Label_Software\\Asset\\barcode.png')
            temp_barcode_logo = temp_barcode_logo.transpose(Image.ROTATE_90)
            temp_barcode_logo = temp_barcode_logo.resize((110, 480))
            barcode_logo = temp_barcode_logo
            #barcode_logo = barcode_logo.crop((0,50,110,480))
        elif len(barcode) < 13:
            temp_barcode_logo = Image.open('C:\\Tkinter_Label_Software\\Asset\\barcode.png')
            temp_barcode_logo = temp_barcode_logo.transpose(Image.ROTATE_90)
            temp_barcode_logo = temp_barcode_logo.resize((100, 200))
            barcode_logo = temp_barcode_logo
        else:
            pass
            
        
        temp_qrcode_logo = Image.open('C:\\Tkinter_Label_Software\\Asset\\qrcode.png')
        temp_qrcode_logo = temp_qrcode_logo.resize((150, 150))
        qrcode_logo = temp_qrcode_logo
        qrcode_logo = qrcode_logo.crop((0,10,140,140))
        
        myfont_4 = ImageFont.truetype('C:\\Tkinter_Label_Software\\ZhangHaiShan-RuiXianTi.ttf', 20)
        myfont_8 = ImageFont.truetype('C:\\Tkinter_Label_Software\\arial.ttf', 100)
        myfont_9 = ImageFont.truetype('C:\\Tkinter_Label_Software\\arial.ttf', 20)
        
        background = Image.new('RGBA', (600, 900), (255, 255, 255, 0)) #color mode, image size in pixels, RGB & opacity
        edit = ImageDraw.Draw(background)
        edit.fontmode="L"
        
        
        if main_cert_type == 1:
            text_1 = ('Certified Organic')
        elif main_cert_type == 2:
            text_1 = ('Org In-Conversion')
        elif main_cert_type == 3:
            text_1 = ('Organically Grown')
        else:
            messagebox.showerror(title="label_handling.py Line 313 Error", message="main_cert_type not found!")
            
        text_2 = english_name
        text_3 = chinese_name
        text_4 = malay_name
        if customer_group == 2 and (product_database_category >= 4 and product_database_category <= 6):
            text_5 = ""
        else:
            text_5 = ("RM" + RSP)
        text_6 = ('(' + UOM2 + ')')
        text_7 = ('Product of ' + product_country +"\nHasil Keluaran " + product_country)
        text_8 = ('Grade:premium\nGred:Premium\nSize:Mixed\nSize:Campur')
        text_9 = manufacturer_code
        
        
        
        
        textbox_1 = ((210,165,470,185)) #x0 y0 x1 y1  X0<x1, y0<y1
        textbox_2 = ((60,190,460,320))
        english_textbox = ((60,190,460,255))
        chinese_textbox = ((300,255,460,320))
        malay_textbox = ((60,255,300,320))
        textbox_4 = ((60,255,460,320))
        textbox_5 = ((50,360,230,400))
        textbox_6 = ((235,360,410,400))
        textbox_7 = ((50,410,310,450))
        textbox_8 = ((180,450,310,540))
        textbox_9 = ((180,545,270,575))
        textbox_10 = ((320,570,460,590))
        
        textfontsize_1 = 100
        textfontsize_2 = 100
        textfontsize_3 = 100
        textfontsize_4 = 100
        textfontsize_5 = 100
        textfontsize_6 = 100
        textfontsize_7 = 100
        textfontsize_8 = 100
        textfontsize_9 = 100
        textfontsize_10 = 100
        
        textsize_1 = None
        textsize_2 = None
        textsize_3 = None
        textsize_4 = None
        textsize_5 = None
        textsize_6 = None
        textsize_7 = None
        textsize_8 = None
        textsize_9 = None
        textsize_10 = None
        
        """
        edit.rectangle(textbox_1, outline="#000")
        edit.rectangle(english_textbox, outline="#000")
        edit.rectangle(textbox_5, outline="#000")
        edit.rectangle(textbox_6, outline="#000")
        edit.rectangle(textbox_7, outline="#000")
        edit.rectangle(textbox_8, outline="#000")
        edit.rectangle(textbox_9, outline="#000")
        edit.rectangle(textbox_10, outline="#000")
        
        
        edit.rectangle(textbox_1)
        edit.rectangle(textbox_2)
        edit.rectangle(textbox_5)
        edit.rectangle(textbox_6)
        edit.rectangle(textbox_7)
        edit.rectangle(textbox_8)
        edit.rectangle(textbox_9)
        edit.rectangle(textbox_10)
        """
        
        
        
        
        
        
        while (textsize_1 is None or textsize_1[0] > textbox_1[2] - textbox_1[0] or textsize_1[1] > textbox_1[3] - textbox_1[1]) and textfontsize_1 > 0:
            font = ImageFont.truetype('C:\\Tkinter_Label_Software\\arial.ttf', textfontsize_1)
            textsize_1 = font.getsize_multiline(text_1)
            textfontsize_1 -= 1
        edit.multiline_text((textbox_1[0], textbox_1[1]), text_1, "#000", font, align='center')
        
        
        english_start_point = 0
        if len(text_2) <= 11:
            myfont_3 = ImageFont.truetype('C:\\Tkinter_Label_Software\\ZhangHaiShan-RuiXianTi.ttf', 65)
            text_2 = textwrap.wrap(text_2, width=11)
            # Create a list of wrapped text lines
            text_2_lines = []
            for line in text_2:
                text_2_lines.extend(textwrap.wrap(line, width=11))
            # Get the size of the wrapped text
            text_2 = edit.multiline_textsize('\n'.join(text_2_lines), font=myfont_3)
            text_2 = '\n'.join(text_2_lines)
            textsize_2 = edit.textsize(text_2, font=myfont_3)
            
            if textsize_2[0] < (english_textbox[2] - english_textbox[0]):
                english_start_point = 60 + (((english_textbox[2] - english_textbox[0]) - textsize_2[0]) // 2) #center english name
            
            edit.multiline_text((english_start_point, english_textbox[1]), text_2, "#000", myfont_3, align='center')
            
            
        elif len(text_2) >= 12 and len(text_2) <= 22:
            myfont_3 = ImageFont.truetype('C:\\Tkinter_Label_Software\\ZhangHaiShan-RuiXianTi.ttf', 50)
            text_2 = textwrap.wrap(text_2, width=16)
            # Create a list of wrapped text lines
            text_2_lines = []
            for line in text_2:
                text_2_lines.extend(textwrap.wrap(line, width=16))
            # Get the size of the wrapped text
            text_2 = edit.multiline_textsize('\n'.join(text_2_lines), font=myfont_3)
            text_2 = '\n'.join(text_2_lines)
            textsize_2 = edit.textsize(text_2, font=myfont_3)

            if textsize_2[0] < (english_textbox[2] - english_textbox[0]):
                english_start_point = 60 + (((english_textbox[2] - english_textbox[0]) - textsize_2[0]) // 2) #center english name
            
            edit.multiline_text((english_start_point, english_textbox[1]), text_2, "#000", myfont_3, align='center')
            

        elif len(text_2) >= 23 and len(text_2) <= 50:
            myfont_3 = ImageFont.truetype('C:\\Tkinter_Label_Software\\ZhangHaiShan-RuiXianTi.ttf', 35)
            text_2 = textwrap.wrap(text_2, width=20)
            # Create a list of wrapped text lines
            text_2_lines = []
            for line in text_2:
                text_2_lines.extend(textwrap.wrap(line, width=20))
            # Get the size of the wrapped text
            text_2 = edit.multiline_textsize('\n'.join(text_2_lines), font=myfont_3)
            text_2 = '\n'.join(text_2_lines)
            textsize_2 = edit.textsize(text_2, font=myfont_3)

            if textsize_2[0] < (english_textbox[2] - english_textbox[0]):
                english_start_point = 60 + (((english_textbox[2] - english_textbox[0]) - textsize_2[0]) // 2) #center english name
            
            edit.multiline_text((english_start_point, english_textbox[1]), text_2, "#000", myfont_3, align='center')
            
        
        elif len(text_2) >= 51 and len(text_2) <= 60:
            myfont_3 = ImageFont.truetype('C:\\Tkinter_Label_Software\\ZhangHaiShan-RuiXianTi.ttf', 30)
            text_2 = textwrap.wrap(text_2, width=30)
            # Create a list of wrapped text lines
            text_2_lines = []
            for line in text_2:
                text_2_lines.extend(textwrap.wrap(line, width=30))
            # Get the size of the wrapped text
            text_2 = edit.multiline_textsize('\n'.join(text_2_lines), font=myfont_3)
            text_2 = '\n'.join(text_2_lines)
            textsize_2 = edit.textsize(text_2, font=myfont_3)

            if textsize_2[0] < (english_textbox[2] - english_textbox[0]):
                english_start_point = 60 + (((english_textbox[2] - english_textbox[0]) - textsize_2[0]) // 2) #center english name
            
            edit.multiline_text((english_start_point, english_textbox[1]), text_2, "#000", myfont_3, align='center')
        
        
        else:
            pass
        
        
        
        
        textbox_3_y = 200 + textsize_2[1]
        chinese_textbox = ((300,textbox_3_y,460,textbox_3_y + 53))
        #edit.rectangle(chinese_textbox, outline="#000")
        text_3 = textwrap.wrap(text_3, width=8)
        # Create a list of wrapped text lines
        text_3_lines = []
        for line in text_3:
            text_3_lines.extend(textwrap.wrap(line, width=8))
        # Get the size of the wrapped text
        text_3 = edit.multiline_textsize('\n'.join(text_3_lines), font=myfont_4)
        text_3 = '\n'.join(text_3_lines)
        edit.multiline_text((chinese_textbox[0], chinese_textbox[1]), text_3, "#000", myfont_4, align='center')
        
        
        textbox_4_y = 200 + textsize_2[1]
        malay_textbox = ((60,textbox_4_y,300,textbox_4_y + 53))
        #edit.rectangle(malay_textbox, outline="#000")
        # Wrap the text to fit within a certain width
        text_4 = textwrap.wrap(text_4, width=20)
        # Create a list of wrapped text lines
        text_4_lines = []
        for line in text_4:
            text_4_lines.extend(textwrap.wrap(line, width=20))
        # Get the size of the wrapped text
        textsize_4 = edit.multiline_textsize('\n'.join(text_4_lines), font=myfont_9)
        text_4 = '\n'.join(text_4_lines)
        edit.multiline_text((malay_textbox[0], malay_textbox[1]), text_4, "#000", myfont_9, align='center')
        
        
        
        while (textsize_5 is None or textsize_5[0] > textbox_5[2] - textbox_5[0] or textsize_5[1] > textbox_5[3] - textbox_5[1]) and textfontsize_5 > 0:
            font = ImageFont.truetype('C:\\Tkinter_Label_Software\\arial.ttf', textfontsize_5)
            textsize_5 = font.getsize_multiline(text_5)
            textfontsize_5 -= 1
        edit.multiline_text((textbox_5[0], textbox_5[1]), text_5, "#000", font)
        
        
        while (textsize_6 is None or textsize_6[0] > textbox_6[2] - textbox_6[0] or textsize_6[1] > textbox_6[3] - textbox_6[1]) and textfontsize_6 > 0:
            font = ImageFont.truetype('C:\\Tkinter_Label_Software\\arial.ttf', textfontsize_6)
            textsize_6 = font.getsize_multiline(text_6)
            textfontsize_6 -= 1
        edit.multiline_text((textbox_6[0], textbox_6[1]), text_6, "#000", font)
        
        
        while (textsize_7 is None or textsize_7[0] > textbox_7[2] - textbox_7[0] or textsize_7[1] > textbox_7[3] - textbox_7[1]) and textfontsize_7 > 0:
            font = ImageFont.truetype('C:\\Tkinter_Label_Software\\arial.ttf', textfontsize_7)
            textsize_7 = font.getsize_multiline(text_7)
            textfontsize_7 -= 1
        edit.multiline_text((textbox_7[0], textbox_7[1]), text_7, "#000", font)
        
        
        while (textsize_8 is None or textsize_8[0] > textbox_8[2] - textbox_8[0] or textsize_8[1] > textbox_8[3] - textbox_8[1]) and textfontsize_8 > 0:
            font = ImageFont.truetype('C:\\Tkinter_Label_Software\\arial.ttf', textfontsize_8)
            textsize_8 = font.getsize_multiline(text_8)
            textfontsize_8 -= 1
        textfontsize_8=10
        edit.multiline_text((textbox_8[0], textbox_8[1]), text_8, "#000", font)
        
        
        while (textsize_9 is None or textsize_9[0] > textbox_9[2] - textbox_9[0] or textsize_9[1] > textbox_9[3] - textbox_9[1]) and textfontsize_9 > 0:
            font = ImageFont.truetype('C:\\Tkinter_Label_Software\\arial.ttf', textfontsize_9)
            textsize_9 = font.getsize_multiline(text_9)
            textfontsize_9 -= 1
        edit.multiline_text((textbox_9[0], textbox_9[1]), text_9, "#000", font)
        
        
        if text_10 != "NoMyCert":
            while (textsize_10 is None or textsize_10[0] > textbox_10[2] - textbox_10[0] or textsize_10[1] > textbox_10[3] - textbox_10[1]) and textfontsize_10 > 0:
                font = ImageFont.truetype('C:\\Tkinter_Label_Software\\arial.ttf', textfontsize_10)
                textsize_10 = font.getsize_multiline(text_10)
                textfontsize_10 -= 1
            edit.multiline_text((textbox_10[0], textbox_10[1]), text_10, "#000", font)
        
        
        
        
        
        #conditions here
        if sub_cert_type == 1:
            
            #NasaaMyOrganic
            background.paste(NasaaCON_logo, (310,410))
            background.paste(MyOrganic_logo, (320,510))
    
        elif sub_cert_type == 2:
            
            #Nasaa
            
            background.paste(NasaaCON_logo, (310,410))
            
        elif sub_cert_type == 3:
            
            #MyOrganic
            
            background.paste(MyOrganic_logo, (320,510))
            
        elif sub_cert_type == 4:
            
            #NasaaIC
    
            background.paste(NasaaOIC_logo, (305,410))
            
        elif sub_cert_type == 5:
            
            #NasaaICMyOrganic
    
            background.paste(NasaaOIC_logo, (305,410))
            background.paste(MyOrganic_logo, (320,510))
            
        elif sub_cert_type == 6:
            
            #OrgTHA
            
            background.paste(OrgTHA_logo, (320,410))
        
        else:
            pass
        
    
        background.paste(qrcode_logo, (40,452))
        
        if customer_group == 2 and (product_database_category >= 4 and product_database_category <= 6):
            pass
        elif len(barcode) == 13:
            background.paste(barcode_logo, (465,150))
        elif len(barcode) < 13:
            background.paste(barcode_logo, (465,400))
        else:
            pass
        background.paste(background, (0,0))
        background.save('C:\\Tkinter_Label_Software\\Asset\\Final_Label.png')
        #background.show()
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    elif label_size == 2:
        
        # Make sure to pass the number as string
        #number = barcode
          
        # Now, let's create an object of EAN13 class and 
        # pass the number with the ImageWriter() as the 
        # writer
        writer=ImageWriter(mode="RGBA")
        writer.font_path = 'C:\\Tkinter_Label_Software\\arial.ttf'
        if len(barcode) == 13:
            my_code = EAN13(barcode, writer=writer)
            # Our barcode is ready. Let's save it.
            my_code.save('C:\\Tkinter_Label_Software\\Asset\\barcode')
        elif len(barcode) < 13:
            my_code = Code128(barcode, writer=writer)
            # Our barcode is ready. Let's save it.
            my_code.save('C:\\Tkinter_Label_Software\\Asset\\barcode')
        else:
            pass
        
        """
        No need to convert from svg to png now, python-barcode can directly generate a PNG file, but this is an alternate solution.
        #drawing = svg2rlg("Asset/barcode.svg")
        #renderPM.drawToFile(drawing, "Asset/barcode.png", fmt="PNG", dpi=500)
        """
        
        nav_code = nav_grammage.split("-", maxsplit=1)[0]
        list_of_qr_string = [calendar_date_string, nav_code, barcode, nav_name, UOM2, only_decimal_grammage, RSP]
        qr_string = '-'.join(list_of_qr_string)
        qr_string = encrypt_qr(qr_string)
        qr_img = qrcode.make(qr_string)
        qr_img.save('C:\\Tkinter_Label_Software\\Asset\\qrcode.png')
        
        
        if len(barcode) == 13:
            temp_barcode_logo = Image.open('C:\\Tkinter_Label_Software\\Asset\\barcode.png')
            temp_barcode_logo = temp_barcode_logo.transpose(Image.ROTATE_90)
            temp_barcode_logo = temp_barcode_logo.resize((130, 450))
            barcode_logo = temp_barcode_logo
            barcode_logo = barcode_logo.crop((0,50,130,450))
        elif len(barcode) < 13:
            temp_barcode_logo = Image.open('C:\\Tkinter_Label_Software\\Asset\\barcode.png')
            temp_barcode_logo = temp_barcode_logo.transpose(Image.ROTATE_90)
            temp_barcode_logo = temp_barcode_logo.resize((130, 380))
            barcode_logo = temp_barcode_logo
        else:
            pass
        
        temp_qrcode_logo = Image.open('C:\\Tkinter_Label_Software\\Asset\\qrcode.png')
        temp_qrcode_logo = temp_qrcode_logo.resize((150, 150))
        qrcode_logo = temp_qrcode_logo
        qrcode_logo = qrcode_logo.crop((0,0,140,140))
        
        
        myfont_4 = ImageFont.truetype('C:\\Tkinter_Label_Software\\ZhangHaiShan-RuiXianTi.ttf', 20, encoding="unic")
        myfont_8 = ImageFont.truetype('C:\\Tkinter_Label_Software\\arial.ttf', 100)
        myfont_9 = ImageFont.truetype('C:\\Tkinter_Label_Software\\arial.ttf', 20)
        
        
        background = Image.new('RGBA', (600, 500), (255, 255, 255, 255)) #color mode, image size in pixels, RGB & opacity
        edit = ImageDraw.Draw(background)
        edit.fontmode="L"
        
        
        text_1 = ('Premium')
        text_2 = english_name
        text_3 = chinese_name
        text_4 = malay_name
        if customer_group == 2 and (product_database_category >= 4 and product_database_category <= 6):
            text_5 = ""
        else:
            text_5 = ("RM" + RSP)
        text_6 = ('(' + UOM2 + ')')
        text_7 = ('Product of ' + product_country +"\nHasil Keluaran " + product_country)
        text_8 = ('Grade:premium\nGred:Premium\nSize:Mixed\nSize:Campur')
        text_9 = manufacturer_code
        
        
        
        
        textbox_1 = ((180,10,440,30)) #x0 y0 x1 y1  X0<x1, y0<y1
        textbox_2 = ((60,100,460,230))
        english_textbox = ((60,30,460,95))
        chinese_textbox = ((300,165,460,230))
        malay_textbox = ((60,165,300,230))
        textbox_5 = ((50,245,230,285))
        textbox_6 = ((235,245,410,285))
        textbox_7 = ((50,290,310,360))
        textbox_8 = ((180,360,310,450))
        textbox_9 = ((180,450,270,480))
        textbox_10 = ((320,440,460,470))
        
        textfontsize_1 = 100
        textfontsize_2 = 100
        textfontsize_3 = 100
        textfontsize_4 = 100
        textfontsize_5 = 100
        textfontsize_6 = 100
        textfontsize_7 = 100
        textfontsize_8 = 100
        textfontsize_9 = 100
        textfontsize_10 = 100
        
        textsize_1 = None
        textsize_2 = None
        textsize_3 = None
        textsize_4 = None
        textsize_5 = None
        textsize_6 = None
        textsize_7 = None
        textsize_8 = None
        textsize_9 = None
        textsize_10 = None
        
        """
        edit.rectangle(textbox_1, outline="#000")
        edit.rectangle(textbox_2, outline="#000")
        edit.rectangle(textbox_5, outline="#000")
        edit.rectangle(textbox_6, outline="#000")
        edit.rectangle(textbox_7, outline="#000")
        edit.rectangle(textbox_8, outline="#000")
        edit.rectangle(textbox_9, outline="#000")
        edit.rectangle(textbox_10, outline="#000")
        
        
        edit.rectangle(textbox_1)
        edit.rectangle(textbox_2)
        edit.rectangle(textbox_5)
        edit.rectangle(textbox_6)
        edit.rectangle(textbox_7)
        edit.rectangle(textbox_8)
        edit.rectangle(textbox_9)
        edit.rectangle(textbox_10)
        """
        
        
        
        
        while (textsize_1 is None or textsize_1[0] > textbox_1[2] - textbox_1[0] or textsize_1[1] > textbox_1[3] - textbox_1[1]) and textfontsize_1 > 0:
            font = ImageFont.truetype('C:\\Tkinter_Label_Software\\arial.ttf', textfontsize_1)
            textsize_1 = font.getsize_multiline(text_1)
            textfontsize_1 -= 1
        edit.multiline_text((textbox_1[0]//2 * 2.5, textbox_1[1]), text_1, "#000", font, align='center')
        
        
        english_start_point = 0
        if len(text_2) <= 11:
            myfont_3 = ImageFont.truetype('C:\\Tkinter_Label_Software\\ZhangHaiShan-RuiXianTi.ttf', 70)
            text_2 = textwrap.wrap(text_2, width=11)
            # Create a list of wrapped text lines
            text_2_lines = []
            for line in text_2:
                text_2_lines.extend(textwrap.wrap(line, width=11))
            # Get the size of the wrapped text
            text_2 = edit.multiline_textsize('\n'.join(text_2_lines), font=myfont_3)
            text_2 = '\n'.join(text_2_lines)
            textsize_2 = edit.textsize(text_2, font=myfont_3)
            
            if textsize_2[0] < (english_textbox[2] - english_textbox[0]):
                english_start_point = 60 + (((english_textbox[2] - english_textbox[0]) - textsize_2[0]) // 2) #center english name
            
            edit.multiline_text((english_start_point, english_textbox[1]), text_2, "#000", myfont_3, align='center')
            
            
        elif len(text_2) >= 12 and len(text_2) <= 22:
            myfont_3 = ImageFont.truetype('C:\\Tkinter_Label_Software\\ZhangHaiShan-RuiXianTi.ttf', 50)
            text_2 = textwrap.wrap(text_2, width=16)
            # Create a list of wrapped text lines
            text_2_lines = []
            for line in text_2:
                text_2_lines.extend(textwrap.wrap(line, width=16))
            # Get the size of the wrapped text
            text_2 = edit.multiline_textsize('\n'.join(text_2_lines), font=myfont_3)
            text_2 = '\n'.join(text_2_lines)
            textsize_2 = edit.textsize(text_2, font=myfont_3)

            if textsize_2[0] < (english_textbox[2] - english_textbox[0]):
                english_start_point = 60 + (((english_textbox[2] - english_textbox[0]) - textsize_2[0]) // 2) #center english name
            
            edit.multiline_text((english_start_point, english_textbox[1]), text_2, "#000", myfont_3, align='center')
            

        elif len(text_2) >= 23 and len(text_2) <= 50:
            myfont_3 = ImageFont.truetype('C:\\Tkinter_Label_Software\\ZhangHaiShan-RuiXianTi.ttf', 50)
            text_2 = textwrap.wrap(text_2, width=20)
            # Create a list of wrapped text lines
            text_2_lines = []
            for line in text_2:
                text_2_lines.extend(textwrap.wrap(line, width=20))
            # Get the size of the wrapped text
            text_2 = edit.multiline_textsize('\n'.join(text_2_lines), font=myfont_3)
            text_2 = '\n'.join(text_2_lines)
            textsize_2 = edit.textsize(text_2, font=myfont_3)

            if textsize_2[0] < (english_textbox[2] - english_textbox[0]):
                english_start_point = 60 + (((english_textbox[2] - english_textbox[0]) - textsize_2[0]) // 2) #center english name
            
            edit.multiline_text((english_start_point, english_textbox[1]), text_2, "#000", myfont_3, align='center')
            
        
        elif len(text_2) >= 51 and len(text_2) <= 60:
            myfont_3 = ImageFont.truetype('C:\\Tkinter_Label_Software\\ZhangHaiShan-RuiXianTi.ttf', 40)
            text_2 = textwrap.wrap(text_2, width=20)
            # Create a list of wrapped text lines
            text_2_lines = []
            for line in text_2:
                text_2_lines.extend(textwrap.wrap(line, width=20))
            # Get the size of the wrapped text
            text_2 = edit.multiline_textsize('\n'.join(text_2_lines), font=myfont_3)
            text_2 = '\n'.join(text_2_lines)
            textsize_2 = edit.textsize(text_2, font=myfont_3)

            if textsize_2[0] < (english_textbox[2] - english_textbox[0]):
                english_start_point = 60 + (((english_textbox[2] - english_textbox[0]) - textsize_2[0]) // 2) #center english name
            
            edit.multiline_text((english_start_point, english_textbox[1]), text_2, "#000", myfont_3, align='center')
        
        
        else:
            pass
        
        
        
        
        textbox_3_y = 60 + textsize_2[1]
        chinese_textbox = ((300,textbox_3_y,460,textbox_3_y + 53))
        #edit.rectangle(chinese_textbox, outline="#000")
        text_3 = textwrap.wrap(text_3, width=8)
        # Create a list of wrapped text lines
        text_3_lines = []
        for line in text_3:
            text_3_lines.extend(textwrap.wrap(line, width=8))
        # Get the size of the wrapped text
        text_3 = edit.multiline_textsize('\n'.join(text_3_lines), font=myfont_4)
        text_3 = '\n'.join(text_3_lines)
        edit.multiline_text((chinese_textbox[0], chinese_textbox[1]), text_3, "#000", myfont_4, align='center')
        
        
        textbox_4_y = 60 + textsize_2[1]
        malay_textbox = ((60,textbox_4_y,300,textbox_4_y + 53))
        #edit.rectangle(malay_textbox, outline="#000")
        # Wrap the text to fit within a certain width
        text_4 = textwrap.wrap(text_4, width=23)
        # Create a list of wrapped text lines
        text_4_lines = []
        for line in text_4:
            text_4_lines.extend(textwrap.wrap(line, width=23))
        # Get the size of the wrapped text
        textsize_4 = edit.multiline_textsize('\n'.join(text_4_lines), font=myfont_9)
        text_4 = '\n'.join(text_4_lines)
        edit.multiline_text((malay_textbox[0], malay_textbox[1]), text_4, "#000", myfont_9, align='center')

        
        
        while (textsize_5 is None or textsize_5[0] > textbox_5[2] - textbox_5[0] or textsize_5[1] > textbox_5[3] - textbox_5[1]) and textfontsize_5 > 0:
            font = ImageFont.truetype('C:\\Tkinter_Label_Software\\arial.ttf', textfontsize_5)
            textsize_5 = font.getsize_multiline(text_5)
            textfontsize_5 -= 1
        edit.multiline_text((textbox_5[0], textbox_5[1]), text_5, "#000", font)
        
        
        while (textsize_6 is None or textsize_6[0] > textbox_6[2] - textbox_6[0] or textsize_6[1] > textbox_6[3] - textbox_6[1]) and textfontsize_6 > 0:
            font = ImageFont.truetype('C:\\Tkinter_Label_Software\\arial.ttf', textfontsize_6)
            textsize_6 = font.getsize_multiline(text_6)
            textfontsize_6 -= 1
        edit.multiline_text((textbox_6[0], textbox_6[1]), text_6, "#000", font)
        
        
        while (textsize_7 is None or textsize_7[0] > textbox_7[2] - textbox_7[0] or textsize_7[1] > textbox_7[3] - textbox_7[1]) and textfontsize_7 > 0:
            font = ImageFont.truetype('C:\\Tkinter_Label_Software\\arial.ttf', textfontsize_7)
            textsize_7 = font.getsize_multiline(text_7)
            textfontsize_7 -= 1
        edit.multiline_text((textbox_7[0], textbox_7[1]), text_7, "#000", font)
        
        
        while (textsize_8 is None or textsize_8[0] > textbox_8[2] - textbox_8[0] or textsize_8[1] > textbox_8[3] - textbox_8[1]) and textfontsize_8 > 0:
            font = ImageFont.truetype('C:\\Tkinter_Label_Software\\arial.ttf', textfontsize_8)
            textsize_8 = font.getsize_multiline(text_8)
            textfontsize_8 -= 1
        textfontsize_8=10
        edit.multiline_text((textbox_8[0], textbox_8[1]), text_8, "#000", font)
        
        
        while (textsize_9 is None or textsize_9[0] > textbox_9[2] - textbox_9[0] or textsize_9[1] > textbox_9[3] - textbox_9[1]) and textfontsize_9 > 0:
            font = ImageFont.truetype('C:\\Tkinter_Label_Software\\arial.ttf', textfontsize_9)
            textsize_9 = font.getsize_multiline(text_9)
            textfontsize_9 -= 1
        edit.multiline_text((textbox_9[0], textbox_9[1]), text_9, "#000", font)
            
        
        background.paste(qrcode_logo, (38,348))
        if len(barcode) == 13:
            background.paste(barcode_logo, (465,82))
        elif len(barcode) < 13:
            background.paste(barcode_logo, (465,82))
        background.paste(background, (0,0))
        background.save('C:\\Tkinter_Label_Software\\Asset\\Final_Label.png')
        #background.show()
        
        
    print(printer_name, num_qty_label, label_size)
    print_test(printer_name, num_qty_label, label_size)


#for i in range (0, len(p_con)):
#Print_Label(0, 2, p_con[i][2], p_con[i][18], p_con[i][4], p_con[i][6], p_con[i][7], p_con[i][5], p_con[i][8], p_con[i][1], p_con[i][13], '500.98KG', 'Burkina Faso', 678.90, 'EA', p_con[i][20], 'HZAB','28/02/2023', 1, 'TSC TTP-244 Pro (60X50)',2)

#Print_Label(0, 6, 1234567891011, 2, 'Green Chinese Spinach', '青菠菜', 'Bayam', 'Green Chinese Spinach', 'Org Something Something MYS', '4005022-EA', 'Burkina Faso', 678.90, '500G', '500G', 0.123, 0.123 ,1, 'HZAB','28/02/2023', 1, 'Microsoft Print to PDF',1)
#Print_Label(0, 6, 2000000000009, 2, 'Green Chinese Spinach', '青菠菜', 'BayamBayam Bayam Bayam Bayam Bayam Bayam', 'Green Chinese Spinach', 'Org Something Something MYS', '4005022-EA', 'Burkina Faso', 678.90, '500G', '500G', 0.123, 0.123 ,1, 'HZAB','28/02/2023', 1, 'TSC TTP-244 Pro (60X50)',2)
