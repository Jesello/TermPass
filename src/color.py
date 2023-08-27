import termcolor
import conf
import json

c = lambda x,y: termcolor.colored(x,y)

class Color:
    
    def __init__(self):
        self.conf = conf.conf()
        self.colors = termcolor.COLORS
        self.input_color = self.conf.input_color
        self.warning_color = self.conf.warning_color
        self.info_color = self.conf.info_color
    
    def change_color(self):
        with open(f"{self.conf.home_dir}/.local/share/pass/conf.json","r") as file:
            conf = json.load(file)
        
        print("\nAvaible colors\n")
        
        for i in self.colors:
            print(f"{i} "+termcolor.colored("     ","white",f"on_{i}"))
            
        print()
        while True:
            a = str(input("Select input color: "))
            if (a in self.colors):
                conf["input_color"] = a
                break
            else:
                pass
        
        while True:
            b = input("Select warning color: ")
            if (b in self.colors):
                conf["warning_color"] = b 
                break
            else:
                pass
            
        while True:
            b = input("Select info color: ")
            if (b in self.colors):
                conf["info_color"] = b 
                break
            else:
                pass
        
        
        jo = json.dumps(conf,indent=4)
        
        with open(f"{self.conf.home_dir}/.local/share/pass/conf.json","w") as file:
            file.write(jo)