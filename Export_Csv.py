# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 15:18:57 2023

@author: user
"""

import os
import mysql.connector

def export_csv():
    username = os.getlogin()
    Desktop_Path = 'C:\\Users\\' + username + '\\Desktop\\'
    Csv_File_name = 'Usoft_Ledger_Entries_'
    Csv_Number = 0
    Csv_Extension = '.csv'
    
    Export_Path = Desktop_Path + Csv_File_name + str(Csv_Number) + Csv_Extension
    # check if file is available in the file system
    
    while True:
        if not os.path.isfile(Export_Path):
        
            list_of_ip = ["123.456.789.0", "223.456.789.0", "323.456.789.0", "423.456.789.0", "523.456.789.0", "623.456.789.0", "723.456.789.0"]
            #a list of servers, live servers or backups
            
            for each in list_of_ip:
                try:
                    server = mysql.connector.connect(user='admin', password='password', host=each, database='database name', port='port name', connection_timeout=1)
                    break;
                except:
                    pass
            
            cur = server.cursor()
            
            query = """SELECT * FROM server_log;"""
            cur.execute(query)
            fetched_result = cur.fetchall()
            
            excel_headers_list = ["Executed Date","Product Manufactured Date","Product ID","Product Barcode", "Product System Name", "Product English Name", "Product Melayu Name", "Product Navision Name","Product Inventory Posting Group","Product Unit Of Measure 1","Product Unit Of Measure 2","Product Unit Of Conversion 1", "Product Unit Of Conversion 2", "Product Country Of Origin", "Product Unit Price", "Product Unit Amount", "Product Main Cert Type","Product Sub Cert Type", "Product My Cert Type", "Product Manufactured Code","Quantity Of Label", "Printer Name", "Size Of Label","Device Identifier", "No."]
            
            with open(Export_Path,"w") as excel_file:
                excel_file.write(','.join(str(y) for y in excel_headers_list))
                excel_file.write("\n")
                
                for each_tuple in fetched_result:
                        excel_file.write(','.join([str(x) for x in each_tuple]))
                        excel_file.write("\n")
            
            break
        else:
            Csv_Number += 1
            Export_Path = Desktop_Path + Csv_File_name + str(Csv_Number) + Csv_Extension
        
            print(Csv_Number)
        
