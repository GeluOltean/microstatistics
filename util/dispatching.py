import os
import subprocess
import tempfile
import json
import pandas

class SubprocDispatcher(object):
    def __init__(self, df: pandas.DataFrame):
        self.data = df.T.values
        self.data_json = json.dumps({"counts": [list(map(float, x)) for x in self.data]})
        pass

    def exec_univariate(self, flags: list):
        with tempfile.NamedTemporaryFile() as temp:
        # temp = tempfile.NamedTemporaryFile()
            temp.write(self.data_json.encode())
            temp.seek(0)
    
            cmd = subprocess.Popen(["./microecostats-cli", f"-path={temp.name}", *flags], stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT)
            res, err = cmd.communicate()
            temp.close()
            return json.loads(res)
        pass

