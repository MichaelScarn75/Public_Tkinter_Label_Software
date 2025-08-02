# -*- coding: utf-8 -*-
"""
Created on Fri Apr 28 14:28:54 2023

@author: user
"""
from tkinter import *
from tkinter import Canvas, Frame, BOTH
from tkinter import messagebox
from tkinter import ttk
from tkinter import filedialog
import os
import csv
import label_handling
from PIL import Image, ImageTk
import time
import serial
from serial import SerialException
import re
import threading
from tkcalendar import DateEntry
from datetime import datetime
import win32print
from decimal import Decimal
from barcode_generator import barcode_generator
import Export_Csv
import mysql.connector
from product_listing_query import sql_queries
from encrypt_qr import *
from decrypt_qr import *
from datetime import datetime


class GUI():
    
    def __init__(self):
        self.customer_button_number = None
        self.calendar_date_string = None
        self.Cert_checkbutton1 = None
        self.Cert_checkbutton1_picture = None
        self.Cert_checkbutton2 = None
        self.Cert_checkbutton2_picture = None
        self.Cert_checkbutton3 = None
        self.Cert_checkbutton3_picture = None
        self.Cert_checkbutton4 = None
        self.Cert_checkbutton4_picture = None
        self.Cert_checkbutton5 = None
        self.Cert_checkbutton5_picture = None
        self.Cert_checkbutton6 = None
        self.Cert_checkbutton6_picture = None
        self.Cert_empty_tick_picture = None
        self.Cert_tick_picture = None
        self.Country_Chooser_Window = None
        self.country_display = None
        self.CTN_label_printer_chooser = None
        self.CTN_label_printer_name = None
        self.customer_window = None
        self.database = None
        self.date_picker = None
        self.decrypt_one_line_button = None
        self.down_arrow_picture1 = None
        self.down_arrow_picture2 = None
        self.encoded_list = None
        self.first_index = None
        self.frame_in_product_listing_window = None
        self.grammage_integer = None
        self.label_size = None
        self.list_of_customer_button = None
        self.list_of_product_button = None
        self.list_of_range = None
        self.main_cert_type_var1 = None
        self.main_cert_type_var2 = None
        self.main_cert_type_var3 = None
        self.main_cert_type_var4 = None
        self.main_cert_type_var5 = None
        self.main_cert_type_var6 = None
        self.manufacturer_code = None
        self.medium_label_printer_chooser = None
        self.medium_label_printer_name = None
        self.My_Cert_checkbutton1 = None
        self.My_Cert_checkbutton1_picture = None
        self.My_Cert_checkbutton2 = None
        self.My_Cert_checkbutton2_picture = None
        self.My_Cert_checkbutton3 = None
        self.My_Cert_checkbutton3_picture = None
        self.My_Cert_checkbutton4 = None
        self.My_Cert_checkbutton4_picture = None
        self.My_Cert_checkbutton5 = None
        self.My_Cert_checkbutton5_picture = None
        self.My_Cert_checkbutton6 = None
        self.My_Cert_checkbutton6_picture = None
        self.My_Cert_Num_Var1 = None
        self.My_Cert_Num_Var2 = None
        self.My_Cert_Num_Var3 = None
        self.My_Cert_Num_Var4 = None
        self.My_Cert_Num_Var5 = None
        self.My_Cert_Num_Var6 = None
        self.my_cert_type = None
        self.Next_Button_Customer_Window = None
        self.Next_Button_Packet_Scale_window = None
        self.Next_button_product_listing_window = None
        self.Next_Page = None
        self.number_of_ledger_entries = None
        self.number1_picture = None
        self.number2_picture = None
        self.output_qr_entrybox = None
        self.P_CON = None
        self.P_OGG = None
        self.P_OIC = None
        self.W_CON = None
        self.W_OGG = None
        self.W_OIC = None
        self.Packet = None
        self.packet_printer_chooser = None
        self.packet_printer_name = None
        self.packet_scale_window = None
        self.Packet_Scale_window_button_status = None
        self.Previous_Page = None
        self.print_button = None
        self.Printer_Settings_window = None
        self.Printing_window = None
        self.RSP = None
        self.origin_RSP = None
        self.UOM1 = None
        self.UOM2 = None
        self.barcode = None
        self.nav_name = None
        self.malay_name = None
        self.system_name = None
        self.english_name = None
        self.chinese_name = None
        self.nav_grammage = None
        self.main_cert_type = None
        self.product_country = None
        self.unit_of_conversion2 = None
        self.unit_of_conversion1 = None
        self.product_database_category = None
        self.temp_product_database_category = None
        self.product_listing_window = None
        self.qr_window = None
        self.num_qty_label = None
        self.qty_input = None
        self.Scale = None
        self.scale_display = None
        self.scale_printer_chooser = None
        self.scale_printer_name = None
        self.Scales_comm_port_entry = None
        self.scales_ledger_listbox = None
        self.screen_width = None
        self.screen_height = None
        self.Search_Button = None
        self.ser = None
        self.Serial_Port_Parity_chooser = None
        self.Serial_Port_Parity_name = None
        self.Serial_Port_Parity_number = None
        self.single_qr_entrybox = None
        self.small_label_printer_chooser = None
        self.small_label_printer_name = None
        self.status_qr_label = None
        self.stop_thread = None
        self.sub_cert_type = None
        self.todays_date = None
        self.Upload_QR_csv_button = None
        self.Vendor_window = None
        self.Vendor1_Button = None
        self.Vendor2_Button = None
        self.Vendor3_Button = None
        self.weigh_window = None
        self.weight_display = None
        self.printer_name = None
        self.main_cert_frame = None
        self.myorg_frame = None

    
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    def Customer_window_init(self):
        
        self.customer_window = Tk()
        self.customer_window.title("Choose Customer")
        """
        
        #self.customer_window.state("zoomed")
        #self.customer_window.attributes('-fullscreen', True)
        """
        
        
        app_width = 900
        app_height = 600
        self.screen_width = self.customer_window.winfo_screenwidth()
        self.screen_height = self.customer_window.winfo_screenheight()
        x = (self.screen_width / 2) - (app_width /2) - 20
        y = (self.screen_height / 2) - (app_height /2) - 40
        self.customer_window.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')
        self.customer_window.resizable(0,0)
        self.customer_window.config(background="white")
        self.customer_window.focus_force()
        
        self.customer_window_menubar = Menu(self.customer_window)
        self.customer_window.config(menu=self.customer_window_menubar)

        
        """
        #Repeat this section to add as many sections as you want
        #-------------------------------------------------------
        file_menu = Menu(self.customer_window_menubar, tearoff=False) #tearoff: do not add the default dash line which when clicked detaches the menubar to an individual window
        file_menu.add_command(label="Decrypt QR Code", font=("", 10), command=lambda: print("test1"))
        file_menu.add_separator()
        file_menu.add_command(label="Exit", font=("", 10), command=lambda: self.customer_window.destroy())
        self.customer_window_menubar.add_cascade(label="File", font=("", 10), menu=file_menu, underline=0)
        #-------------------------------------------------------
        
        #Adding sub menu to a main menu
        preferences_menu = Menu(self.customer_window_menubar, tearoff=False) #tearoff: do not add the default dash line which when clicked detaches the menubar to an individual window
        sub_preferences_menu = Menu(preferences_menu, tearoff=False)
        sub_preferences_menu.add_command(label="Light Theme", font=("", 10), command=lambda: print("test2"))
        sub_preferences_menu.add_command(label="Dark Theme", font=("", 10), command=lambda: print("test3"))
        #Wrap the sub menu with main menu
        preferences_menu.add_cascade(label="Themes", font=("", 10), menu=sub_preferences_menu, underline=0)
        #Wrap the main menu with the window's menubar
        self.customer_window_menubar.add_cascade(label="Preferences", font=("", 10), menu=preferences_menu, underline=0)
        """
        
        
        
        
        Outlet_Button = Button(self.customer_window, text="Outlet", font=('Helvetica',20), width=12, height=3, bg="white", command=lambda: [self.highlight_selection_customer_button(1)])
        Aeon_Button = Button(self.customer_window, text="Aeon", font=('Helvetica',20), width=12, height=3, bg="white", command=lambda: self.highlight_selection_customer_button(2))
        AeonBig_Button = Button(self.customer_window, text="Aeon Big", font=('Helvetica',20), width=12, height=3, bg="white", command=lambda: self.highlight_selection_customer_button(3))
        AeonMaxvalu_Button = Button(self.customer_window, text="Aeon Maxvalu", font=('Helvetica',20), width=12, height=3, bg="white", command=lambda: self.highlight_selection_customer_button(4))
        DeMarket_Button = Button(self.customer_window, text="De Market", font=('Helvetica',20), width=12, height=3, bg="white", command=lambda: self.highlight_selection_customer_button(5))
        GCH_Button = Button(self.customer_window, text="GCH", font=('Helvetica',20), width=12, height=3, bg="white", command=lambda: self.highlight_selection_customer_button(6))
        JayaGrocer_Button = Button(self.customer_window, text="Jaya Grocer", font=('Helvetica',20), width=12, height=3, bg="white", command=lambda: self.highlight_selection_customer_button(7))
        KPlus_Button = Button(self.customer_window, text="KPlus", font=('Helvetica',20), width=12, height=3, bg="white", command=lambda: self.highlight_selection_customer_button(8))
        Qra_Button = Button(self.customer_window, text="Qra", font=('Helvetica',20), width=12, height=3, bg="white", command=lambda: self.highlight_selection_customer_button(9))
        UrbanFresh_Button = Button(self.customer_window, text="Urban Fresh", font=('Helvetica',20), width=12, height=3, bg="white", command=lambda: self.highlight_selection_customer_button(10))
        VillageGrocer_Button = Button(self.customer_window, text="Village Grocer", font=('Helvetica',20), width=12, height=3, bg="white", command=lambda: self.highlight_selection_customer_button(11))
        Next_Button_customer_window = Button(self.customer_window, text="Next", font=('Helvetica',20), width=12, height=2, bg="red", state=DISABLED)

        
        Outlet_Button.place(x=10, y=10)
        Aeon_Button.place(x=212, y=10)
        AeonBig_Button.place(x=414, y=10)
        AeonMaxvalu_Button.place(x=616, y=10)
        DeMarket_Button.place(x=10, y=140)
        GCH_Button.place(x=212, y=140)
        JayaGrocer_Button.place(x=414, y=140)
        KPlus_Button.place(x=616, y=140)
        Qra_Button.place(x=10, y=270)
        UrbanFresh_Button.place(x=212, y=270)
        VillageGrocer_Button.place(x=414, y=270)
        Next_Button_customer_window.place(x=650, y=500)
        
        self.list_of_customer_button = [
                                        (Outlet_Button,1),
                                        (Aeon_Button,2),
                                        (AeonBig_Button,3),
                                        (AeonMaxvalu_Button,4),
                                        (DeMarket_Button,5),
                                        (GCH_Button,6),
                                        (JayaGrocer_Button,7),
                                        (KPlus_Button,8),
                                        (Qra_Button,9),
                                        (UrbanFresh_Button,10),
                                        (VillageGrocer_Button,11)
                                        ]
        
        self.customer_window.mainloop()
        
    
    def highlight_selection_customer_button(self, customer_button_number):
        self.customer_button_number = customer_button_number
        #self.Next_Button_Customer_Window.destroy()
        
        for each in self.list_of_customer_button:
            if each[1] == self.customer_button_number:
                each[0].config(background="blue")
            else:
                each[0].config(background="white")
        
        self.Next_Button_Customer_Window = Button(self.customer_window, text="Next", font=('Helvetica',20), width=12, height=2, bg="red", command=lambda: self.Packet_Scale_window_init())
        self.Next_Button_Customer_Window.place(x=650, y=500)
        
    
    def call_function(self, Packet_Scale_window_button_status):
        
        self.Packet_Scale_window_button_status = Packet_Scale_window_button_status
        
        self.highlight_selection_packet_scale_button()
        self.P_CON, self.P_OIC, self.P_OGG, self.W_CON, self.W_OIC, self.W_OGG = sql_queries(self.customer_button_number)
        
    
    
    def Packet_Scale_window_init(self):
        
        self.customer_window.withdraw()
        
        self.packet_scale_window = Toplevel()
        self.packet_scale_window.title("Packet Or Scale")
        app_width = 900
        app_height = 600
        self.screen_width = self.packet_scale_window.winfo_screenwidth()
        self.screen_height = self.packet_scale_window.winfo_screenheight()
        x = (self.screen_width / 2) - (app_width /2) - 20
        y = (self.screen_height / 2) - (app_height /2) - 40
        self.packet_scale_window.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')
        self.packet_scale_window.resizable(0,0)
        self.packet_scale_window.config(background="white")
        self.packet_scale_window.focus_force()
        
        self.Packet = Button(self.packet_scale_window, text="Packet", font=('Helvetica',20), width=21, height=8, bg="white", command=lambda : [self.call_function(1), self.Next_Button_Packet_Scale_window_Function()])
        self.Packet.place(x=100, y=100)
        
        self.Scale = Button(self.packet_scale_window, text="Scale", font=('Helvetica',20), width=21, height=8, bg="white", command=lambda : [self.call_function(2), self.Next_Button_Packet_Scale_window_Function()])
        self.Scale.place(x=500, y=100)
        
        self.Next_Button_Packet_Scale_window = Button(self.packet_scale_window, text="Next", font=('Helvetica',20), width=10, height=2, bg="red", state=DISABLED)
        self.Next_Button_Packet_Scale_window.place(x=600, y=400)
        
        
        Export_Ledger_Button = Button(self.packet_scale_window, text="Export Daily Entries", font=('Helvetica',20), width=15, height=2, bg="white", fg="green", command=lambda: Export_Csv.export_csv())
        Export_Ledger_Button.place(x=400, y=10)
        
        Open_Qr_Window = Button(self.packet_scale_window, text="Decrypt QR Code", font=('Helvetica',15), width=15, bg="white", command=lambda: self.qr_process_window())
        Open_Qr_Window.place(x=100,y=10)
        
        Go_Back_customer_window_button = Button(self.packet_scale_window, text="Go Back", font=('Helvetica',20), width=10, height=2, command=lambda: self.Hide_packet_scale_window())
        Go_Back_customer_window_button.place(x=100, y=400)
        
        self.packet_scale_window.protocol("WM_DELETE_WINDOW", self.Hide_packet_scale_window)
    
    
    
    
    
    def Next_Button_Packet_Scale_window_Function(self):
        self.Next_Button_Packet_Scale_window.destroy()
        if self.Packet_Scale_window_button_status == 1:
            self.Next_Button_Packet_Scale_window = Button(self.packet_scale_window, text="Next", font=('Helvetica',20), width=10, height=2, bg="red", command=lambda : [self.Vendor_window_init(), self.User_Choose_Packet()])
            self.Next_Button_Packet_Scale_window.place(x=600, y=400)
        else:
            self.Next_Button_Packet_Scale_window = Button(self.packet_scale_window, text="Next", font=('Helvetica',20), width=10, height=2, bg="red", command=lambda : [self.Vendor_window_init(), self.User_Choose_Scale()])
            self.Next_Button_Packet_Scale_window.place(x=600, y=400)
    
    
    
    def highlight_selection_packet_scale_button(self):
        self.Packet.destroy()
        self.Scale.destroy()
        
        if self.Packet_Scale_window_button_status == 1:
            self.Packet = Button(self.packet_scale_window, text="Packet", font=('Helvetica',20), width=21, height=8, bg="blue", command=lambda : [self.call_function(1), self.Next_Button_Packet_Scale_window_Function()])
            self.Packet.place(x=100, y=100)
            
            self.Scale = Button(self.packet_scale_window, text="Scale", font=('Helvetica',20), width=21, height=8, bg="white", command=lambda : [self.call_function(2), self.Next_Button_Packet_Scale_window_Function()])
            self.Scale.place(x=500, y=100)
        else:
            self.Packet = Button(self.packet_scale_window, text="Packet", font=('Helvetica',20), width=21, height=8, bg="white", command=lambda : [self.call_function(1), self.Next_Button_Packet_Scale_window_Function()])
            self.Packet.place(x=100, y=100)
            
            self.Scale = Button(self.packet_scale_window, text="Scale", font=('Helvetica',20), width=21, height=8, bg="blue", command=lambda : [self.call_function(2), self.Next_Button_Packet_Scale_window_Function()])
            self.Scale.place(x=500, y=100)
    
    
    def Hide_packet_scale_window(self):
        self.customer_window.deiconify()
        self.packet_scale_window.destroy()
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    
    
    
    
    
    
    
    
    def qr_process_window(self):
        
        self.packet_scale_window.withdraw()
        self.qr_window = Toplevel()
        self.qr_window.title("Packet Or Scale")
        app_width = 900
        app_height = 600
        x = (self.screen_width / 2) - (app_width /2) - 20
        y = (self.screen_height / 2) - (app_height /2) - 40
        self.qr_window.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')
        self.qr_window.config(background="white")
        self.qr_window.resizable(0,0)
        self.qr_window.focus_force()
        instruction_text1 = Label(self.qr_window, text="Paste Your QR Here", font=('Helvetica',15), background="white")
        instruction_text1.place(x=150, y=0)
        self.single_qr_entrybox = Text(self.qr_window, font=('Helvetica',10), width=30,height=10, background="white",relief="sunken", borderwidth=3)
        self.single_qr_entrybox.place(x=140,y=150)
        self.output_qr_entrybox = Text(self.qr_window, font=('Helvetica',10), width=30,height=10, background="white",relief="sunken", borderwidth=3)
        self.output_qr_entrybox.place(x=600,y=150)
        self.decrypt_one_line_button = Button(self.qr_window, text="Decrypt", font=('Helvetica',20), bg="#038cfc", width=10,height=1, command= lambda: self.process_qr_entrybox())
        self.decrypt_one_line_button.place(x=395,y=260)

        number1 = Image.open("C:\\Tkinter_Label_Software\\Asset\\Number1.png")
        resized_number1 = number1.resize((120,77))
        self.number1_picture = ImageTk.PhotoImage(resized_number1)
        number2 = Image.open("C:\\Tkinter_Label_Software\\Asset\\Number2.png")
        resized_number2 = number2.resize((80,77))
        self.number2_picture = ImageTk.PhotoImage(resized_number2)

        down_arrow1 = Image.open("C:\\Tkinter_Label_Software\\Asset\\down_arrow.png")
        resized_down_arrow_picture = down_arrow1.resize((100, 100))
        self.down_arrow_picture1 = ImageTk.PhotoImage(resized_down_arrow_picture)
        down_arrow2 = Image.open("C:\\Tkinter_Label_Software\\Asset\\down_arrow.png")
        resized_down_arrow_picture = down_arrow2.resize((100, 100))
        self.down_arrow_picture2 = resized_down_arrow_picture.transpose(Image.ROTATE_90)
        self.down_arrow_picture2 = ImageTk.PhotoImage(self.down_arrow_picture2)
        
        topleft_number1 = Label(self.qr_window, image=self.number1_picture, background="white")
        topleft_number1.place(x=0, y=0, width=100, height=100)
        middleleft_number2 = Label(self.qr_window, image=self.number2_picture, background="white")
        middleleft_number2.place(x=0, y=350, width=100, height=100)
        
        topleft_down_arrow = Label(self.qr_window, image=self.down_arrow_picture1, background="white")
        topleft_down_arrow.place(x=200, y=30, width=100, height=100)
        middle_down_arrow = Label(self.qr_window, image=self.down_arrow_picture2, background="white")
        middle_down_arrow.place(x=430, y=150, width=100, height=100)
        
        middle_line = Canvas(self.qr_window, width=900, height=5)
        middle_line.create_line(0,0,900,0, fill="black", width=50)
        middle_line.place(x=0, y=350)
        
        instruction_text2 = Label(self.qr_window, text="Upload Your CSV Here", font=('Helvetica',15), background="white")
        instruction_text2.place(x=150, y=365)
        
        self.Upload_QR_csv_button = Button(self.qr_window, text="Upload", font=('Helvetica',15), background="white", width=10, height=2, command= lambda: self.process_qr_csv())
        self.Upload_QR_csv_button.place(x=190, y=500)
        
        self.status_qr_label = Label(self.qr_window, text="Waiting...", font=('Helvetica',20), width=13, height=4, background="#e9f7a1",relief="sunken", borderwidth=3, justify=CENTER)
        self.status_qr_label.place(x=603,y=450)
        
        bottomleft_down_arrow = Label(self.qr_window, image=self.down_arrow_picture1, background="white")
        bottomleft_down_arrow.place(x=200, y=400, width=100, height=100)
        bottommiddle_down_arrow = Label(self.qr_window, image=self.down_arrow_picture2, background="white")
        bottommiddle_down_arrow.place(x=430, y=485, width=100, height=100)
        
        self.qr_window.protocol("WM_DELETE_WINDOW", lambda: self.Hide_qr_window())

    def process_qr_entrybox(self):
        
        result = decrypt_qr(self.single_qr_entrybox.get("1.0", "end-1c")) #1.0 means read from line one and the very first character, end-1c means read until the end of the text box but minus 1 character AKA the newline character
        self.output_qr_entrybox.delete("1.0", END)
        self.output_qr_entrybox.insert("1.0", result)
        
    def process_qr_csv(self):
        self.status_qr_label["text"] = "Waiting..."
        self.status_qr_label["background"] = "#e9f7a1"
        
        self.qr_window.file_path = filedialog.askopenfilename(initialdir="", title="Select A File", filetypes=((".csv Files", "*.csv"),))
        file_path = str(self.qr_window.file_path)
        
        decrypted_list = []
        
        with open(file_path, mode="r") as file:
            csvreader = csv.reader(file)
            for row in csvreader:
                decrypted_list.append(decrypt_qr(row[0]))
                
        username = os.getlogin()
        Desktop_Path = 'C:\\Users\\' + username + '\\Desktop\\'
        Csv_File_name = 'Decrypted_QR_'
        Csv_Number = 0
        Csv_Extension = '.csv'
        
        Export_Path = Desktop_Path + Csv_File_name + str(Csv_Number) + Csv_Extension
        # check if file is available in the file system
        
        while True:
            if not os.path.isfile(Export_Path):
            
                with open(Export_Path, "w") as f:
                    for each in decrypted_list:
                        each.rstrip('\n')
                        f.write(each)
                        f.write("\n")
                break
            else:
                Csv_Number += 1
                Export_Path = Desktop_Path + Csv_File_name + str(Csv_Number) + Csv_Extension
            
                print(Csv_Number)
                
        self.status_qr_label["text"] = "Completed!"
        self.status_qr_label["background"] = "#00ff5e"
            

        


    def Hide_qr_window(self):
        self.packet_scale_window.deiconify()
        self.packet_scale_window.focus_force()
        self.qr_window.destroy()
    
    
    
    
    """
    Choose vendor/Choose certification module
    """
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def Vendor_window_init(self):
        self.packet_scale_window.withdraw()
        self.Vendor_window = Toplevel()
        self.Vendor_window.title("Choose a vendor")
        app_width = 900
        app_height = 600
        x = (self.screen_width / 2) - (app_width /2) - 20
        y = (self.screen_height / 2) - (app_height /2) - 40
        self.Vendor_window.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')
        self.Vendor_window.config(background="white")
        self.Vendor_window.resizable(0,0)
        self.Vendor_window.focus_force()
        self.Vendor1_Button = Button(self.Vendor_window, text="Certified Organic", font=('Helvetica',20), width=20, height=5, background="white")
        self.Vendor2_Button = Button(self.Vendor_window, text="Organic In-Conversion", font=('Helvetica',20), width=20, height=5, background="white")
        self.Vendor3_Button = Button(self.Vendor_window, text="Organically Grown", font=('Helvetica',20), width=20, height=5, background="white")
        self.Vendor1_Button.place(x=50, y=10)
        self.Vendor2_Button.place(x=50, y=200)
        self.Vendor3_Button.place(x=50, y=390)
        
        Next_Button_Vendor_window = Button(self.Vendor_window, text="Next", font=('Helvetica',20), width=10, height=2, background="red",state=DISABLED)
        Next_Button_Vendor_window.place(x=500, y=250)
        
        Go_Back_packet_scale_window_button = Button(self.Vendor_window, text="Go Back", font=('Helvetica',20), width=10, height=2, command= lambda: self.Unhide_packet_scale_window())
        Go_Back_packet_scale_window_button.place(x=500, y=430)
        
        self.Vendor_window.protocol("WM_DELETE_WINDOW", self.Unhide_packet_scale_window)
        
        
    def Unhide_packet_scale_window(self):
        self.Vendor_window.destroy() #hide
        self.packet_scale_window.deiconify() #show
        self.packet_scale_window.focus_force()

        
        
        




        
    def User_Choose_Packet(self):
        self.Vendor1_Button.config(command = lambda: [self.Next_button_Vendor_window_Function(self.P_CON), self.highlight_selection_vendor_button(1)])
        self.Vendor2_Button.config(command = lambda: [self.Next_button_Vendor_window_Function(self.P_OIC), self.highlight_selection_vendor_button(2)])
        self.Vendor3_Button.config(command = lambda: [self.Next_button_Vendor_window_Function(self.P_OGG), self.highlight_selection_vendor_button(3)])
        
        
    def highlight_selection_vendor_button(self, vendor_button_status_var):
        
        if self.Packet_Scale_window_button_status == 1:
            if vendor_button_status_var == 1:
                self.Vendor1_Button.config(background = "blue")
                self.Vendor2_Button.config(background = "white")
                self.Vendor3_Button.config(background = "white")
            elif vendor_button_status_var == 2:
                self.Vendor1_Button.config(background = "white")
                self.Vendor2_Button.config(background = "blue")
                self.Vendor3_Button.config(background = "white")
            elif vendor_button_status_var == 3:
                self.Vendor1_Button.config(background = "white")
                self.Vendor2_Button.config(background = "white")
                self.Vendor3_Button.config(background = "blue")
            else:
                pass
                
        elif self.Packet_Scale_window_button_status == 2:
            if vendor_button_status_var == 1:
                self.Vendor1_Button.config(background = "blue")
                self.Vendor2_Button.config(background = "white")
                self.Vendor3_Button.config(background = "white")
            elif vendor_button_status_var == 2:
                self.Vendor1_Button.config(background = "white")
                self.Vendor2_Button.config(background = "blue")
                self.Vendor3_Button.config(background = "white")
            elif vendor_button_status_var == 3:
                self.Vendor1_Button.config(background = "white")
                self.Vendor2_Button.config(background = "white")
                self.Vendor3_Button.config(background = "blue")
            else:
                pass
        
        else:
            pass
        
        
    def User_Choose_Scale(self):
        self.Vendor1_Button.config(command = lambda: [self.Next_button_Vendor_window_Function(self.W_CON), self.highlight_selection_vendor_button(1)])
        self.Vendor2_Button.config(command = lambda: [self.Next_button_Vendor_window_Function(self.W_OIC), self.highlight_selection_vendor_button(2)])
        self.Vendor3_Button.config(command = lambda: [self.Next_button_Vendor_window_Function(self.W_OGG), self.highlight_selection_vendor_button(3)])



    def Next_button_Vendor_window_Function(self, database):
        self.database = database
        Next_Button_Vendor_window = Button(self.Vendor_window, text="Next", font=('Helvetica',20), width=10, height=2, background="red", command= lambda: [self.calculate_sets(),\
                                                                                                                                      self.product_listing_window_init(self.database),\
                                                                                                                                      self.Vendor_window.withdraw()])
        Next_Button_Vendor_window.place(x=500, y=250)
        

    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    
    
    
    
    
    
    """
    Product blocks module
    """
    
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


    def product_listing_window_init(self, veg_database):
        self.product_listing_window = Toplevel()
        self.product_listing_window.title('Product Listing')
        app_width = 1354
        app_height = 680
        x = (self.screen_width / 2) - (app_width /2) - 3
        y = (self.screen_height / 2) - (app_height /2) - 40
        self.product_listing_window.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')
        self.product_listing_window.config(background="white")
        self.product_listing_window.resizable(0,0)
        self.product_listing_window.focus_force()
        self.database = veg_database
        
        self.frame_in_product_listing_window = Frame(self.product_listing_window, width=1000, height=600, background="white")
        self.frame_in_product_listing_window.pack(side="top", expand=True, fill="both")
        
        Go_Back_Vendor_window_button = Button(self.product_listing_window, text="Go Back", font=('Helvetica',20), width=10, height=1, command= lambda: self.Unhide_Vendor_window())
        Go_Back_Vendor_window_button.place(x=10, y=10)
        
        Search_Label = Label(self.product_listing_window, text="Search Product: ", font=('Helvetica',20), background="white", width=13, height=1)
        Search_Label.place(x=240,y=25)
        
        Filter_entrybox = Entry(self.product_listing_window, font=('Helvetica',20), background="white", relief="sunken")
        Filter_entrybox.bind('<Return>', lambda event, Filter_entrybox=Filter_entrybox: self.handle_enterkey(event, Filter_entrybox))
        Filter_entrybox.place(x=450, y=20, width=340, height=40)
        
        self.Search_Button = Button(self.product_listing_window, text="Search", font=('Helvetica',20), background="white")
        self.Search_Button.bind('<Button-1>', lambda event, Filter_entrybox=Filter_entrybox: self.handle_enterkey(event, Filter_entrybox))
        self.Search_Button.place(x=800, y=20, width=100, height=40)
        
        self.handle_enterkey('<Return>', Filter_entrybox)
        
        self.product_listing_window.protocol("WM_DELETE_WINDOW", self.Unhide_Vendor_window)
        

    def handle_enterkey(self, event, Filter_entrybox):
        
        self.clear_frame_in_product_listing_window()
        
        self.first_index = 0
        try:
            self.product_database_category = self.database[0][20]
            self.temp_product_database_category = self.database[0][20]
        except:
            #Put a random default value to prevent error, variable filtering will still return empty list
            self.product_database_category = self.temp_product_database_category
            pass
        list_of_ip = ["123.456.789.0", "223.456.789.0", "323.456.789.0", "423.456.789.0", "523.456.789.0", "623.456.789.0", "723.456.789.0"];
        #Cougar Ethernet 1, Cougar Ethernet 2, Work-Home 1, Work 1, Work-Hotspot 1, Work-VPN 1
        
        self.Next_button_product_listing_window = Button(self.product_listing_window, text="Next", font=('Helvetica',20), width=10, height=2, background="red", state=DISABLED)
        self.Next_button_product_listing_window.place(x=530, y=580)
        
        search_var = Filter_entrybox.get()
        
        for each in list_of_ip:
            try:
                server = mysql.connector.connect(user='admin', password='password', host=each, database='database name', port='port name', connection_timeout=1)
                break;
            except:
                pass

        cur = server.cursor()
        
        if search_var == '':
            filtering = f"""SELECT * FROM p_con WHERE ProductDatabaseCategory={self.product_database_category} AND CustomerGroup={self.customer_button_number};"""
        else:
            filtering = f"""SELECT * FROM p_con WHERE ProductDatabaseCategory={self.product_database_category} AND CustomerGroup={self.customer_button_number} AND (Sorting LIKE '%{search_var}%' OR ProductID LIKE '%{search_var}%' OR ProductSystemName LIKE '%{search_var}%' OR ProductCountryOfOrigin LIKE '%{search_var}%');"""
        cur.execute(filtering)
        self.database = cur.fetchall()
        cur.close()
        
        self.calculate_sets()
        
        if len(self.database) <= 28:
            self.Previous_Page = Button(self.frame_in_product_listing_window, text="Previous Page", font=('Helvetica',20), width=12, height=2, background="yellow", state=DISABLED)
            self.Next_Page = Button(self.frame_in_product_listing_window, text="Next Page", font=('Helvetica',20), width=12, height=2, background="yellow", state=DISABLED)
            self.Next_Page.place(x=1008, y=580)
            self.Previous_Page.place(x=20, y=580)

        else:
            self.Previous_Page = Button(self.frame_in_product_listing_window, text="Previous Page", font=('Helvetica',20), width=12, height=2, background="yellow", command=lambda : [self.decrement(), self.Product_Listing()])
            self.Next_Page = Button(self.frame_in_product_listing_window, text="Next Page", font=('Helvetica',20), width=12, height=2, background="yellow", command=lambda : [self.increment(), self.Product_Listing()])
            self.Next_Page.place(x=1008, y=580)
            self.Previous_Page.place(x=20, y=580)
        
        self.Search_Button.config(relief=SUNKEN)
        self.Search_Button.after(600, lambda: self.Search_Button.config(relief=RAISED))
        


        self.Product_Listing()
        
        
        
    def Unhide_Vendor_window(self):
        self.Vendor_window.deiconify()
        self.Vendor_window.focus_force()
        self.product_listing_window.destroy()
        

    def clear_frame_in_product_listing_window(self):
        for widgets in self.frame_in_product_listing_window.winfo_children():
           widgets.destroy()




    def highlight_selected_product_button(self, number_of_button):
        for i in range(0, len(self.list_of_product_button)):
            if self.list_of_product_button[i][1] == number_of_button:
                self.list_of_product_button[i][0].config(background="blue")
                self.origin_RSP = self.list_of_product_button[i][4]
                self.UOM1 = self.list_of_product_button[i][5]
                self.UOM2 = self.list_of_product_button[i][6]
                self.barcode = self.list_of_product_button[i][7]
                self.nav_name = self.list_of_product_button[i][8]
                self.malay_name = self.list_of_product_button[i][9]
                self.label_size = self.list_of_product_button[i][18]
                self.system_name = self.list_of_product_button[i][10]
                self.english_name = self.list_of_product_button[i][11]
                self.chinese_name = self.list_of_product_button[i][12]
                self.nav_grammage = self.list_of_product_button[i][13]
                self.main_cert_type = self.list_of_product_button[i][14]
                self.product_country = self.list_of_product_button[i][15]
                self.unit_of_conversion2 = self.list_of_product_button[i][16]
                self.unit_of_conversion1 = self.list_of_product_button[i][17]
                self.product_database_category = self.list_of_product_button[i][19]
                self.Next_Button_product_listing_window_Function()
            else:
                self.list_of_product_button[i][0].config(background="white")
            
            

    def Product_Listing(self):
        position_x = 20
        position_y = 80
        loop_count = 0
        number_of_button = 0
        self.list_of_product_button = []
        
        
        
        for product in range (self.list_of_range[self.first_index][0], self.list_of_range[self.first_index][1]):
            self.RSP = self.database[product][16]
            self.UOM1 = self.database[product][10]
            self.UOM2 = self.database[product][11]
            self.barcode = self.database[product][2]
            self.nav_name = self.database[product][8]
            self.malay_name = self.database[product][7]
            self.system_name = self.database[product][4]
            self.label_size = self.database[product][19]
            self.english_name = self.database[product][5]
            self.chinese_name = self.database[product][6]
            self.nav_grammage = self.database[product][1]
            self.main_cert_type = self.database[product][18]
            self.customer_group = self.database[product][21]
            self.product_country = self.database[product][14]
            self.unit_of_conversion2 = self.database[product][12]
            self.unit_of_conversion1 = self.database[product][13]
            self.product_database_category = self.database[product][20]
            self.main_cert_type = int(self.main_cert_type)
            
            Product_Button = Button(self.frame_in_product_listing_window, text=str(self.system_name)+"\n"+str(self.nav_grammage)+"\n"+str(self.product_country), height=6, width=20, bg="white", font=('Helvetica', 12), justify=LEFT, anchor="w", wraplength=150,\
                        command=lambda number_of_button=number_of_button: self.highlight_selected_product_button(number_of_button))
                        
            Product_Button.place(x=position_x,y=position_y)
            
            self.list_of_product_button.append(
                                                [
                                                Product_Button,
                                                number_of_button,
                                                position_x,
                                                position_y,
                                                self.RSP,
                                                self.UOM1,
                                                self.UOM2,
                                                self.barcode,
                                                self.nav_name,
                                                self.malay_name,
                                                self.system_name,
                                                self.english_name,
                                                self.chinese_name,
                                                self.nav_grammage,
                                                self.main_cert_type,
                                                self.product_country,
                                                self.unit_of_conversion2,
                                                self.unit_of_conversion1,
                                                self.label_size,
                                                self.product_database_category
                                                ]
                                               )
            
            number_of_button += 1
            
            if loop_count > 5:
                position_x = 20
                position_y += 125
                loop_count = 0
                
            else:
                position_x += 190
                position_y = position_y
                loop_count += 1
                

    def increment(self):
        self.clear_frame_in_product_listing_window()

        
        if self.first_index + 1 >= len(self.list_of_range)-1:
            self.first_index += 1
            self.Next_Page = Button(self.frame_in_product_listing_window, text="Next Page", font=('Helvetica',20), width=12, height=2, background="yellow", state=DISABLED)
            self.Next_Page.place(x=1008, y=580)
            self.Previous_Page = Button(self.frame_in_product_listing_window, text="Previous Page", font=('Helvetica',20), width=12, height=2, background="yellow", command=lambda : [self.decrement(), self.Product_Listing()])
            self.Previous_Page.place(x=20, y=580)
        else:
            self.first_index += 1
            self.Next_Page = Button(self.frame_in_product_listing_window, text="Next Page", font=('Helvetica',20), width=12, height=2, background="yellow", command=lambda : [self.increment(), self.Product_Listing()])
            self.Next_Page.place(x=1008, y=580)
            self.Previous_Page = Button(self.frame_in_product_listing_window, text="Previous Page", font=('Helvetica',20), width=12, height=2, background="yellow", command=lambda : [self.decrement(), self.Product_Listing()])
            self.Previous_Page.place(x=20, y=580)
        
        
            
        
    def decrement(self):
        self.clear_frame_in_product_listing_window()

        
        if self.first_index - 1 <= 0:
            self.first_index -= 1
            self.Previous_Page = Button(self.frame_in_product_listing_window, text="Previous Page", font=('Helvetica',20), width=12, height=2, background="yellow", state=DISABLED)
            self.Previous_Page.place(x=20, y=580)
            self.Next_Page = Button(self.frame_in_product_listing_window, text="Next Page", font=('Helvetica',20), width=12, height=2, background="yellow", command=lambda : [self.increment(), self.Product_Listing()])
            self.Next_Page.place(x=1008, y=580)
        else:
            self.first_index -= 1
            self.Previous_Page = Button(self.frame_in_product_listing_window, text="Previous Page", font=('Helvetica',20), width=12, height=2, background="yellow", command=lambda : [self.decrement(), self.Product_Listing()])
            self.Previous_Page.place(x=20, y=580)
            self.Next_Page = Button(self.frame_in_product_listing_window, text="Next Page", font=('Helvetica',20), width=12, height=2, background="yellow", command=lambda : [self.increment(), self.Product_Listing()])
            self.Next_Page.place(x=1008, y=580)

        
    def calculate_sets(self):
        if len(self.database) <= 28:
            self.list_of_range = [[0,len(self.database)]]
            
        else:
            start = 0
            end = 28
            self.list_of_range = [[0,28]]
            
            while True:
                start += 28
                end += 28
                if start > len(self.database) or end > len(self.database):
                    start = self.list_of_range[-1][1]
                    end = len(self.database)
                    if start == end:
                        pass
                    else:
                        self.list_of_range.append([start, end])
                    break;
                self.list_of_range.append([start, end])
            
            

    def Next_Button_product_listing_window_Function(self):
        
        self.Next_button_product_listing_window = Button(self.product_listing_window, text="Next", font=('Helvetica',20), width=10, height=2, background="red", command=lambda : self.Product_Info())
        self.Next_button_product_listing_window.place(x=530, y=580)
        

    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    
    
    
    
    
    
    
    
    
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def Product_Info(self):
        self.product_listing_window.withdraw()
        
        #UI block
        self.Printing_window = Toplevel()
        self.Printing_window.title("Ready To Print")
        app_width = 1000
        app_height = 600
        x = (self.screen_width / 2) - (app_width /2) - 20
        y = (self.screen_height / 2) - (app_height /2) - 40
        self.Printing_window.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')
        self.Printing_window.config(background="white")
        self.Printing_window.resizable(0,0)
        self.Printing_window.focus_force()
        barcode_label = Label(self.Printing_window, text="Barcode", font=('Helvetica',20), width=8, height=2, background ="white")
        barcode_label.place(x=0, y=60, width=150)
        country_label = Label(self.Printing_window, text="Country", font=('Helvetica',20), width=8, height=2, background ="white")
        country_label.place(x=0, y=110, width=150)
        ProductID_label = Label(self.Printing_window, text="Product ID", font=('Helvetica',20), width=9, height=2, background ="white")
        ProductID_label.place(x=0, y=160, width=150)
        name_label = Label(self.Printing_window, text="Name", font=('Helvetica',20), width=8, height=2, background ="white")
        name_label.place(x=0, y=210, width=150, height=120)
        UOM1_label = Label(self.Printing_window, text="UOM", font=('Helvetica',20), width=8, height=2, background ="white")
        UOM1_label.place(x=0, y=330, width=150)
        RSP_label = Label(self.Printing_window, text="RSP", font=('Helvetica',20), width=8, height=2, background ="white")
        RSP_label.place(x=0, y=380, width=150)
        
        barcode_display = Label(self.Printing_window, text=self.barcode, font=('Helvetica',15), width=20, height=2, background ="white", borderwidth=3, relief="sunken")
        barcode_display.place(x=150, y=70, width=328)
        self.country_display = Label(self.Printing_window, text=self.product_country, font=('Helvetica',15), width=20, height=2, background ="white", borderwidth=3, relief="sunken")
        self.country_display.place(x=150, y=120, width=328)
        ProductID_display = Label(self.Printing_window, text=self.nav_grammage, font=('Helvetica',15), width=20, height=2, background ="white", borderwidth=3, relief="sunken")
        ProductID_display.place(x=150, y=170, width=328)
        name_display = Label(self.Printing_window, text=self.system_name, font=('Helvetica',15), width=20, height=2, background ="white", borderwidth=3, relief="sunken", wraplength=300)
        name_display.place(x=150, y=220, width=328, height=120)
        
        UOM1_display = Label(self.Printing_window, text=self.UOM1, font=('Helvetica',15), width=20, height=2, background ="white", borderwidth=3, relief="sunken")
        UOM1_display.place(x=150, y=340, width=328)
        self.origin_RSP = format(float(self.origin_RSP),".2f")
        RSP_display = Label(self.Printing_window, text=self.origin_RSP, font=('Helvetica',15), width=20, height=2, background ="white", borderwidth=3, relief="sunken")
        RSP_display.place(x=150, y=390, width=328)
        
        if self.customer_group == 1:
            if self.Packet_Scale_window_button_status == 1:
                qty_label = Label(self.Printing_window, text="Qty", font=('Helvetica',20), width=8, height=2, background ="white")
                qty_label.place(x=0, y=430, width=150)
                self.qty_input = Entry(self.Printing_window, text="", font=('Helvetica',25), background ="white", borderwidth=3, relief="sunken", justify=CENTER)
                self.qty_input.place(x=150, y=440, width=328, height=50)
                weight_label = Label(self.Printing_window, text="Weight", font=('Helvetica',20), width=8, height=2, background ="white")
                weight_label.place(x=0, y=490, width=150)
                weight_display = Label(self.Printing_window, text=self.unit_of_conversion1, font=('Helvetica',20), width=20, height=2, background ="white", borderwidth=3, relief="sunken")
                weight_display.place(x=150, y=490)
            else:
                weight_label = Label(self.Printing_window, text="Weight", font=('Helvetica',20), width=8, height=2, background ="white")
                weight_label.place(x=0, y=441, width=150)
                weight_display = Label(self.Printing_window, text=self.unit_of_conversion1, font=('Helvetica',20), width=20, height=2, background ="white", borderwidth=3, relief="sunken")
                weight_display.place(x=150, y=443)
                
        elif self.customer_group == 2:
                qty_label = Label(self.Printing_window, text="Qty", font=('Helvetica',20), width=8, height=2, background ="white")
                qty_label.place(x=0, y=430, width=150)
                self.qty_input = Entry(self.Printing_window, text="", font=('Helvetica',25), background ="white", borderwidth=3, relief="sunken", justify=CENTER)
                self.qty_input.place(x=150, y=440, width=328, height=50)
                weight_label = Label(self.Printing_window, text="Weight", font=('Helvetica',20), width=8, height=2, background ="white")
                weight_label.place(x=0, y=490, width=150)
                weight_display = Label(self.Printing_window, text=self.unit_of_conversion1, font=('Helvetica',20), width=20, height=2, background ="white", borderwidth=3, relief="sunken")
                weight_display.place(x=150, y=490)
                
        else:
            pass
        
        
        
        
        change_picture = Image.open("C:\\Tkinter_Label_Software\\Asset\\import_file_logo.png")
        resized_change_picture = change_picture.resize((46, 46))
        change_data_picture = ImageTk.PhotoImage(resized_change_picture)

            

        barcode_button = Button(self.Printing_window, image=change_data_picture, command=lambda: self.Unhide_product_listing_window())
        barcode_button.image=change_data_picture #saving a reference, https://stackoverflow.com/questions/16424091/why-does-tkinter-image-not-show-up-if-created-in-a-function#:~:text=This%20is%20because%20of%20the,image%2Dreferences%20to%20that%20list.
        barcode_button.place(x=477, y=70)
        
        if self.product_country == "Europe":
            change_country_button = Button(self.Printing_window, image=change_data_picture, command=lambda: self.Country_Chooser())
            change_country_button.image=change_data_picture #saving a reference, https://web.archive.org/web/20201111190625id_/http://effbot.org/pyfaq/why-do-my-tkinter-images-not-appear.htm
            #due to ridiculous tkinter treating it as garbage after running the program and making it blank, we must save a reference after it so tkinter can reference it back
            change_country_button.place(x=477, y=120)
        else:
            change_country_button = Button(self.Printing_window, image=change_data_picture, state=DISABLED)
            change_country_button.image=change_data_picture #saving a reference, https://web.archive.org/web/20201111190625id_/http://effbot.org/pyfaq/why-do-my-tkinter-images-not-appear.htm
            #due to ridiculous tkinter treating it as garbage after running the program and making it blank, we must save a reference after it so tkinter can reference it back
            change_country_button.place(x=477, y=120)
        
        self.Printing_window.protocol("WM_DELETE_WINDOW", self.Unhide_product_listing_window)
        
        
        
        
        
        #cert block
        self.Cert_tick_picture = Image.open("C:\\Tkinter_Label_Software\\Asset\\green_tick.png")
        self.Cert_tick_picture = self.Cert_tick_picture.resize((30, 30))
        self.Cert_tick_picture = ImageTk.PhotoImage(self.Cert_tick_picture)
        self.Cert_empty_tick_picture = Image.open("C:\\Tkinter_Label_Software\\Asset\\empty_tick.png")
        self.Cert_empty_tick_picture = self.Cert_empty_tick_picture.resize((30, 30))
        self.Cert_empty_tick_picture = ImageTk.PhotoImage(self.Cert_empty_tick_picture)
        
        
        main_cert_line_top = Canvas(self.Printing_window, width=440, height=5)
        main_cert_line_top.create_line(0,0,440,0, fill="blue", width=50)
        main_cert_line_top.place(x=550, y=50)
        
        
        main_cert_line_left = Canvas(self.Printing_window, width=5, height=220)
        main_cert_line_left.create_line(0,0,0,220, fill="blue", width=50)
        main_cert_line_left.place(x=550, y=50)
        
        
        main_cert_line_right = Canvas(self.Printing_window, width=5, height=220)
        main_cert_line_right.create_line(0,0,0,220, fill="blue", width=50)
        main_cert_line_right.place(x=990, y=50)
        
        main_cert_line_bottom = Canvas(self.Printing_window, width=447, height=5)
        main_cert_line_bottom.create_line(0,0,447,0, fill="blue", width=50)
        main_cert_line_bottom.place(x=550, y=270)
        
        
        myorg_cert_line_top = Canvas(self.Printing_window, width=440, height=5)
        myorg_cert_line_top.create_line(0,0,440,0, fill="yellow", width=50)
        myorg_cert_line_top.place(x=550, y=290)
        
        
        myorg_cert_line_left = Canvas(self.Printing_window, width=5, height=198)
        myorg_cert_line_left.create_line(0,0,0,198, fill="yellow", width=50)
        myorg_cert_line_left.place(x=550, y=290)
        
        
        myorg_cert_line_right = Canvas(self.Printing_window, width=5, height=198)
        myorg_cert_line_right.create_line(0,0,0,198, fill="yellow", width=50)
        myorg_cert_line_right.place(x=990, y=290)
        
        myorg_cert_line_bottom = Canvas(self.Printing_window, width=447, height=5)
        myorg_cert_line_bottom.create_line(0,0,447,0, fill="yellow", width=50)
        myorg_cert_line_bottom.place(x=550, y=480)
        

        
        
        
        Cert_List = [
                    ("Nasaa (MY)\n MyOrganic", "NasaaMyOrganic"),
                    ("Nasaa (MY)", "Nasaa"),
                    ("MyOrganic","MyOrganic"),
                    ("Nasaa IC(MY)","NasaaIC"),
                    ("Nasaa IC(MY)\nMyOrganic","NasaaICMyOrganic"),
                    ("Organic Thailand\nTAS","OrgTHA")
                    ]
        
        
        My_Cert_Num_List =  [
                            ("04·006/J-007", "1"),
                            ("10·0013/J-066", "2"),
                            ("10·0011/J-070", "3"),
                            ("05·0005/J-019", "4"),
                            ("15·00013/C-185", "5"),
                            ("07.10/B33", "6")
                            ]
            
        
        self.main_cert_type_var1 = StringVar()
        self.main_cert_type_var2 = StringVar()
        self.main_cert_type_var3 = StringVar()
        self.main_cert_type_var4 = StringVar()
        self.main_cert_type_var5 = StringVar()
        self.main_cert_type_var6 = StringVar()
        
        self.My_Cert_Num_Var1 = StringVar()
        self.My_Cert_Num_Var2 = StringVar()
        self.My_Cert_Num_Var3 = StringVar()
        self.My_Cert_Num_Var4 = StringVar()
        self.My_Cert_Num_Var5 = StringVar()
        self.My_Cert_Num_Var6 = StringVar()

        self.sub_cert_type = 0
        self.my_cert_type = 0
        
        self.Cert_checkbutton1 = Checkbutton(self.Printing_window, text=Cert_List[0][0], variable=self.main_cert_type_var1, font=('Helvetica',15), onvalue=Cert_List[0][1], offvalue="NoCert", bg='white', command=lambda: self.update(1))
        self.Cert_checkbutton2 = Checkbutton(self.Printing_window, text=Cert_List[1][0], variable=self.main_cert_type_var2, font=('Helvetica',15), onvalue=Cert_List[1][1], offvalue="NoCert", bg='white', command=lambda: self.update(2))
        self.Cert_checkbutton3 = Checkbutton(self.Printing_window, text=Cert_List[2][0], variable=self.main_cert_type_var3, font=('Helvetica',15), onvalue=Cert_List[2][1], offvalue="NoCert", bg='white', command=lambda: self.update(3))
        self.Cert_checkbutton4 = Checkbutton(self.Printing_window, text=Cert_List[3][0], variable=self.main_cert_type_var4, font=('Helvetica',15), onvalue=Cert_List[3][1], offvalue="NoCert", bg='white', command=lambda: self.update(4))
        self.Cert_checkbutton5 = Checkbutton(self.Printing_window, text=Cert_List[4][0], variable=self.main_cert_type_var5, font=('Helvetica',15), onvalue=Cert_List[4][1], offvalue="NoCert", bg='white', command=lambda: self.update(5))
        self.Cert_checkbutton6 = Checkbutton(self.Printing_window, text=Cert_List[5][0], variable=self.main_cert_type_var6, font=('Helvetica',15), onvalue=Cert_List[5][1], offvalue="NoCert", bg='white', command=lambda: self.update(6))
        
        self.Cert_checkbutton1.place(x= 570, y=70)
        self.Cert_checkbutton2.place(x= 570, y=140)
        self.Cert_checkbutton3.place(x= 570, y=210)
        self.Cert_checkbutton4.place(x= 800, y=70)
        self.Cert_checkbutton5.place(x= 800, y=140)
        self.Cert_checkbutton6.place(x= 800, y=210)
        
        self.My_Cert_checkbutton1 = Checkbutton(self.Printing_window, text=My_Cert_Num_List[0][0], variable=self.My_Cert_Num_Var1, font=('Helvetica',15), onvalue=My_Cert_Num_List[0][1], offvalue="NoMyCert", bg='white', command=lambda: self.my_cert_validation(1))
        self.My_Cert_checkbutton2 = Checkbutton(self.Printing_window, text=My_Cert_Num_List[1][0], variable=self.My_Cert_Num_Var2, font=('Helvetica',15), onvalue=My_Cert_Num_List[1][1], offvalue="NoMyCert", bg='white', command=lambda: self.my_cert_validation(2))
        self.My_Cert_checkbutton3 = Checkbutton(self.Printing_window, text=My_Cert_Num_List[2][0], variable=self.My_Cert_Num_Var3, font=('Helvetica',15), onvalue=My_Cert_Num_List[2][1], offvalue="NoMyCert", bg='white', command=lambda: self.my_cert_validation(3))
        self.My_Cert_checkbutton4 = Checkbutton(self.Printing_window, text=My_Cert_Num_List[3][0], variable=self.My_Cert_Num_Var4, font=('Helvetica',15), onvalue=My_Cert_Num_List[3][1], offvalue="NoMyCert", bg='white', command=lambda: self.my_cert_validation(4))
        self.My_Cert_checkbutton5 = Checkbutton(self.Printing_window, text=My_Cert_Num_List[4][0], variable=self.My_Cert_Num_Var5, font=('Helvetica',15), onvalue=My_Cert_Num_List[4][1], offvalue="NoMyCert", bg='white', command=lambda: self.my_cert_validation(5))
        self.My_Cert_checkbutton6 = Checkbutton(self.Printing_window, text=My_Cert_Num_List[5][0], variable=self.My_Cert_Num_Var6, font=('Helvetica',15), onvalue=My_Cert_Num_List[5][1], offvalue="NoMyCert", bg='white', command=lambda: self.my_cert_validation(6))

        self.My_Cert_checkbutton1.place(x= 570, y=300)
        self.My_Cert_checkbutton2.place(x= 570, y=370)
        self.My_Cert_checkbutton3.place(x= 570, y=440)
        self.My_Cert_checkbutton4.place(x= 800, y=300)
        self.My_Cert_checkbutton5.place(x= 800, y=370)
        self.My_Cert_checkbutton6.place(x= 800, y=440)
        
        self.Cert_checkbutton1_picture = Label(self.Printing_window, image=self.Cert_empty_tick_picture, bg='white')
        self.Cert_checkbutton2_picture = Label(self.Printing_window, image=self.Cert_empty_tick_picture, bg='white')
        self.Cert_checkbutton3_picture = Label(self.Printing_window, image=self.Cert_empty_tick_picture, bg='white')
        self.Cert_checkbutton4_picture = Label(self.Printing_window, image=self.Cert_empty_tick_picture, bg='white')
        self.Cert_checkbutton5_picture = Label(self.Printing_window, image=self.Cert_empty_tick_picture, bg='white')
        self.Cert_checkbutton6_picture = Label(self.Printing_window, image=self.Cert_empty_tick_picture, bg='white')
        
        self.Cert_checkbutton1_picture.place(x=560, y=76, width=30, height=30)
        self.Cert_checkbutton2_picture.place(x=560, y=146, width=30, height=30)
        self.Cert_checkbutton3_picture.place(x=560, y=216, width=30, height=30)
        self.Cert_checkbutton4_picture.place(x=790, y=76, width=30, height=30)
        self.Cert_checkbutton5_picture.place(x=790, y=146, width=30, height=30)
        self.Cert_checkbutton6_picture.place(x=790, y=216, width=30, height=30)
        
        self.My_Cert_checkbutton1_picture = Label(self.Printing_window, image=self.Cert_empty_tick_picture, bg='white')
        self.My_Cert_checkbutton2_picture = Label(self.Printing_window, image=self.Cert_empty_tick_picture, bg='white')
        self.My_Cert_checkbutton3_picture = Label(self.Printing_window, image=self.Cert_empty_tick_picture, bg='white')
        self.My_Cert_checkbutton4_picture = Label(self.Printing_window, image=self.Cert_empty_tick_picture, bg='white')
        self.My_Cert_checkbutton5_picture = Label(self.Printing_window, image=self.Cert_empty_tick_picture, bg='white')
        self.My_Cert_checkbutton6_picture = Label(self.Printing_window, image=self.Cert_empty_tick_picture, bg='white')
        
        self.My_Cert_checkbutton1_picture.place(x=560, y=306, width=30, height=30)
        self.My_Cert_checkbutton2_picture.place(x=560, y=376, width=30, height=30)
        self.My_Cert_checkbutton3_picture.place(x=560, y=446, width=30, height=30)
        self.My_Cert_checkbutton4_picture.place(x=790, y=306, width=30, height=30)
        self.My_Cert_checkbutton5_picture.place(x=790, y=376, width=30, height=30)
        self.My_Cert_checkbutton6_picture.place(x=790, y=446, width=30, height=30)
        
        
        
        
        
        #date picker block
        self.date_picker=DateEntry(self.Printing_window, selectmode='none', locale='en_US', date_pattern='D/M/YYYY', font=('Helvetica',20), width=10, height=2, borderwidth=10, justify=CENTER, firstweekday="monday", showothermonthdays=False)
        self.date_picker.place(x=30,y=10)



        self.encoded_list = [
                            ['0','Z'],
                            ['01','A'],
                            ['02','B'],
                            ['03','C'],
                            ['04','D'],
                            ['05','E'],
                            ['06','F'],
                            ['07','G'],
                            ['08','H'],
                            ['09','I'],
                            ['1','A'],
                            ['2','B'],
                            ['3','C'],
                            ['4','D'],
                            ['5','E'],
                            ['6','F'],
                            ['7','G'],
                            ['8','H'],
                            ['9','I'],
                            ['10','J'],
                            ['11','K'],
                            ['12','L']
                            ]

        self.manufacturer_code = 'H'
        self.calendar_date_string = ''
        
        
        
        self.print_button = Button(self.Printing_window, text= "Print", font=('Helvetica',20), width=8, height=2, bg="red", command= lambda : self.Print_button())
        self.print_button.place(x=600, y=500)
            
        
        Change_Printer_Settings_button = Button(self.Printing_window, text="Change printer settings", font=('Helvetica',15), width=20, height=2, bg="white", command= lambda: self.Printer_Settings())
        Change_Printer_Settings_button.place(x=250, y=3)
    
    
    
    
    
    
    
    def Country_Chooser(self):
        
        self.Country_Chooser_Window = Toplevel()
        self.Country_Chooser_Window.title("Country Chooser")
        app_width = 700
        app_height = 400
        x = (self.screen_width / 2) - (app_width /2) - 20
        y = (self.screen_height / 2) - (app_height /2) - 40
        self.Country_Chooser_Window.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')
        self.Country_Chooser_Window.config(background="white")
        self.Country_Chooser_Window.grab_set()
        self.Country_Chooser_Window.resizable(0,0)
        self.Country_Chooser_Window.focus_force()
        
        
        Country_List = [
        "Argentina",
        "Belgium",
        "Burkina Faso",
        "Chile",
        "Ecuador",
        "Egypt",
        "Ehiopia",
        "France",
        "Germany",
        "Greece",
        "Israel",
        "Italy",
        "Kenya",
        "Morocco",
        "Netherlands",
        "Peru",
        "Poland",
        "Portugal",
        "Senegal",
        "South Africa",
        "Spain",
        "Turkey"
        ]
        
        position_x = 0
        position_y = 50
        loop_count = 0
        
        for each in Country_List:
            Country_Button = Button(self.Country_Chooser_Window, text=each, width=20, height=2, font=('Helvetica',10), command=lambda each=each: self.change_country_display_text(each))
            Country_Button.place(x=position_x, y=position_y)
                
            
            if loop_count > 2:
                position_x = 0
                position_y += 50
                loop_count = 0
                
            else:
                position_x += 170
                position_y = position_y
                
                loop_count += 1
    
    
    
    def change_country_display_text(self,each):
        self.country_display["text"]=each
        self.Country_Chooser_Window.destroy()
    
    
    
    def Printer_Settings(self):
        """
        global packet_printer_name #By declaring StrinVar() variables as global variables it helps tkinter to remember the value of them & setting default values for them
        global scale_printer_name
        global small_label_printer_name
        global medium_label_printer_name
        global CTN_label_printer_name
        global Serial_Port_Parity_name
        not sure still needed or not
        """
        
        self.Printing_window.withdraw()
        self.Printer_Settings_window = Toplevel()
        self.Printer_Settings_window.title("Printer Settings")
        app_width = 1050
        app_height = 600
        x = (self.screen_width / 2) - (app_width /2) - 20
        y = (self.screen_height / 2) - (app_height /2) - 40
        self.Printer_Settings_window.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')
        self.Printer_Settings_window.config(background="white")
        self.Printer_Settings_window.resizable(0,0)
        self.Printer_Settings_window.focus_force()
        
        
        # Get the list of available printers
        printers_general_tuple = win32print.EnumPrinters(win32print.PRINTER_ENUM_LOCAL, None, 1)
        printers_list = []
        # Print the list of printers
        for printer in printers_general_tuple:
            printers_list.append(printer[2])

            
        
        count = 0
        printer_settings_list = []
        config_file = open("C:\\Tkinter_Label_Software\\config.ini")
        for line in config_file:
            if (line == -1 or not(line.strip('\n') in printers_list)) and count<=4:
                printer_settings_list.append(win32print.GetDefaultPrinter().strip('\n'))
            else:
                printer_settings_list.append(line.strip('\n'))
            count += 1
        config_file.close()
        
        config_file = open("C:\\Tkinter_Label_Software\\config.ini", "w")
        for each in printer_settings_list:
            config_file.write(each)
            config_file.write("\n")
            
        config_file.close()
        

        
        parity_settings_list = ["None", "Odd"]
          
        self.packet_printer_name = StringVar()
        self.scale_printer_name = StringVar()
        self.small_label_printer_name = StringVar()
        self.medium_label_printer_name = StringVar()
        self.CTN_label_printer_name = StringVar()
        self.Serial_Port_Parity_name = StringVar()
        
        
        self.packet_printer_chooser = ttk.Combobox(self.Printer_Settings_window, font=('Helvetica',20), width = 50, textvariable = self.packet_printer_name, state="readonly")
        self.scale_printer_chooser = ttk.Combobox(self.Printer_Settings_window, font=('Helvetica',20), width = 50, textvariable = self.scale_printer_name, state="readonly")
        self.small_label_printer_chooser = ttk.Combobox(self.Printer_Settings_window, font=('Helvetica',20), width = 50, textvariable = self.small_label_printer_name, state="readonly")
        self.medium_label_printer_chooser = ttk.Combobox(self.Printer_Settings_window, font=('Helvetica',20), width = 50, textvariable = self.medium_label_printer_name, state="readonly")
        self.CTN_label_printer_chooser = ttk.Combobox(self.Printer_Settings_window, font=('Helvetica',20), width = 50, textvariable = self.CTN_label_printer_name, state="readonly")
        self.Serial_Port_Parity_chooser = ttk.Combobox(self.Printer_Settings_window, font=('Helvetica',20), width = 50, textvariable = self.Serial_Port_Parity_name, state="readonly")
        
        self.packet_printer_chooser['values'] = (printers_list)
        self.scale_printer_chooser['values'] = (printers_list)
        self.small_label_printer_chooser['values'] = (printers_list)
        self.medium_label_printer_chooser['values'] = (printers_list)
        self.CTN_label_printer_chooser['values'] = (printers_list)
        self.Serial_Port_Parity_chooser['values'] = (parity_settings_list)
        
        
        Scales_comm_port_label = Label(self.Printer_Settings_window, text= "Scales comm port :", font=('Helvetica',15), width=20, height=2, bg="white", anchor="w")
        Scales_comm_port_label.place(x=10, y=430, height=50)
        self.Scales_comm_port_entry = Entry(self.Printer_Settings_window, text="", font=('Helvetica',20), width = 5, background ="white", borderwidth=3, relief="sunken", justify=CENTER)
        self.Scales_comm_port_entry.place(x=240, y=430, height=50)
        
        
        self.packet_printer_chooser.current(printers_list.index(printer_settings_list[0]))
        self.scale_printer_chooser.current(printers_list.index(printer_settings_list[1]))
        self.small_label_printer_chooser.current(printers_list.index(printer_settings_list[2]))
        self.medium_label_printer_chooser.current(printers_list.index(printer_settings_list[3]))
        self.CTN_label_printer_chooser.current(printers_list.index(printer_settings_list[4]))
        self.Serial_Port_Parity_chooser.current(parity_settings_list.index(printer_settings_list[5]))
        self.Scales_comm_port_entry.insert(0, str(printer_settings_list[6]))
        
        self.packet_printer_chooser.place(x=240, y=10, height=50)
        self.scale_printer_chooser.place(x=240, y=80, height=50)
        self.small_label_printer_chooser.place(x=240, y=150, height=50)
        self.medium_label_printer_chooser.place(x=240, y=220, height=50)
        self.CTN_label_printer_chooser.place(x=240, y=290, height=50)
        self.Serial_Port_Parity_chooser.place(x=240, y=360, height=50)
        
        packet_printer_label = Label(self.Printer_Settings_window, text= "PKT Label Printer :", font=('Helvetica',15), width=20, height=2, bg="white", anchor="w")
        scale_printer_label = Label(self.Printer_Settings_window, text= "Scales Label Printer :", font=('Helvetica',15), width=20, height=2, bg="white", anchor="w")
        small_label_printer_label = Label(self.Printer_Settings_window, text= "Small Label Printer :", font=('Helvetica',15), width=20, height=2, bg="white", anchor="w")
        medium_label_printer_label = Label(self.Printer_Settings_window, text= "Medium Label Printer :", font=('Helvetica',15), width=20, height=2, bg="white", anchor="w")
        CTN_printer_label = Label(self.Printer_Settings_window, text= "CTN Label Printer :", font=('Helvetica',15), width=20, height=2, bg="white", anchor="w")
        Serial_Port_Parity_label = Label(self.Printer_Settings_window, text= "Serial Port Parity :", font=('Helvetica',15), width=20, height=2, bg="white", anchor="w")
        
        packet_printer_label.place(x=10, y=10, height=50)
        scale_printer_label.place(x=10, y=80, height=50)
        small_label_printer_label.place(x=10, y=150, height=50)
        medium_label_printer_label.place(x=10, y=220, height=50)
        CTN_printer_label.place(x=10, y=290, height=50)
        Serial_Port_Parity_label.place(x=10, y=360, height=50)
        
        
        
        
        Save_Printer_Settings_button = Button(self.Printer_Settings_window, text="Save", font=('Helvetica',15), width=8, height=2, bg="white", justify=CENTER, command=lambda: [self.Printer_Settings_Configuration(), self.Unhide_Printing_window()])
        Save_Printer_Settings_button.place(x=700, y=500)
        
        Cancel_Printer_Settings_button = Button(self.Printer_Settings_window, text="Cancel", font=('Helvetica',15), width=8, height=2, bg="white", justify=CENTER, command=lambda: self.Unhide_Printing_window())
        Cancel_Printer_Settings_button.place(x=913, y=500)
        
        self.Printer_Settings_window.protocol("WM_DELETE_WINDOW", self.Unhide_Printing_window)
    
    
    
    
    def Printer_Settings_Configuration(self):
        config_file = open("C:\\Tkinter_Label_Software\\config.ini", "w")
        config_file.write(str(self.packet_printer_chooser.get()))
        config_file.write('\n')
        config_file.write(str(self.scale_printer_chooser.get()))
        config_file.write('\n')
        config_file.write(str(self.small_label_printer_chooser.get()))
        config_file.write('\n')
        config_file.write(str(self.medium_label_printer_chooser.get()))
        config_file.write('\n')
        config_file.write(str(self.CTN_label_printer_chooser.get()))
        config_file.write('\n')
        config_file.write(str(self.Serial_Port_Parity_chooser.get()))
        config_file.write('\n')
        config_file.write(str(self.Scales_comm_port_entry.get()))
        config_file.close()
        
    def Unhide_Printing_window(self):
        self.Printing_window.deiconify()
        self.Printing_window.focus_force()
        self.Printer_Settings_window.destroy()
        
        
        

        
    def validate_date(self):
        self.manufacturer_code = 'H'
        todays_date = datetime.today().strftime('%d/%m/%Y')
        self.calendar_date_string = self.date_picker.get_date()
        
        try:
            user_date_correct_format = self.date_picker.get_date().strftime('%d/%m/%Y')
            self.calendar_date_string = user_date_correct_format

            
        except:
            self.calendar_date_string = todays_date
            self.date_picker.set_date(todays_date)


        self.calendar_date_string = str(self.calendar_date_string)
        temp_calendar_date_string = self.calendar_date_string.split("/")
        day_of_calendar = temp_calendar_date_string[0]
        month_of_calendar = temp_calendar_date_string[1]
        

        
        for i in day_of_calendar:
            for a in self.encoded_list:
                if i == a[0]:
                    self.manufacturer_code = self.manufacturer_code + a[1]
                    
        for a in self.encoded_list:
            if str(month_of_calendar) == a[0]:
                self.manufacturer_code = self.manufacturer_code + a[1]
                break;
    
    
    
    
    def run_two_functions(self):
        self.validate_date()
        
        if self.product_country == "Europe":
            self.product_country = self.country_display.cget("text")
        else:
            pass
        
        
        
        # Get the list of available printers
        printers_general_tuple = win32print.EnumPrinters(win32print.PRINTER_ENUM_LOCAL, None, 1)
        printers_list= []
        # Print the list of printers
        for printer in printers_general_tuple:
            printers_list.append(printer[2])
            
        count = 0
        printer_settings_list = []
        config_file = open("C:\\Tkinter_Label_Software\\config.ini")
        for line in config_file:
            if (line == -1 or not(line.strip('\n') in printers_list)) and count<=4:
                printer_settings_list.append(win32print.GetDefaultPrinter().strip('\n'))
            else:
                printer_settings_list.append(line.strip('\n'))
            count += 1
        config_file.close()
        
        config_file = open("C:\\Tkinter_Label_Software\\config.ini", "w")
        for each in printer_settings_list:
            config_file.write(each)
            config_file.write("\n")
            
        config_file.close()
        
        self.Serial_Port_Parity_number = printer_settings_list[6]
        
        if self.label_size == 1:
            self.printer_name = str(printer_settings_list[1])
        elif self.label_size == 2:
            self.printer_name = str(printer_settings_list[3])
        elif self.label_size == 3:
            self.printer_name = str(printer_settings_list[2])
        else:
            pass
        
        
        if self.Packet_Scale_window_button_status == 1:
            label_handling.Print_Label(self.my_cert_type,
                                       self.sub_cert_type,
                                       self.barcode,
                                       self.main_cert_type,
                                       self.system_name,
                                       self.chinese_name,
                                       self.malay_name,
                                       self.english_name,
                                       self.nav_name,
                                       self.nav_grammage,
                                       self.product_country,
                                       self.origin_RSP,
                                       self.UOM1,
                                       self.UOM2,
                                       self.unit_of_conversion1,
                                       self.unit_of_conversion2,
                                       self.product_database_category,
                                       self.manufacturer_code,
                                       self.calendar_date_string,
                                       self.num_qty_label,
                                       self.printer_name,
                                       self.label_size,
                                       self.customer_group
                                       )
            
        elif self.customer_group == 2 and (self.product_database_category >= 4 and self.product_database_category <= 6):
            label_handling.Print_Label(self.my_cert_type,
                                       self.sub_cert_type,
                                       self.barcode,
                                       self.main_cert_type,
                                       self.system_name,
                                       self.chinese_name,
                                       self.malay_name,
                                       self.english_name,
                                       self.nav_name,
                                       self.nav_grammage,
                                       self.product_country,
                                       self.origin_RSP,
                                       self.UOM1,
                                       self.UOM2,
                                       self.unit_of_conversion1,
                                       self.unit_of_conversion2,
                                       self.product_database_category,
                                       self.manufacturer_code,
                                       self.calendar_date_string,
                                       self.num_qty_label,
                                       self.printer_name,
                                       self.label_size,
                                       self.customer_group
                                       )
        else:
            self.start_the_thread()

    
    
    
    
    def Print_button(self):
        if self.customer_group == 1:
            if self.Packet_Scale_window_button_status == 1:
                self.num_qty_label = self.qty_input.get()
            else:
                self.num_qty_label = 1
                
        elif self.customer_group == 2:
            self.num_qty_label = self.qty_input.get()
            
        else:
            pass
        
        
        if self.customer_group == 1:
            if self.Packet_Scale_window_button_status == 1:
                if self.sub_cert_type > 6 and self.num_qty_label == "":
                    messagebox.showerror(title="GUI.py Line 1527 Error", message="certificate not found!")
                    time.sleep(0.5)
                    messagebox.showerror(title="GUI.py Line 1529 Error", message="label quantity cannot be zero!")
                    
                    self.print_button.config(command= lambda : self.Print_button())
                    self.print_button.place(x=600, y=500)
                    
                elif self.sub_cert_type > 6:
                    messagebox.showerror(title="GUI.py Line 1535 Error", message="certificate not found!")
                    
                    self.print_button.config(command= lambda : self.Print_button())
                    self.print_button.place(x=600, y=500)
                    
                elif self.num_qty_label == "":
                    messagebox.showerror(title="GUI.py Line 1541 Error", message="label quantity cannot be zero!")
                    
                    self.print_button.config(command= lambda : self.Print_button())
                    self.print_button.place(x=600, y=500)
                    
                elif self.num_qty_label.isdigit() == False:
                    messagebox.showerror(title="GUI.py Line 1547 Error", message="numbers only!")
                    
                    self.print_button.config(command= lambda : self.Print_button())
                    self.print_button.place(x=600, y=500)
                    
                else:
                    self.num_qty_label = int(self.num_qty_label)
                    self.run_two_functions()
                    self.print_button.config(command= lambda : self.Print_button())
                    self.print_button.place(x=600, y=500)
                    
            else:
                self.num_qty_label = int(self.num_qty_label)
                self.run_two_functions()
                self.print_button.config(command= lambda : self.Print_button())
                self.print_button.place(x=600, y=500)
                    
        elif self.customer_group == 2:
            if self.sub_cert_type > 6 and self.num_qty_label == "":
                messagebox.showerror(title="GUI.py Line 1560 Error", message="certificate not found!")
                time.sleep(0.5)
                messagebox.showerror(title="GUI.py Line 1562 Error", message="label quantity cannot be zero!")
                
                self.print_button.config(command= lambda : self.Print_button())
                self.print_button.place(x=600, y=500)
                
            elif self.sub_cert_type > 6:
                messagebox.showerror(title="GUI.py Line 1568 Error", message="certificate not found!")
                
                self.print_button.config(command= lambda : self.Print_button())
                self.print_button.place(x=600, y=500)
                
            elif self.num_qty_label == "":
                messagebox.showerror(title="GUI.py Line 1574 Error", message="label quantity cannot be zero!")
                
                self.print_button.config(command= lambda : self.Print_button())
                self.print_button.place(x=600, y=500)
                
            elif self.num_qty_label.isdigit() == False:
                messagebox.showerror(title="GUI.py Line 1580 Error", message="numbers only!")
                
                self.print_button.config(command= lambda : self.Print_button())
                self.print_button.place(x=600, y=500)
                
            else:
                self.num_qty_label = int(self.num_qty_label)
                self.run_two_functions()
                self.print_button.config(command= lambda : self.Print_button())
                self.print_button.place(x=600, y=500)
                
        else:
            pass
    
    
    
    
    def Unhide_product_listing_window(self):
        self.product_listing_window.deiconify()
        #self.product_listing_window.state("zoomed") Fullscreen but with title bar and window taskbar
        #self.product_listing_window.resizable(0,0)
        self.product_listing_window.focus_force()
        self.Printing_window.destroy()
    
    
    
    
    def update(self,temp_sub_cert_type):
        global Printing_window
        self.product_country = self.country_display.cget("text")
        
        if self.Packet_Scale_window_button_status == 1:
            self.num_qty_label = self.qty_input.get()
        else:
            self.num_qty_label = 1
        
        
            
        self.sub_cert_type = temp_sub_cert_type
        
        self.Cert_checkbutton1_picture.destroy()
        self.Cert_checkbutton2_picture.destroy()
        self.Cert_checkbutton3_picture.destroy()
        self.Cert_checkbutton4_picture.destroy()
        self.Cert_checkbutton5_picture.destroy()
        self.Cert_checkbutton6_picture.destroy()

        
        self.Cert_checkbutton1_picture = Label(self.Printing_window, image=self.Cert_empty_tick_picture, bg='white')
        self.Cert_checkbutton1_picture.place(x=560, y=76, width=30, height=30)
        self.Cert_checkbutton2_picture = Label(self.Printing_window, image=self.Cert_empty_tick_picture, bg='white')
        self.Cert_checkbutton2_picture.place(x=560, y=146, width=30, height=30)
        self.Cert_checkbutton3_picture = Label(self.Printing_window, image=self.Cert_empty_tick_picture, bg='white')
        self.Cert_checkbutton3_picture.place(x=560, y=216, width=30, height=30)
        self.Cert_checkbutton4_picture = Label(self.Printing_window, image=self.Cert_empty_tick_picture, bg='white')
        self.Cert_checkbutton4_picture.place(x=790, y=76, width=30, height=30)
        self.Cert_checkbutton5_picture = Label(self.Printing_window, image=self.Cert_empty_tick_picture, bg='white')
        self.Cert_checkbutton5_picture.place(x=790, y=146, width=30, height=30)
        self.Cert_checkbutton6_picture = Label(self.Printing_window, image=self.Cert_empty_tick_picture, bg='white')
        self.Cert_checkbutton6_picture.place(x=790, y=216, width=30, height=30)
        
        
        
                
        if self.sub_cert_type == 1:
            self.Cert_checkbutton1_picture.destroy()
            
            self.Cert_checkbutton1_picture = Label(self.Printing_window, image=self.Cert_tick_picture, bg='blue')
            self.Cert_checkbutton1_picture.place(x=560, y=76, width=30, height=30)

            self.Cert_checkbutton2.deselect()
            self.Cert_checkbutton3.deselect()
            self.Cert_checkbutton4.deselect()
            self.Cert_checkbutton5.deselect()
            self.Cert_checkbutton6.deselect()
            
            
        elif self.sub_cert_type == 2:

            self.Cert_checkbutton2_picture.destroy()
            
            self.Cert_checkbutton2_picture = Label(self.Printing_window, image=self.Cert_tick_picture, bg='blue')
            self.Cert_checkbutton2_picture.place(x=560, y=146, width=30, height=30)
            
            self.Cert_checkbutton1.deselect()
            self.Cert_checkbutton3.deselect()
            self.Cert_checkbutton4.deselect()
            self.Cert_checkbutton5.deselect()
            self.Cert_checkbutton6.deselect()
            

        elif self.sub_cert_type == 3:
            self.Cert_checkbutton3_picture.destroy()
            
            self.Cert_checkbutton3_picture = Label(self.Printing_window, image=self.Cert_tick_picture, bg='blue')
            self.Cert_checkbutton3_picture.place(x=560, y=216, width=30, height=30)
            
            self.Cert_checkbutton2.deselect()
            self.Cert_checkbutton1.deselect()
            self.Cert_checkbutton4.deselect()
            self.Cert_checkbutton5.deselect()
            self.Cert_checkbutton6.deselect()
            

        elif self.sub_cert_type == 4:
            self.Cert_checkbutton4_picture.destroy()
            
            self.Cert_checkbutton4_picture = Label(self.Printing_window, image=self.Cert_tick_picture, bg='blue')
            self.Cert_checkbutton4_picture.place(x=790, y=76, width=30, height=30)
            
            self.Cert_checkbutton2.deselect()
            self.Cert_checkbutton3.deselect()
            self.Cert_checkbutton1.deselect()
            self.Cert_checkbutton5.deselect()
            self.Cert_checkbutton6.deselect()
            

        elif self.sub_cert_type == 5:
            self.Cert_checkbutton5_picture.destroy()
            
            self.Cert_checkbutton5_picture = Label(self.Printing_window, image=self.Cert_tick_picture, bg='blue')
            self.Cert_checkbutton5_picture.place(x=790, y=146, width=30, height=30)
            
            self.Cert_checkbutton2.deselect()
            self.Cert_checkbutton3.deselect()
            self.Cert_checkbutton4.deselect()
            self.Cert_checkbutton1.deselect()
            self.Cert_checkbutton6.deselect()
            

        elif self.sub_cert_type == 6:
            self.Cert_checkbutton6_picture.destroy()
            
            self.Cert_checkbutton6_picture = Label(self.Printing_window, image=self.Cert_tick_picture, bg='blue')
            self.Cert_checkbutton6_picture.place(x=790, y=216, width=30, height=30)
            
            self.Cert_checkbutton2.deselect()
            self.Cert_checkbutton3.deselect()
            self.Cert_checkbutton4.deselect()
            self.Cert_checkbutton5.deselect()
            self.Cert_checkbutton1.deselect()
            

        else:
            print("No Sub Cert")
            pass


                
        if self.Packet_Scale_window_button_status == 1:
            if self.num_qty_label == '':
                messagebox.showerror(title="GUI.py Line 1726 Error", message="label quantity cannot be zero!")
            else:
                self.num_qty_label = int(self.num_qty_label)
    
        
        self.print_button.config(command= lambda : self.Print_button())
        self.print_button.place(x=600, y=500)
    
    
    
    
    
    def my_cert_validation(self,temp_my_cert_type):
        self.my_cert_type = temp_my_cert_type
        
        self.My_Cert_checkbutton1_picture.destroy()
        self.My_Cert_checkbutton2_picture.destroy()
        self.My_Cert_checkbutton3_picture.destroy()
        self.My_Cert_checkbutton4_picture.destroy()
        self.My_Cert_checkbutton5_picture.destroy()
        self.My_Cert_checkbutton6_picture.destroy()
        
        self.My_Cert_checkbutton1.deselect()
        self.My_Cert_checkbutton2.deselect()
        self.My_Cert_checkbutton3.deselect()
        self.My_Cert_checkbutton4.deselect()
        self.My_Cert_checkbutton5.deselect()
        self.My_Cert_checkbutton6.deselect()
        
        self.My_Cert_checkbutton1_picture = Label(self.Printing_window, image=self.Cert_empty_tick_picture, bg='white')
        self.My_Cert_checkbutton2_picture = Label(self.Printing_window, image=self.Cert_empty_tick_picture, bg='white')
        self.My_Cert_checkbutton3_picture = Label(self.Printing_window, image=self.Cert_empty_tick_picture, bg='white')
        self.My_Cert_checkbutton4_picture = Label(self.Printing_window, image=self.Cert_empty_tick_picture, bg='white')
        self.My_Cert_checkbutton5_picture = Label(self.Printing_window, image=self.Cert_empty_tick_picture, bg='white')
        self.My_Cert_checkbutton6_picture = Label(self.Printing_window, image=self.Cert_empty_tick_picture, bg='white')
        self.My_Cert_checkbutton1_picture.place(x=560, y=306, width=30, height=30)
        self.My_Cert_checkbutton2_picture.place(x=560, y=376, width=30, height=30)
        self.My_Cert_checkbutton3_picture.place(x=560, y=446, width=30, height=30)
        self.My_Cert_checkbutton4_picture.place(x=790, y=306, width=30, height=30)
        self.My_Cert_checkbutton5_picture.place(x=790, y=376, width=30, height=30)
        self.My_Cert_checkbutton6_picture.place(x=790, y=446, width=30, height=30)
        
        
        if self.my_cert_type == 1:
            self.My_Cert_checkbutton1_picture.destroy()
            self.My_Cert_checkbutton1_picture = Label(self.Printing_window, image=self.Cert_tick_picture, bg='blue')
            self.My_Cert_checkbutton1_picture.place(x=560, y=306, width=30, height=30)
            self.My_Cert_checkbutton1.select()
            
            
        elif self.my_cert_type == 2:

            self.My_Cert_checkbutton2_picture.destroy()
            
            self.My_Cert_checkbutton2_picture = Label(self.Printing_window, image=self.Cert_tick_picture, bg='blue')
            self.My_Cert_checkbutton2_picture.place(x=560, y=376, width=30, height=30)
            

        elif self.my_cert_type == 3:
            self.My_Cert_checkbutton3_picture.destroy()
            
            self.My_Cert_checkbutton3_picture = Label(self.Printing_window, image=self.Cert_tick_picture, bg='blue')
            self.My_Cert_checkbutton3_picture.place(x=560, y=446, width=30, height=30)
            

        elif self.my_cert_type == 4:
            self.My_Cert_checkbutton4_picture.destroy()
            
            self.My_Cert_checkbutton4_picture = Label(self.Printing_window, image=self.Cert_tick_picture, bg='blue')
            self.My_Cert_checkbutton4_picture.place(x=790, y=306, width=30, height=30)
            

        elif self.my_cert_type == 5:
            self.My_Cert_checkbutton5_picture.destroy()
            
            self.My_Cert_checkbutton5_picture = Label(self.Printing_window, image=self.Cert_tick_picture, bg='blue')
            self.My_Cert_checkbutton5_picture.place(x=790, y=376, width=30, height=30)
            

        elif self.my_cert_type == 6:
            self.My_Cert_checkbutton6_picture.destroy()
            
            self.My_Cert_checkbutton6_picture = Label(self.Printing_window, image=self.Cert_tick_picture, bg='blue')
            self.My_Cert_checkbutton6_picture.place(x=790, y=446, width=30, height=30)
            

        else:
            print("No Sub Cert")
            pass
    
    
    
    
    
    
    
    def start_the_thread(self):
        self.stop_thread = False
        
        t2 = threading.Thread(target=lambda: self.Weighted_Product_Window())
        t3 = threading.Thread(target=lambda: self.Open_Port())
        t2.start()
        t3.start()
    
    
    
    
    
    
    def Weighted_Product_Window(self):
        self.Printing_window.withdraw()
        self.number_of_ledger_entries = 0
        
        self.weigh_window = Toplevel()
        self.weigh_window.title("Weighing product")
        app_width = 1000
        app_height = 600
        x = (self.screen_width / 2) - (app_width /2) - 20
        y = (self.screen_height / 2) - (app_height /2) - 40
        self.weigh_window.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')
        self.weigh_window.config(background="white")
        self.weigh_window.resizable(0,0)
        self.weigh_window.focus_force()
        
        nav_grammage_label = Label(self.weigh_window, text="Product ID:", font=('Helvetica',15), width=10, height=2, anchor="e", background="white", borderwidth=3)
        nav_grammage_label.place(x=80, y=0)
        
        system_name_label = Label(self.weigh_window, text="Name:", font=('Helvetica',15), width=10, height=2, anchor="e", background="white", borderwidth=3)
        system_name_label.place(x=80, y=70)
        
        RSP_label = Label(self.weigh_window, text="Price/KG:", font=('Helvetica',15), width=10, height=2, anchor="e", background="white", borderwidth=3)
        RSP_label.place(x=80, y=140)
        
        weight_label = Label(self.weigh_window, text="Weight:", font=('Helvetica',15), width=10, height=2, anchor="e", background="white", borderwidth=3)
        weight_label.place(x=80, y=190)
        
        scale_label = Label(self.weigh_window, text="Scale status:", font=('Helvetica',15), width=10, height=2, anchor="e", background="white", borderwidth=3)
        scale_label.place(x=80, y=240)
        
        nav_grammage_display = Label(self.weigh_window, text=self.nav_grammage, font=('Helvetica',15), width=60, height=2, anchor="w", background="white", borderwidth=3, justify=LEFT, relief="sunken")
        nav_grammage_display.place(x=200, y=0)
        system_name_display = Label(self.weigh_window, text=self.system_name, font=('Helvetica',15), width=60, height=4, anchor="w", background="white", borderwidth=3, justify=LEFT, relief="sunken", wraplength=400)
        system_name_display.place(x=200, y=50)

        
        two_decimals_RSP = format(float(self.origin_RSP),".2f")
        try:
            self.unit_of_conversion2 = format(float(self.unit_of_conversion2), ".3f")
        except Exception as e:
            with open("C:\\Tkinter_Label_Software\\log.txt", "a") as file:
                current_datetime = datetime.now()
                current_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
                file.write("\n")
                file.write(current_datetime)
                file.write("\n")
                file.write(str(e))
                file.write("\n")
                
            self.unit_of_conversion2 = "0.000"
        RSP_display = Label(self.weigh_window, text=two_decimals_RSP, font=('Helvetica',15), width=60, height=2, anchor="w", background="white", borderwidth=3, justify=LEFT, relief="sunken")
        RSP_display.place(x=200, y=140)
        
        
        self.weight_display = Label(self.weigh_window, text=self.unit_of_conversion2, font=('Helvetica',15), width=60, height=2, anchor="w", background="white", borderwidth=3, justify=LEFT, relief="sunken")
        self.weight_display.place(x=200, y=190)
        

        self.scale_display = Label(self.weigh_window, text="", font=('Helvetica',15), width=60, height=2, anchor="w", background="white", borderwidth=3, justify=LEFT, relief="sunken")
        self.scale_display.place(x=200, y=240)
        
        scale_ledger_columns = ['barcode', 'weight', 'RSP']
        

        self.scales_ledger_listbox = ttk.Treeview(self.weigh_window, columns=scale_ledger_columns, show='headings')
        for i in scale_ledger_columns:
            self.scales_ledger_listbox.column(i, width=166, anchor='w', stretch=0)
        self.scales_ledger_listbox.heading('barcode', text='Barcode')
        self.scales_ledger_listbox.heading('weight', text='Weight')
        self.scales_ledger_listbox.heading('RSP', text='Unit Price')
        self.scales_ledger_listbox.place(x=200, y=350, width=500, height=230)
        self.scales_ledger_listbox.bind('<Button-1>', lambda event: self.handle_click(event))
        #How to pass arguments into event handler
        #self.scales_ledger_listbox.bind('<<TreeviewSelect>>', lambda event, calendar_date_string=calendar_date_string: item_selected(event, calendar_date_string))
        
        delete_ledger_entries_button = Button(self.weigh_window, text="Delete", font=('Helvetica',20), width=8, height=2, bg="yellow", command=lambda: self.delete_ledger_entries_function())
        delete_ledger_entries_button.place(x=750, y=450)
        
        self.weigh_window.protocol("WM_DELETE_WINDOW", lambda : self.update_stop_thread_status())
    
    
    
    def handle_click(self, event):
        #Basically when it detects mouse1 click on the separator on the treeview object it will block the user from resizing it by returning "break" string
        if self.scales_ledger_listbox.identify_region(event.x, event.y) == "separator":
            return "break"
    
    
    
    def delete_ledger_entries_function(self):
        for selected_item in self.scales_ledger_listbox.selection():
            self.scales_ledger_listbox.delete(selected_item)
    
    
    
    
    
    def Open_Port(self):
        if self.stop_thread == True:
            return

        port_status = ""
        
        try:
            self.ser = serial.Serial(port="COM" + self.Serial_Port_Parity_number, baudrate=9600, parity=serial.PARITY_NONE, timeout=0.1)
            list_of_words = ["S", "T", "G", "S", "kg", "KG", "k", "g", "K", "G"]
            origin_barcode = self.barcode
            self.RSP = self.origin_RSP
            self.ser.close()
            time.sleep(1)
            self.scale_display["text"] = "OK"
            self.scale_display["background"] = "#00ff5e"
            
            if self.ser.isOpen() == False:
                self.ser.open()
            
            while self.stop_thread != True:
                raw_data = self.ser.read(20)
                self.ser.flush()
                temp = raw_data.decode('latin-1')
                self.unit_of_conversion2 = [x.strip() for x in temp.split(',')]
                self.unit_of_conversion2 = re.sub('\s+', '', self.unit_of_conversion2[len(self.unit_of_conversion2)-1]) #\s means all whitespaces characters in all encoding, + means replace any of them in this string
                self.unit_of_conversion2 = re.sub('kg', '', self.unit_of_conversion2)
                self.unit_of_conversion2 = re.sub('k', '', self.unit_of_conversion2)
                self.unit_of_conversion2 = re.sub('g', '', self.unit_of_conversion2)
                self.unit_of_conversion2 = re.sub('KG', '', self.unit_of_conversion2)
                self.unit_of_conversion2 = re.sub('K', '', self.unit_of_conversion2)
                self.unit_of_conversion2 = re.sub('G', '', self.unit_of_conversion2)
                
                #if self.unit_of_conversion2 
                
                if any(x in temp for x in list_of_words):
                    try:
                        
                        self.unit_of_conversion2 = Decimal(self.unit_of_conversion2).quantize(Decimal('1.000'))
                        self.RSP = Decimal(self.origin_RSP).quantize(Decimal('1.000'))
                        self.RSP = self.RSP * self.unit_of_conversion2
                        self.RSP = Decimal(self.RSP).quantize(Decimal('1.000'))
                        
                        if self.RSP.as_tuple().digits[-1] == 5:
                            self.RSP = round(round(self.RSP,2) + Decimal(0.01),2) #Decimal function here will turn self.RSP into long decimal again so need to round up second time
                        else:
                            self.RSP = round(self.RSP,2)
        
                        if self.unit_of_conversion2 >= 1:
                            self.UOM2 = str(self.unit_of_conversion2) + "KG"
                            
                        else:
                            self.UOM2 = int(self.unit_of_conversion2 * 1000)
                            self.UOM2 = str(self.UOM2) + "G"
                            
                        print(self.unit_of_conversion2)
                        print(type(self.unit_of_conversion2))
                        
                        if (self.unit_of_conversion2 <= 0.000 or self.unit_of_conversion2 > 30.000):
                            pass
                        else:
                            self.weight_display.destroy()
                            self.barcode = barcode_generator(self.RSP, self.barcode)
                            self.number_of_ledger_entries += 1
                            self.scales_ledger_listbox.insert('', END,values = (str(self.barcode) + "    " +str(self.UOM2) + "    " + str(self.RSP)))
                            self.weight_display = Label(self.weigh_window, text=self.unit_of_conversion2, font=('Helvetica',15), width=60, height=2, anchor="w", background="white", borderwidth=3, justify=LEFT, relief="sunken")
                            self.weight_display.place(x=200, y=190)
                            label_handling.Print_Label(
                                                        self.my_cert_type,
                                                        self.sub_cert_type,
                                                        self.barcode,
                                                        self.main_cert_type,
                                                        self.system_name,
                                                        self.chinese_name,
                                                        self.malay_name,
                                                        self.english_name,
                                                        self.nav_name,
                                                        self.nav_grammage,
                                                        self.product_country,
                                                        self.RSP,
                                                        self.UOM1,
                                                        self.UOM2,
                                                        self.unit_of_conversion1,
                                                        self.unit_of_conversion2,
                                                        self.product_database_category,
                                                        self.manufacturer_code,
                                                        self.calendar_date_string,
                                                        self.num_qty_label,
                                                        self.printer_name,
                                                        self.label_size,
                                                        self.customer_group
                                                        )
                        break;
                    except:
                        pass
                else:
                    pass
    
                port_status = "OK"
                time.sleep(0.1)
            
        
            i = 0
            self.ser.close()
            self.Open_Port()
        
        except Exception as e:
            print(e)
            with open("C:\\Tkinter_Label_Software\\log.txt", "a") as file:
                current_datetime = datetime.now()
                current_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
                file.write("\n")
                file.write(current_datetime)
                file.write("\n")
                file.write(str(e))
                file.write("\n")
            time.sleep(1)
            self.scale_display["text"] = "Error"
            self.scale_display["background"] = "#ff0059"
    
    
    
    
    def update_stop_thread_status(self):
        self.stop_thread = True
        try:
            self.Printing_window.deiconify()
            self.Printing_window.focus_force()
            self.weigh_window.destroy()
        except:
            self.customer_window.destroy()
    
    
    
    
    
    


#Creates a temporary window to make sure potential error messagebox does show up
temp_window = Tk()
try:
    temp_window.destroy()
    t1 = threading.Thread(target=lambda: GUI().Customer_window_init())
    t1.start()
except Exception as e:
    e = str(e)
    with open("C:\\Tkinter_Label_Software\\log.txt", "a") as file:
        current_datetime = datetime.now()
        current_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
        file.write("\n")
        file.write(current_datetime)
        file.write("\n")
        file.write(e)
        file.write("\n")
        messagebox.showerror(title="GUI.py Line 2145 Error", message = e)
temp_window.mainloop()
