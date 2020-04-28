
# Tiny Synology DiskStation daemon

This little service was created for a Synology DiskStation DS214+ running Debian
(Buster), but, will probably also work for similar models.

The daemon will turn off the blinking LED at startup and shut the system down
when the power button is pressed.

Installation:

    # git clone https://github.com/easybe/synd.git /usr/local/synd
    # pip3 install -r /usr/local/synd/requirements.txt
    # systemctl enable /usr/local/synd/synd.service
    # systemctl start synd
