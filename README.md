# ProtonVpn-Installer
Lightweight python script to install systemd service to run protonvpn at boot/startup as systemd service.

Edit the service.txt file to match your path to protonvpn binary!
* Installation:

`git clone https://github.com/dsx12/ProtonVpn-Installer`

`cd ProtonVpn-Installer`

`sudo python3 install.py`

To check if everything is working correctly run:

`sudo service protonvpn status`

Or alternatively:

`sudo systemctl status protonvpn.service`
