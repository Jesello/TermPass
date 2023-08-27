import cmd
import os
import crypt
import inputs
from color import *
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
        
        color = Color()
    
        print(c("\nAll available keys:\n",color.info_color))
        
        for i in crypt.Crypt().get_keys():
            print(f"- {i} -")
        print()

    def do_rm(self,args):
        
        r = conf.conf()
        
        try:
            os.remove(f"{r.pass_dir}/{args}.gpg")
        except:
            pass

    def do_ls(self,args):
        
        color = Color()
        r = conf.conf()
    
        print(c("\nAll stored passwords:\n",color.info_color))
        for i in [f for f in os.listdir(r.pass_dir) if not f.startswith('.')]:
            a,b = os.path.splitext(i)
            print(f"- {a} -")
        print()

    def do_setup(self,args):
        setup()

    def do_conf(self,args):
        
         r = conf.conf()
         print(f"\n{r.get_conf()}\n")
    
    def do_color(self,args):
        
        color = Color()
        color.change_color()
        
        print(c("\nRestart to apply new colors",color.info_color))
    
    def default(self,args):
        
        r = conf.conf()
        
        if f"{args}.gpg" in [f for f in os.listdir(r.pass_dir) if not f.startswith('.')]:
            crypt.Crypt().decrypt(args,inputs.ask_password())

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