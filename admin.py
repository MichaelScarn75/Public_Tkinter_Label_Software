# -*- coding: utf-8 -*-
"""
Created on Mon May 15 11:34:57 2023

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

class admin():
    
    def Login_Window(self):
        self.login_window = Tk()
        self.login_window.title("Choose Customer")
        app_width = 900
        app_height = 600
        self.screen_width = self.login_window.winfo_screenwidth()
        self.screen_height = self.login_window.winfo_screenheight()
        x = (self.screen_width / 2) - (app_width /2)
        y = (self.screen_height / 2) - (app_height /2)
        self.login_window.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')
        self.login_window.resizable(0,0)
        self.login_window.config(background="white")
        self.login_window.focus_force()
        self.login_window.grab_set()
        
        Username_label = Label(self.login_window, text="Username: ", font=('Helvetica', 15), background="white")
        Password_label = Label(self.login_window, text="Password: ", font=('Helvetica', 15), background="white")
        
        Username_entrybox = Text(self.login_window, font=('Helvetica',15), width=30,height=1, background="white",relief="sunken", borderwidth=3)
        Password_entrybox = Text(self.login_window, font=('Helvetica',15), width=30,height=1, background="white",relief="sunken", borderwidth=3)
        
        Username_label.place(x = 200, y = 100)
        Password_label.place(x = 200, y = 200)
        Username_entrybox.place(x = 300, y = 100)
        Password_entrybox.place(x = 300, y = 200)
        
        self.login_window.mainloop()
        
    

admin().Login_Window()
