# Mac OS KVM install script
a simple script with simplicity in mind. create a MacOS virtual machine with virtualization support with just few commands!
<p align="center">
  <img src="https://media.discordapp.net/attachments/839233065020162058/839233107071860797/Screenshot_from_2021-05-04_21-57-31.png?width=788&height=443" />
</p>

## Dependencies
```bash
sudo apt-get install qemu-system qemu-utils python3 python3-pip  # for Ubuntu, Debian, Mint, and PopOS.
sudo pacman -S qemu python python-pip python-wheel  # for Arch.
sudo xbps-install -Su qemu python3 python3-pip   # for Void Linux.
sudo zypper in qemu-tools qemu-kvm qemu-x86 qemu-audio-pa python3-pip  # for openSUSE Tumbleweed
sudo dnf install qemu qemu-img python3 python3-pip # for Fedora
sudo emerge -a qemu python:3.4 pip # for Gentoo

pip3 install pyfiglet
pip install termcolor

i think that is all :)
```

## Installation
simply clone the directory and run installscript.py
```bash
git clone https://github.com/KrychaTech/MacOS-KVM-Installscript/
cd MacOS-KVM-Installscript
python3 installscript.py
```
after that, follow the instructions!

## editing basic.sh
the machine uses 8gb of ram and 6 cores by default.
if you want to change it, you can do it by editing the basic.sh (included with this repo)
```bash
# changing ram:
# edit -m 8G \ to:
-m 4G \ # gives machine 4GB of ram
-m 16G \ # gives machine 16gb of ram
# Changing cores
# edit -smp 4,cores=6 \ to:
-smp 4,cores=2 \ # gives machine 2 cores
-smp 4,cores=8 \ # gives machine 8 cores
```

## Credits
all the credits go to https://github.com/foxlet/ for creating the MacOS-KVM repo.

## Screenshots 
![alt text](https://cdn.discordapp.com/attachments/839233065020162058/839237589412216932/Screenshot_from_2021-05-04_21-37-10.png)
![alt text](https://media.discordapp.net/attachments/839233065020162058/839237589412216932/Screenshot_from_2021-05-04_21-37-10.png?width=788&height=443)
![alt text](https://media.discordapp.net/attachments/839233065020162058/839238103952654406/Screenshot_from_2021-05-04_21-37-18.png)
