# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 10:58:54 2023

@author: user
"""

import mysql.connector
from datetime import datetime

def log_function(my_cert_type, cert_type_var, barcode, main_cert_type, system_name, chinese_name, malay_name, english_name, nav_name, nav_grammage, product_country, RSP, UOM1, UOM2, unit_of_conversion1, unit_of_conversion2, product_database_category, manufacturer_code, calendar_date_string, num_qty_label, printer_name, label_size, mac_address):
    my_cert_type = str(my_cert_type)
    sub_cert_type = str(cert_type_var)
    barcode = str(barcode)
    main_cert_type = str(main_cert_type)
    system_name = str(system_name)
    chinese_name = str(chinese_name)
    malay_name = str(malay_name)
    english_name = str(english_name)
    nav_name = str(nav_name)
    nav_grammage = str(nav_grammage)
    product_country = str(product_country)
    RSP = str(RSP)
    UOM1 = str(UOM1)
    UOM2 = str(UOM2)
    unit_of_conversion1 = str(unit_of_conversion1)
    unit_of_conversion2 = str(unit_of_conversion2)
    product_database_category = str(product_database_category)
    manufacturer_code = str(manufacturer_code)
    calendar_date_string = str(calendar_date_string)
    num_qty_label = str(num_qty_label)
    printer_name = str(printer_name)
    label_size = str(label_size)
    mac_address = str(mac_address)
    
    if my_cert_type == "1":
        my_cert_type="04·006/J-007"
    elif my_cert_type == "2":
        my_cert_type="10·0013/J-066"
    elif my_cert_type == "3":
        my_cert_type="10·0011/J-070"
    elif my_cert_type == "4":
        my_cert_type="05·0005/J-019"
    elif my_cert_type == "5":
        my_cert_type="15·00013/C-185"
    elif my_cert_type == "6":
        my_cert_type="07.10/B33"
    else:
        pass
    
    if sub_cert_type == "1":
        sub_cert_type="NasaaMyOrganic"
    elif sub_cert_type == "2":
        sub_cert_type="Nasaa"
    elif sub_cert_type == "3":
        sub_cert_type="MyOrganic"
    elif sub_cert_type == "4":
        sub_cert_type="NasaaIC"
    elif sub_cert_type == "5":
        sub_cert_type="NasaaICMyOrganic"
    elif sub_cert_type == "6":
        sub_cert_type="OrganicThailand"
    else:
        pass
    
    if main_cert_type == "1":
        main_cert_type = "CON"
    elif main_cert_type == "2":
        main_cert_type = "OIC"
    elif main_cert_type == "3":
        main_cert_type = "OGG"
    else:
        pass
    
    if label_size == "1":
        label_size = "60X90MM"
    elif label_size == "2":
        label_size = "60X50MM"
    elif label_size == "3":
        label_size = "40X35MM"
    else:
        pass
    
    
    list_of_ip = ["123.456.789.0", "223.456.789.0", "323.456.789.0", "423.456.789.0", "523.456.789.0", "623.456.789.0", "723.456.789.0"]
    #a list of servers, live servers or backups
    
    for each in list_of_ip:
        try:
            log = mysql.connector.connect(user='admin', password='password', host=each, database='database name', port='port name', connection_timeout=1)
            break;
        except:
            pass
    

    cur = log.cursor()
    
    log_query = ("INSERT INTO server_log\
                (ExecutedDate,\
                ProductManufacturedDate,\
                ProductID,\
                ProductBarcode,\
                ProductSystemName,\
                ProductEnglishName,\
                ProductMelayuName,\
                ProductNavisionName,\
                ProductInventoryPostingGroup,\
                ProductUnitOfMeasure1,\
                ProductUnitOfMeasure2,\
                ProductUnitOfConversion1,\
                ProductUnitOfConversion2,\
                ProductCountryOfOrigin,\
                ProductUnitPrice,\
                ProductUnitAmount,\
                ProductMainCertType,\
                ProductSubCertType,\
                ProductMyCertType,\
                ProductManufacturedCode,\
                QuantityOfLabel,\
                PrinterName,\
                ProductLabelSize,\
                DeviceIdentifier)\
                VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)")
                    
    Posting_Group_query = ("SELECT ProductInventoryPostingGroup FROM p_con WHERE ProductID=%s;")
    cur.execute(Posting_Group_query, (nav_grammage,)) #value must be in tuple
    inventory_posting_group = cur.fetchall()
    inventory_posting_group = inventory_posting_group[0][0]
    
    datetime_now = datetime.now()
    datetime_string = datetime_now.strftime("%d/%m/%Y %H:%M:%S")
    str(datetime_string)
    
    cur.execute(log_query, (datetime_string,calendar_date_string,nav_grammage,barcode,system_name,english_name,malay_name,nav_name,inventory_posting_group,UOM1,UOM2,unit_of_conversion1,unit_of_conversion2,product_country,RSP,RSP,main_cert_type,sub_cert_type,my_cert_type,manufacturer_code,num_qty_label,printer_name,label_size, mac_address))
    log.commit()
    cur.close()
