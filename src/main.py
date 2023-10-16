from start import setup
import interpreter
import os
import conf
import sys

if __name__ == "__main__":

    home = os.path.expanduser("~")

    if os.path.exists(f"{home}/.local/share/pass") != True or os.path.exists(f"{home}/.local/share/pass/conf.json") != True:
        setup()

    interpreter.App().cmdloop()
