import os
import subprocess


my_env = os.environ.copy()
my_env
my_env.get("PATH", "")
my_env["PATH"] = os.pathsep.join(["/opt/myapp/", my_env["PATH"]])

my_env["PATH"]

result = subprocess.run(["myapp"], env=my_env)

"_".join('Country Name'.split(" "))