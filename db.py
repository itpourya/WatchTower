#!/usr/bin/python3

import pymongo
import sqlite3

def save_bugcrowd(data, path, username, password):
    dbpath = path+username+"@"+password
    client = pymongo.MongoClient(dbpath)
    
    db = client["watch"]
    collection = db["bug_crowd"]
    collection.delete_many({})
    collection.insert_many(data)
    
    client.close()   
    
def save_domains(datas):
    conn = sqlite3.connect("db/database.sqlite")
    cur = conn.cursor()

    cur.execute("DROP TABLE IF EXISTS domains")
    cur.execute("""CREATE TABLE IF NOT EXISTS domains (
                domain TEXT);""")
    
    conn.commit()
    
    for data in datas.split('\n'):
        query = f'INSERT INTO domains VALUES ("{data}")'
        cur.execute(query)
        conn.commit()
        
    conn.close()
    
def save_federacy(data, path, username, password):
    dbpath = path+username+"@"+password
    client = pymongo.MongoClient(dbpath)
    
    db = client["watch"]
    collection = db["federacy"]
    collection.delete_many({})
    collection.insert_many(data)
    
    client.close() 
    
def save_hackerone(data, path, username, password):
    dbpath = path+username+"@"+password
    client = pymongo.MongoClient(dbpath)
    
    db = client["watch"]
    collection = db["hackerone"]
    collection.delete_many({})
    collection.insert_many(data)
    
    client.close() 
    
def save_intigirity(data, path, username, password):
    dbpath = path+username+"@"+password
    client = pymongo.MongoClient(dbpath)
    
    db = client["watch"]
    collection = db["intigirity"]
    collection.delete_many({})
    collection.insert_many(data)
    
    client.close() 
    
def save_yeswehack(data, path, username, password):
    dbpath = path+username+"@"+password
    client = pymongo.MongoClient(dbpath)
    
    db = client["watch"]
    collection = db["yeswehack"]
    collection.delete_many({})
    collection.insert_many(data)
    
    client.close() 