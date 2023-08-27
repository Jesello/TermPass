import termcolor
import os
import json

def setup():
    try:
        os.makedirs(f"{os.environ['HOME']}/.local/share/pass")
    except:
        pass
    
    conf = {}
    colors = termcolor.COLORS
    
    conf["gnupg_dir"] = input("\nWhere is the main gnupg directory: ")
    conf["pass_dir"] = input("Where you want to store passwords: ")
    
    print("\nAvaible colors\n")
    
    for i in colors:
        print(f"{i} "+termcolor.colored("     ","white",f"on_{i}"))
        
    print()
    
    while True:
        a = str(input("Select input color: "))
        if (a in colors):
            conf["input_color"] = a
            break
        else:
            pass
        
    while True:
        b = input("Select warning color: ")
        if (b in colors):
            conf["warning_color"] = b 
            break
        else:
            pass
            
    while True:
        c = input("Select info color: ")
        if (c in colors):
            conf["info_color"] = c
            break
        else:
            pass
            
    jo = json.dumps(conf,indent=4)
    
    with open(f"{os.environ['HOME']}/.local/share/pass/conf.json","w") as file:
        file.write(jo)

    exit(0)