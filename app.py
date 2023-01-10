from flask import Flask
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from time import sleep
from flask import request
import os
import hashlib
import validators

location = "/var/www/html/"
location = ""

app = Flask(__name__)

@app.route('/')
def index():
    content = ""
    domain = request.args.get('domain', default = "", type = str)
    if domain != '':
        if validators.url(domain):
            name = randName()
            f = open(location + 'tasks/' + name, "a")
            f.write(domain)
            f.close()

            waiting = 0
            image = location + "static/images/" + name + ".png"

            link = "/static/images/" + name + ".png"
            content = "<a href='" + link + "' target='_blank'>" + link + "<br>"
            content += "<img src='" + link + "' width='300px'></a><br>"
            while not os.path.exists(image):
                waiting += 1
                sleep(1)
                if waiting > 15:
                    content = "Unexpected error<br>"
        else:
            content = "Not valid domain"

    return content + '<hr><form><label>Type website:</label><input type="text" name="domain" placeholder="domain"><input type="submit"></form>'

def randName():
    return hashlib.sha256(os.urandom(64)).hexdigest()

def screenshot(domain, task):
    options = Options()
    options.add_argument('--headless')

    driver = webdriver.Firefox(options=options)
    driver.get(domain)
    sleep(1)

    image = task + ".png"

    driver.get_screenshot_as_file(location + "static/images/" + image)
    driver.quit()
    return location + "static/images/" + image

def getScreenshot():
    tasks = os.listdir(location + "tasks")

    for task in tasks:
        file = open(location + "tasks/" + task, "r")
        domain = file.read()
        if domain != '':
            screenshot(domain, task)
        os.remove(location + "tasks/"+ task)

if __name__ == '__main__':
    app.run()



# sudo apt install xfce4 xfce4-goodies tightvncserver dbus-x11 python3 python3-pip firefox-esr apache2 libapache2-mod-wsgi-py3
# vncserver
#PORT 5901

# chmod -R a+rwX /var/www/html/tasks


        # vncserver -kill :1
        # mv ~/.vnc/xstartup ~/.vnc/xstartup.bak
        # nano ~/.vnc/xstartup
            # #!/bin/bash
            # xrdb $HOME/.Xresources
            # startxfce4 &

        # sudo chmod +x ~/.vnc/xstartup
        # vncserver

# https://www.digitalocean.com/community/tutorials/how-to-install-and-configure-vnc-on-debian-11