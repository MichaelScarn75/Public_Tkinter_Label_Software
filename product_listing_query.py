# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 15:49:34 2023

@author: user
"""

"""
for i in P_CON:
    print(type(i))
P_CON = [list(i) for i in P_CON]
print(P_CON)
"""
import mysql.connector

def sql_queries(customer_button_number):
    list_of_ip = ["123.456.789.0", "223.456.789.0", "323.456.789.0", "423.456.789.0", "523.456.789.0", "623.456.789.0", "723.456.789.0"]
    #a list of servers, live servers or backups
    
    for each in list_of_ip:
        try:
            sql_database = mysql.connector.connect(user='admin', password='password', host=each, database='database name', port='port name', connection_timeout=1)
            print(each)
            break;
        except:
            pass
        
    cur = sql_database.cursor(buffered=True)
    
    print(customer_button_number)
    cur.execute(f'SELECT * FROM product_listing.p_con WHERE ProductDatabaseCategory=1 AND CustomerGroup={customer_button_number}')
    P_CON = cur.fetchall()
    cur.execute(f'SELECT * FROM product_listing.p_con WHERE ProductDatabaseCategory=2 AND CustomerGroup={customer_button_number}')
    P_OIC = cur.fetchall()
    cur.execute(f'SELECT * FROM product_listing.p_con WHERE ProductDatabaseCategory=3 AND CustomerGroup={customer_button_number}')
    P_OGG = cur.fetchall()
    cur.execute(f'SELECT * FROM product_listing.p_con WHERE ProductDatabaseCategory=4 AND CustomerGroup={customer_button_number}')
    W_CON = cur.fetchall()
    cur.execute(f'SELECT * FROM product_listing.p_con WHERE ProductDatabaseCategory=5 AND CustomerGroup={customer_button_number}')
    W_OIC = cur.fetchall()
    cur.execute(f'SELECT * FROM product_listing.p_con WHERE ProductDatabaseCategory=6 AND CustomerGroup={customer_button_number}')
    W_OGG = cur.fetchall()
    
    cur.close()
    return P_CON, P_OIC, P_OGG, W_CON, W_OIC, W_OGG
