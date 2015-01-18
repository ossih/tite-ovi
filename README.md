# tite-ovi

### Shortly

Simple programs to monitor statuses of doors at guild room.

### Installation

Compile ovi.c

    gcc -o ovi ovi.c

Give ovi binary permission to execute and copy it under $PATH

    chmod +x ovi
    cp ovi /usr/local/sbin/

To make status available via network, create inetd entry

    update-inetd --add "5000 stream tcp nowait root /usr/sbin/tcpd /usr/local/sbin/ovi"
    /etc/init.d/openbsd-inetd restart 

Copy ovi.py somewhere and give it permission to execute

    chmod +x ovi.py
    cp ovi.py /usr/local/bin/

Done with installation!

### Configuration

Edit ovi.py to set IP address of host running door status server

Add crontab entry to make ovi.py run whenever you want

Jobs done! Now you are ready to go!
