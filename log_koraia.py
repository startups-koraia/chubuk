import subprocess

process = subprocess.Popen("tail -f ../log/sp_firedetect_20230912.log", stdout=subprocess.PIPE, shell=True)

while True:
    output = process.stdout.readline()
    if output == b'' and process.poll() is not None:
        break
    if b'start capture.read(frame)' in output:
        print("System Exit")
        process.kill()
        break
    if output:
        print(output.strip())
