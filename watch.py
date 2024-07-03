#!/usr/bin/python3

import requests
import config
import json
import db
import datetime
import asyncio
import eval
   
async def get_bug_crowd(url):
    session = requests.session()
    
    session.headers['User-Agent'] = "Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36"
    
    res = session.get(url)
    datas = json.loads(res.content)
    eval.check_target(datas, 'bug_crowd')
    db.save_bugcrowd(datas, config.DB_PATH, config.DB_USER, config.DB_PASS)

async def get_all_domain(url):
    session = requests.session()
    
    session.headers['User-Agent'] = "Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36"
    
    res = session.get(url)
    datas = res.content.decode()
    db.save_domains(datas)
  
async def get_federacy(url):
    session = requests.session()
    
    session.headers['User-Agent'] = "Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36"
    
    res = session.get(url)
    datas = json.loads(res.content)
    eval.check_target(datas, 'federacy')
    db.save_federacy(datas, config.DB_PATH, config.DB_USER, config.DB_PASS)
  
async def get_hackerone(url):
    session = requests.session()
    
    session.headers['User-Agent'] = "Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36"
    
    res = session.get(url)
    datas = json.loads(res.content)
    eval.check_target(datas, 'hackerone')
    db.save_hackerone(datas, config.DB_PATH, config.DB_USER, config.DB_PASS)    

async def get_intigirity(url):
    session = requests.session()
    
    session.headers['User-Agent'] = "Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36"
    
    res = session.get(url)
    datas = json.loads(res.content)
    eval.check_target(datas, 'intigirity')
    db.save_intigirity(datas, config.DB_PATH, config.DB_USER, config.DB_PASS)
    
async def get_yeswehack(url):
    session = requests.session()
    
    session.headers['User-Agent'] = "Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36"
    
    res = session.get(url)
    datas = json.loads(res.content)
    eval.check_target(datas, 'yeswehack')
    db.save_yeswehack(datas, config.DB_PATH, config.DB_USER, config.DB_PASS)  

async def main():
    start = datetime.datetime.now()
    task1 = asyncio.create_task(get_bug_crowd(config.BUG_CROWD))
    task2 = asyncio.create_task(get_all_domain(config.ALL_DOMAIN))
    task3 = asyncio.create_task(get_federacy(config.FEDERACY))
    task4 = asyncio.create_task(get_hackerone(config.HACKERONE))
    task5 = asyncio.create_task(get_intigirity(config.INTIGIRITY))
    task6 = asyncio.create_task(get_yeswehack(config.YESWEHACK))
    await asyncio.wait([task1, task2, task3, task4, task5, task6])
    
    stop= datetime.datetime.now()
    print(stop - start)

if __name__ == "__main__":
    asyncio.run(main())