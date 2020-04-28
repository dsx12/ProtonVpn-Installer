import os

if __name__ == '__main__':
	commands = ['sudo sudo protonvpn init', 'systemctl enable protonvpn.service',
	'systemctl start protonvpn.service']
	if os.getuid() != 0:
		print('you have to run this script with sudo')
		exit(1)
	try:
		with open('service.txt', 'r') as f:
			contents = f.read()
		with open('/etc/systemd/system/protonvpn.service', 'w') as f:
			f.write(contents)
	except FileNotFoundError as e:
		print('Make sure the service.txt is in the same directory of install.py and the systemd timer path is correct in the script! Error: ', e)
		exit(1)
		
	print('running proton vpn init, enter your configuration settings..')
	for command in commands:
		os.system(command)
	
	print('ProtonVPN installed, now at reboot ProtonVPN will automatically connect')
	print('To check status of protonvpn enter sudo systemctl status protonvpn.service')
