import os
import crypt
import inputs
from color import *
import conf


def list_passwords():
    color = Color()
    r = conf.conf()
    
    print(c("\nAll stored passwords:\n",color.info_color))
    for i in [f for f in os.listdir(r.pass_dir) if not f.startswith('.')]:
        a,b = os.path.splitext(i)
        print(f"- {a} -")
    print()


def remove_file(filename):
    r = conf.conf()
    
    try:
        os.remove(f"{r.pass_dir}/{filename}.gpg")
    except:
        pass


def list_keys():
    color = Color()
    
    print(c("\nAll available keys:\n",color.info_color))
    
    for i in crypt.Crypt().get_keys():
        print(f"- {i} -")
    print()


def view_conf():
    r = conf.conf()
    print(f"\n{r.get_conf()}\n")


def change_colors():
    color = Color()
    color.change_color()
    
    print(c("\nRestart to apply new colors",color.info_color))


def get_password(filename):
    r = conf.conf()
    
    if f"{filename}.gpg" in [f for f in os.listdir(r.pass_dir) if not f.startswith('.')]:
        crypt.Crypt().decrypt(filename,inputs.ask_password())