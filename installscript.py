import time,os
from pyfiglet import Figlet
from termcolor import colored

ver = "catalina"

def render(text,style):
    f = Figlet(font=style)
    print(f.renderText(text))

render("MacOS KVM install script",'slant')
print(colored('Cloning MacOS-KVM directory...', 'blue'))
os.system("git clone https://github.com/foxlet/macOS-Simple-KVM")
os.system("cd macOS-Simple-KVM")
print(colored('Done!', 'blue'))
print("What version of MacOS you want to download? (default: Catalina)\n1. Catalina\n2. Mojave\n3. High Sierra")
version = input("(1/2/3): ")
if version == "1":
    ver = "catalina"
    textver = "Catalina"
if version == "2":
    ver = "mojave"
    textver = "Mojave"
if version == "3":
    ver = "high-sierra"
    textver = "High Sierra"
print(colored(f'Downloading MacOS {textver}!', 'blue'))
os.system(f'cd macOS-Simple-KVM && ./jumpstart.sh --{ver}')
print(colored('Done!', 'blue'))
print("Now, let's create a new virtual-hard drive!")
size = input("size of the hard drive (in GB): ")
os.system(f'cd macOS-Simple-KVM && qemu-img create -f qcow2 MyDisk.qcow2 {size}G')
print(colored('Moving new basic.sh in place of the old one...', 'blue'))
os.system("chmod +x basic.sh")
os.system("mv basic.sh macOS-Simple-KVM/")
print(colored('Done!', 'blue'))
print("Running MacOS...")
os.system("clear")
os.system("cd macOS-Simple-KVM && sudo ./basic.sh")
print("Thanks for using! have a nice day.")
print("to open macOS again, cd to the directory (macoskvmscript/MacOS-Simple-KVM/) and run ./basic.sh")
quit()