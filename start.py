import os

def ops(x):
    os.system(x)


ops("start chrome -Kiosk --app=http://localhost:3000")
ops("start start_flask.exe")
ops("taskkill /F /IM explorer.exe /T")







