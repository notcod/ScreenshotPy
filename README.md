

# sudo apt install xfce4 xfce4-goodies tightvncserver dbus-x11 python3 python3-pip firefox-esr apache2 libapache2-mod-wsgi-py3
# vncserver
#PORT 5901
# nohup /var/www/html/cron.sh &>/dev/null &
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