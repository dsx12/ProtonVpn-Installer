# ProtonVpn-Installer
Lightweight python script to install systemd service to run protonvpn at boot/startup as systemd service.

Edit the service.txt file to match your path to protonvpn binary!
* Installation:

`git clone https://github.com/dsx12/ProtonVpn-Installer`

`cd ProtonVpn-Installer`

`sudo python3 install.py`

To run:

`sudo service protonvpn start`

Alternatively:

`sudo systemctl start protonvpn.service`
