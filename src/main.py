from start import setup
import interpreter
import arguments
import os
import sys
import argparse

if __name__ == "__main__":

    home = os.path.expanduser("~")

    if os.path.exists(f"{home}/.local/share/pass") != True or os.path.exists(f"{home}/.local/share/pass/conf.json") != True:
        setup()
    
    if len(sys.argv) > 1:
        arguments.parse_args(argparse.ArgumentParser())
    
    if len(sys.argv) == 1:
        interpreter.App().cmdloop()