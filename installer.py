import os

if __name__ == '__main__':
	if os.getuid() != 0:
		print('you have to run this script with sudo')
		exit(1)

	try:
		with open('service.txt', 'r') as f:
			contents = f.read()
		with open('/etc/systemd/system/protonvpn.service', 'w') as f:
			f.write(contents)
	except FileNotFoundError as e:
		print(e)
		print('Make sure the service.txt is in the same directory of install.py!')
		exit(1)
	
	print('running proton vpn init, enter your configuration settings..')
	os.system('sudo sudo protonvpn init')
	os.system('systemctl enable protonvpn.service')
	os.system('systemctl start protonvpn.service')
