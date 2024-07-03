#!/usr/bin/python3

import pymongo
import config
import json
import requests
import notif

def getData(target_name, collection_name):
    targets = []
    dbpath = config.DB_PATH+config.DB_USER+"@"+config.DB_PASS
    client = pymongo.MongoClient(dbpath)
    
    db = client["watch"]
    collection = db[collection_name]
    try:
        for x in collection.find({'name':target_name}, {"_id":0}):
            scop = x['targets']['in_scope']
            count = 0
            for count in range(len(scop)):
                if scop[count]['type'] == 'website':
                    targets.append(scop[count]['target'])
                
                count += 1
    except:
        targets = []
    return targets
        
def check_target(datas, platform):
    new_targets = []
    
    for data in datas:
        try:
            database_targets = getData(data['name'], platform)
            scop = data['targets']['in_scope']
            
            for count in range(len(scop)):
                if scop[count]['type'] == 'website':
                    new_targets.append(scop[count]['target'])

                count += 1
            
            for new in new_targets:
                if new in database_targets:
                    pass
                elif database_targets == []:
                    notif.send_notif(data['name'], platform, new)
                else:
                    notif.send_notif(data['name'], platform, new)
                    
            break
        except:
            pass