
import urllib3, requests


loginurl="https://www.kizphonics.com/amember/login"
user_login=""
user_password=""
login_var='amember_login'
passwd_var='amember_pass'
targetDirAbsPath = ''
urlFileName = "urls"

lines = open(urlFileName, "r")
s = requests.Session()
s.get(loginurl)
user_login = user_login
user_password = user_password

r = s.post(loginurl, data={login_var: user_login, passwd_var:user_password}, allow_redirects=True)
print(r.content)

for file in lines:
    print("Getting file: "+str(file.split('/')[-1].rstrip()))
    #print(file.split('/')[-1].rstrip())
    #print(file.rstrip())
    try:
        r2 = s.get(file.rstrip())
    #print(r2.content)
        open(targetDirAbsPath+str(file.split('/')[-1].rstrip()), 'wb').write(r2.content)
    except:
        print("error, try one more time.")
        try:
            r2 = s.get(file.rstrip())
        #print(r2.content)
            open(targetDirAbsPath+str(file.split('/')[-1].rstrip()), 'wb').write(r2.content)
        except:
            print("Fail again, file name: "+file.split('/')[-1].rstrip()+" Try next file")

