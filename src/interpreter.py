import cmd
import os
import crypt
import inputs
from functions import *
from start import setup
import conf

class App(cmd.Cmd):

    prompt = '> '

    def do_new(self,args):
        if len(crypt.Crypt().get_keys()) == 0:
            raise ValueError("You have 0 key. Generate one")
            
        if len(args) > 0:
            crypt.Crypt().encrypt(args,inputs.get_struct(),inputs.get_key())

    def do_keys(self,args):
        
        list_keys()

    def do_rm(self,args):
        
        remove_file(args)

    def do_ls(self,args):
        
        list_passwords()

    def do_setup(self,args):
        setup()

    def do_conf(self,args):
        
         view_conf()
    
    def do_color(self,args):
        
        change_colors()
    
    def default(self,args):
        
        get_password(args)

    def emptyline(self):
        pass
    
    def do_cls(self,args):
        os.system("clear")
        
    def clear(self,args):
        os.system("clear")
        
    def do_EOF(self,args):
        exit(0)
        
    def do_exit(self,args):
        exit(0)