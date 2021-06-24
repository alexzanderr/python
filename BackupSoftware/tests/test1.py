import subprocess
process = subprocess.Popen(r"pscp -P 22 -pw uuu123 C:\Users\dragonfire\.ssh\debian_home_server_key.pub root@192.168.1.234:/root/alexzander/test/", stdout=subprocess.PIPE, stderr=subprocess.PIPE)
out, err = process.communicate()
out = out.decode("utf-8").strip()
err = err.decode("utf-8").strip()
print(out)
print(err)

if err:
    process = subprocess.Popen(r'plink root@192.168.1.234:/root/alexzander/ -pw uuu123 "mkdir test"', stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = process.communicate()
    out = out.decode("utf-8").strip()
    err = err.decode("utf-8").strip()
    print(out)
    print(err)

    process = subprocess.Popen(r"pscp -P 22 -pw uuu123 C:\Users\dragonfire\.ssh\debian_home_server_key.pub root@192.168.1.234:/root/alexzander/test/", stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = process.communicate()
    out = out.decode("utf-8").strip()
    err = err.decode("utf-8").strip()
    print(out)
    print(err)
