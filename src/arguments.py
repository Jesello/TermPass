import argparse
from functions import *
import crypt
import inputs
from color import *


def key_avaible(key):
    for i in crypt.Crypt().get_keys():
        k,m = i.split(" ")
        
        if key == k:
            return True
            
    return False


def parse_struct(data):
    struct = {}
    
    for i in data:
        try:
            a = i.split("=")
            
            struct[a[0]] = a[1]
        except:
            raise Exception("example usage: pass -n/--new filename -s/--struct user=default password=1234 -k keyname")
    return struct
        

def parse_args(parser):
    
    parser.add_argument("-n","--new")
    parser.add_argument("-r","--remove")
    parser.add_argument("-l","--list",action="store_true")
    parser.add_argument("-K","--keys",action="store_true")
    parser.add_argument("-f","--conf",action="store_true")
    parser.add_argument("-c","--color",action="store_true")
    parser.add_argument("-g","--get")
    parser.add_argument("-k","--key")
    parser.add_argument("-s","--struct",nargs="*")
    
    args = parser.parse_args()
    
    selected = False
    
    if args.new != None and selected == False:
        
        color = Color()
        
        if len(crypt.Crypt().get_keys()) == 0:
            raise ValueError("You have 0 key. Generate one")
        
        if args.key == None and key_avaible(args.key) != True:
            print(c("\n- Key not found manually select -",color.warning_color))
            key = inputs.get_key()
            
        else:
            key = args.key
            
        if args.struct == None or len(args.struct) == 0:
            struct = inputs.get_struct()
        
        try:
            if len(args.struct) > 0:
                struct = parse_struct(args.struct)
        except:
            pass
            
        crypt.Crypt().encrypt(args.new,struct,key)
        
    
    if args.remove != None and selected == False:
        remove_file(args.remove)
        
    if args.list != False and selected == False:
        list_passwords()
        
    if args.keys != False and selected == False:
        list_keys()
        
    if args.conf != False and selected == False:
        view_conf()
        
    if args.color != False and selected == False:
        change_colors()
        
    if args.get != None and selected == False:
        get_password(args.get)