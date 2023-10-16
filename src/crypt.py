import os
import gnupg
import json
import tempfile
import subprocess
import re
import conf

class Crypt:

    def __init__(self):
        self.conf = conf.conf()
        self.home_dir = self.conf.home_dir
        self.tmp = self.conf.tmp
        self.pass_dir = self.conf.pass_dir
        self.gpg = self.conf.gpg

    def get_keys(self):

        keys = list()

        for i in self.gpg.list_keys():
            keys.append(i['uids'][0])

        return keys

    def encrypt(self,file_name,fstruct,key):

        with open(f"{self.tmp}/{file_name}","w") as file:
            jo = json.dumps(fstruct,indent=4)
            file.write(jo)

        subprocess.run(args=["gpg","--output",f"{self.pass_dir}/{file_name}.gpg","--encrypt","--recipient",f"{key}",f"{self.tmp}/{file_name}"])
        os.remove(f"{self.tmp}/{file_name}")

    def decrypt(self,file_name,password):

        with open(f"{self.pass_dir}/{file_name}.gpg","rb") as file:
            decrypted_data = self.gpg.decrypt_file(file,passphrase=password,output=f"{self.tmp}/{file_name}")

        if decrypted_data.ok == False:
            print("\ndecription failed: \n")
            print(decrypted_data.stderr)
            return 1

        with open(f"{self.tmp}/{file_name}","r") as file:

            print()

            out = json.loads(file.read())
            out = json.dumps(out,indent=4)

            print(out,end="\n\n")


        os.remove(f"{self.tmp}/{file_name}")
