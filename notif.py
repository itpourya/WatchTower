#!/usr/bin/python3

from discordwebhook import Discord

def send_notif(target_name, target_platform, change):
    discord = Discord(url="#")
    
    msg = f'***{target_name}*** (New on {target_platform}) added some new domains:\n ` {change} \t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t` \n\n'
    
    discord.post(content=msg)
