# GPU BOT

This is a bot to buy GPUs online.

1. Install or update WSL 2
2. Install and create Virtual Environment
3. Install Selenium and Chromedriver

# Cost of Usage
Firstly using bots is against service agreement to website, if they explicitly state that. Check to see if there is an API before attempting any botting of a website.

The estimated Network Data usage per month

Each request to a website (headless) = 1MB

Depending on number of GPUs and Number of Links that this script should be watching: 30 Links

The script should check once every second

30mb per second

86400 seconds in a day

2,592,00mb or 2,592gb or 2.5tb per day

Because of this, using rotating proxies is not cost efficent.

Instead using a VPN is a better idea.

So 30 VPNs to use this script at semi-capacity

Which means 30 virtual machines, 30 headless_alertbot.py running in parallel

## 30 Links to Watch

Why 30 Links, 30 links is not all of the links. 30vpns and 30 virtual machines can be doable. The reasons is because there is no notification on drops or they are too slow. So we need to have our own alert system to watch for stock in real time by the second.

Once there is stock, there can be one script like a sniper_bot scipt that is activated on another system and it goes to that link and because now there is stock, it can click the buy button and finish with checkout.

For example: 3060, 3060TI, 3070, 3080, 3090, but not any of the 6800, 6800XT, 6900, 6900XT
Then which websites that hold stock: Bestbuy.com, Newegg.com, Amazon.com

NVIDIA GeForce RTX 3060 Ti 8GB GDDR6 PCI Express 4.0 Graphics Card Steel and Black 900-1G142-2520-000 - Best Buy

EVGA NVIDIA GeForce RTX 3060 Ti FTW3 GAMING 8GB GDDR6 PCI Express 4.0 Graphics Card 08G-P5-3667-KB - Best Buy

GIGABYTE NVIDIA GeForce RTX 3060 Ti GAMING OC 8G GDDR6 PCI Express 4.0 Graphics Card Black GV-N306TGAMING OC-8GD - Best Buy

EVGA NVIDIA GeForce RTX 3060 Ti FTW3 GAMING 8GB GDDR6 PCI Express 4.0 Graphics Card 08G-P5-3667-KR - Best Buy

GIGABYTE NVIDIA GeForce RTX 3060 Ti EAGLE OC 8G GDDR6 PCI Express 4.0 Graphics Card Black GV-N306TEAGLE OC-8GD - Best Buy

EVGA NVIDIA GeForce RTX 3060 Ti XC GAMING 8GB GDDR6 PCI Express 4.0 Graphics Card 08G-P5-3663-KR - Best Buy

MSI NVIDIA Geforce RTX 3060 Ti VENTUS 2X OC BV 8GB GDDR6 PCI Express 4.0 Graphics Card Black Geforce RTX 3060 Ti VENTUS 2X OC BV - Best Buy

## Development Environment

(Windows Subsystem for Linux) WSL2 

Ubuntu 20.02

Python 3

Pip 3

VirtualEnv

## Installing WSL2 

Powershell with Admin

Enable Windows Subsystem for Linux 

    dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart

Enable Virtual Machine feature

    dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart

Update Linux Kernel update package

x64 machines

    https://wslstorestorage.blob.core.windows.net/wslblob/wsl_update_x64.msi

Set WSL 2 as default

    wsl --set-default-version 2

## Install Pip3

    sudo apt-get install python3-pip

## Install VirtualEnv

    python3 -m pip install --user virtualenv

## Install ensurepip

Install ensurepip with python3-venv package

    sudo apt-get install python3-venv

## Create Virtual Environement

    python3 -m venv env

##  Activate Virtual Environement

    source env/bin/activate

The environment is active when there is:

    (env) user@device

## Installing Chromedriver in WSL 2

Method uses X server

Installing Chrome

    sudo apt-get update

    sudo apt-get install -y curl unzip xvfb libxi6 libgconf-2-4

Chrome itself:

    wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb

    sudo apt install ./google-chrome-stable_current_amd64.deb

Ensure it worked:

    google-chrome --version

    Installing ChromeDriver

Find the URL of the ChromeDriver version that matches your Chrome version on the ChromeDriver website. It should be a zip file; in my case it’s https://chromedriver.storage.googleapis.com/86.0.4240.22/chromedriver_linux64.zip.

Download, unzip, and put it in your bin directory:

    wget https://chromedriver.storage.googleapis.com/86.0.4240.22/chromedriver_linux64.zip
    unzip chromedriver_linux64.zip
    sudo mv chromedriver /usr/bin/chromedriver
    sudo chown root:root /usr/bin/chromedriver
    sudo chmod +x /usr/bin/chromedriver

Double check it worked:

    chromedriver --version

If you had previously installed ChromeDriver in Windows and were using it in WSL from the Path, make sure you aren’t pointing to that one anymore:

which chromedriver # should be /usr/bin/chromedriver
The X Server

Download and install VcXsrv in Windows. Once installed, run xlaunch.exe (from the VcXsrv folder in Program Files). You can leave most of the settings as default, but make sure to check “Disable access control”.

In Linux the DISPLAY environment variable tells GUI applications at which IP address the X Server is that we want to use. Since in WSL2 the IP address of Windows land is not localhost anymore, we need to set DISPLAY to the correct IP address:

    export DISPLAY=$(cat /etc/resolv.conf | grep nameserver | awk '{print $2; exit;}'):0.0

Just Run command into terminal

I recommend you put this in your .bashrc or whatever the equivalent is for your distro.

Now if you run echo $DISPLAY you should get something like 172.17.35.177:0.0.

All done

If you run google-chrome the Linux-side Chrome should open inside an X server window in Windows! This will also “just work” when ChromeDriver tries to open Chrome when you run your automated tests.

https://www.gregbrisebois.com/posts/chromedriver-in-wsl2/

## Install Selenium

    sudo apt-get install selenium

## Test

    import time
    from selenium import webdriver

    driver = webdriver.Chrome('/usr/bin/chromedriver')  # Optional argument, if not specified will search path.
    driver.get('http://www.google.com/');
    time.sleep(5) # Let the user actually see something!
    search_box = driver.find_element_by_name('q')
    search_box.send_keys('ChromeDriver')
    search_box.submit()
    time.sleep(5) # Let the user actually see something!
    driver.quit()

Run on terminal

    python3 test.py

To find path of chromedriver

    whereis chromedriver

## How to deactivate Virtual Environment

    env/bin/deactivate

## Freeze and create requirements

    pip3 freeze > requirements.txt

