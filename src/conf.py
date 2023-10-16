import json
import os
import gnupg
import tempfile

class conf:
    def __init__(self):
        self.home_dir = os.path.expanduser("~")
        self.conf = json.load(open(f"{self.home_dir}/.local/share/pass/conf.json"))
        self.pass_dir = self.conf["pass_dir"]
        self.gpg = gnupg.GPG(gnupghome=self.conf["gnupg_dir"])
        self.tmp = tempfile.gettempdir()
        self.input_color = self.conf["input_color"]
        self.warning_color = self.conf["warning_color"]
        self.info_color = self.conf["info_color"]

    def get_conf(self):
        conf = json.load(open(f"{self.home_dir}/.local/share/pass/conf.json"))
        conf = json.dumps(conf,indent=4)

        return conf
