import subprocess

subprocess.run("date")
subprocess.run("git status", shell=True)
subprocess.run(["sleep", "4"])
subprocess.run(["ls", "no_file"])


result = subprocess.run(["host", "8.8.8.8"], capture_output=True)
print(result.returncode)
print(result.stdout)
print(result.stdout.decode().split())

result = subprocess.run(["host", "google.com"], capture_output=True, text=True, check=True)
print(result.stdout.strip())

result = subprocess.run(["rm", 'doesnot_exist'], capture_output=True)
print(result.returncode)
print(result.stderr)
print(result.stderr.decode().split())