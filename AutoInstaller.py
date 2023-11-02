#! /usr/bin/python3
# -*- coding: utf-8 -*-
import os
import sys
from getpass import getpass


#sudo dpkg --configure -a

def execute_as_root(root_password,command):
    os.system('echo %s|sudo -S %s' % (root_password,command))

def what_is_it(program_name):
    print("\n==================== Install " + program_name + " ====================")

def update_packege(root_password):
    print("\n==================== Update ====================")
    os.system('echo %s|sudo -S %s' % (root_password, "sudo apt update"))

def upgrade_packeges(root_password):
    print("\n==================== Upgrade ====================")
    os.system('echo %s|sudo -S %s' % (root_password, "sudo apt upgrade --yes"))

def apt_install(root_password,program_name):
    os.system('echo %s|sudo -S %s' % (root_password, "sudo apt install " + program_name + " --yes"))

def flatpak(root_password):
    what_is_it("flatpak")
    apt_install(root_password,"flatpak")
    update_packege(root_password)
    execute_as_root(root_password,"flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo")

def fix_plank(root_password):
    print("==================== Fix Plank ====================")
    os.system('echo %s|sudo -S %s' % (root_password,"gsettings set net.launchpad.plank.dock.settings:/net/launchpad/plank/docks/dock1/ show-dock-item false")) #  Remove anchor icon in Plank
    print("Done!")

def fix_gedit(root_password):
    print("==================== Fix Gedit ====================")
    os.system('echo %s|sudo -S %s' % (root_password,'gsettings set org.gnome.gedit.preferences.encodings candidate-encodings' + '"' + "['UTF-8', 'WINDOWS-1251', 'KOI8-R', 'CURRENT', 'ISO-8859-15', 'UTF-16']" + '"'))
    print("Done!")

def apt_clean(root_password):
    print("==================== Cleaning ====================")
    print("> autoremove")
    os.system('echo %s|sudo -S %s' % (root_password, "sudo apt autoremove --yes"))
    print("> autoclean")
    os.system('echo %s|sudo -S %s' % (root_password, "sudo apt autoclean --yes"))
    print("> clean")
    os.system('echo %s|sudo -S %s' % (root_password, "sudo apt clean --yes"))

def logo():
    print("######################################")
    print("#            AutoInstaller           #")
    print("######################################")
    print("By AlexNottaBen")

def clear():
    os.system("clear")

# Begin
clear()
logo()
root_password = getpass("Input Root Password > ")
clear()
logo()

ChooseMethodForDebian = False
ChooseflatpakMethod = False

do_clean = "0"
IsFixingDependencies = "0"
IsUpdate = "0"
IsUpgrade = "0"
UpdateMicroCodeIntel = "0"
UpdateMicroCodeAmd64 = "0"
Isfix_gedit = "0"
Isfix_plank = "0"
Installflatpak = "0"
InstallVLC = "0"
InstallMPV = "0"
InstallGIMP = "0"
InstallKrita = "0"
InstallMyPaint = "0"
InstallInkScape = "0"
Installblender = "0"
InstallSweetHome3D = "0"
InstallScratch = "0"
InstallScratch3 = "0"
InstallFileZilla = "0"
InstallCaja = "0"
InstallTimeShift = "0"
InstallPeaZip = "0"
InstallKdenline = "0"
InstallOpenShot = "0"
InstallAudacity = "0"
InstallGrubCustomizer = "0"
InstallVBOX = "0"
InstallNotepadqq = "0"
InstallNotepadplusplus = "0"
InstallWine = "0"
InstallPlayOnLinux = "0"
InstallFireFox = "0"
InstallLibreWolf = "0"
InstallThunderBird = "0"
InstallChromium = "0"
InstallUnGoogledChromium = "0"
InstallTor = "0"
InstallShotWell = "0"
InstallVSC = "0"
InstallLibreOffice = "0"
InstallBleachBit = "0"
InstallStacer = "0"
InstallCheese = "0"
InstallGparted = "0"
InstallQbitTorrent = "0"
InstallSSR = "0"
InstallOBS = "0"
InstallSteam = "0"
InstallPidgin = "0"
InstallTelegram = "0"
InstallTeams = "0"
InstallLutris = "0"
InstallGpp = "0"
InstallArduinoIDLE = "0"
InstallPython3IDLE = "0"
InstallClamAV = "0"
InstallIPTables = "0"  #  !!!
InstallUFW = "0"
InstallPitivi = "0"
InstallMousePad = "0"
InstallKate  = "0"
InstallPyCharm = "0"
InstallGodotEngine = "0"
InstallCodeBlocks = "0"
InstallMediaCodes = "0"
InstallKolourPaint = "0"
InstallDoubleCmd = "0"
InstallGnomeDisk = "0"
InstallBaobab = "0"
InstallBlender = "0"
InstallGnomeSoftware = "0"

print("0 - Custom")
print("1 - Default (For Debian and Debian-based OS)")
print("2 - Default (For Ubuntu and Ubuntu-based OS)")
print("3 - Education")
print("4 - Entertaiments")
print('5 - "Fast" MS Teams')
print('6 - Content Creation')
print('7 - Only Updating')
print('8 - Only Basic Fixing and Cleaning')
print('P1 - All For Python Developer')
print('P2 - All For Godot Developer')

Selected = input("Select > ")

if Selected == "1":
    UpdateMicroCodeIntel = "1"
    Installflatpak = "1"
    IsUpdate = "1"
    IsUpgrade = "1"
    Isfix_plank = "1"
    InstallVLC = "1"
    InstallGIMP = "1"
    InstallPeaZip = "1"
    InstallVBOX = "1"
    InstallWine = "1"
    InstallLibreWolf = "1"
    InstallTor = "1"
    InstallVSC = "1"
    InstallUnGoogledChromium = "1"
    InstallLibreOffice = "1"
    InstallGparted = "1"
    InstallQbitTorrent = "1"
    InstallSSR = "1"
    InstallSteam = "1"
    InstallTelegram = "2"
    InstallTeams = "1"
    InstallGpp = "1"
    InstallArduinoIDLE = "0"
    InstallPython3IDLE = "0"
    do_clean = "1"
    IsFixingDependencies = "1"
    InstallShotWell = "1"
    InstallStacer = "1"
    InstallCodeBlocks = "1"
    InstallKdenline = "1"
    InstallKolourPaint = "1"
    InstallGnomeDisk = "1"
    InstallDoubleCmd = "1"
    InstallBaobab = "1"
    InstallGnomeSoftware = "1"
    ChooseMethodForDebian = True
    ChooseflatpakMethod = True

if Selected == "2":
    UpdateMicroCodeIntel = "1"
    Installflatpak = "1"
    IsUpdate = "1"
    IsUpgrade = "1"
    Isfix_plank = "1"
    InstallVLC = "1"
    InstallGIMP = "1"
    InstallPeaZip = "1"
    InstallVBOX = "1"
    InstallNotepadplusplus = "0"
    InstallWine = "1"
    InstallLibreWolf = "1"
    InstallUnGoogledChromium = "1"
    InstallTor = "1"
    InstallVSC = "1"
    InstallLibreOffice = "1"
    InstallGparted = "1"
    InstallQbitTorrent = "1"
    InstallSSR = "1"
    InstallSteam = "1"
    InstallTelegram = "2"
    InstallTeams = "1"
    do_clean = "1"
    IsFixingDependencies = "1"
    InstallShotWell = "1"
    InstallStacer = "1"
    InstallKate = "1"
    InstallGpp = "1"
    InstallPyCharm = "0"
    InstallCaja = "1"  #  For Open The Trash by The Plank on Debian
    InstallCodeBlocks = "1"
    InstallKrita = "1"
    InstallKdenline = "1"
    InstallKolourPaint = "1"
    InstallGnomeDisk = "1"
    InstallDoubleCmd = "1"
    InstallBaobab = "1"
    InstallKolourPaint = "1"
    InstallGnomeSoftware = "1"
    ChooseMethodForDebian = False
    ChooseflatpakMethod = False

if Selected == "3":
    Installflatpak = "0"
    IsUpdate = "1"
    IsUpgrade = "1"
    Isfix_plank = "1"
    InstallVLC = "1"
    InstallGIMP = "1"
    InstallPeaZip = "1"
    InstallVBOX = "1"
    InstallFireFox = "1"
    InstallVSC = "1"
    InstallLibreOffice = "1"
    InstallBleachBit = "1"
    InstallGparted = "1"
    InstallQbitTorrent = "1"
    InstallSSR = "1"
    InstallTeams = "1"
    InstallGnomeSoftware = "1"
    do_clean = "1"
    IsFixingDependencies = "1"

if Selected == "4":
    Installflatpak = "0"
    IsUpdate = "1"
    IsUpgrade = "1"
    InstallSSR = "1"
    InstallSteam = "1"
    InstallWine = "1"
    InstallPlayOnLinux = "1"
    InstallLutris = "1"
    InstallGnomeSoftware = "1"
    do_clean = "1"
    IsFixingDependencies = "1"

if Selected == "5":
    Installflatpak = "0"
    IsUpdate = "1"
    Isfix_plank = "1"
    InstallSSR = "1"
    InstallTeams = "1"
    do_clean = "1"
    IsFixingDependencies = "1"

if Selected == "6":
    Installflatpak = "0"
    IsUpdate = "1"
    IsUpgrade = "1"
    InstallGIMP = "1"
    InstallVLC = "1"
    InstallKdenline = "1"
    do_clean = "1"
    IsFixingDependencies = "1"

if Selected == "7":
    Installflatpak = "0"
    IsUpdate = "1"
    IsUpgrade = "1"

if Selected == "8":
    Installflatpak = "0"
    IsUpdate = "1"
    IsUpgrade = "1"
    do_clean = "1"
    IsFixingDependencies = "1"

if Selected == "F":
    UpdateMicroCodeIntel = "1"
    Installflatpak = "1"
    IsUpdate = "1"
    IsUpgrade = "1"
    InstallVLC = "1"
    InstallGIMP = "1"
    InstallPeaZip = "1"
    InstallWine = "1"
    InstallPlayOnLinux = "1"
    InstallFireFox = "0"
    InstallChromium = "0"
    InstallUnGoogledChromium = "1"
    InstallTor = "1"
    InstallLibreOffice = "1"
    InstallBleachBit = "0"
    InstallGparted = "1"
    InstallQbitTorrent = "1"
    InstallSSR = "1"
    InstallTeams = "0"
    do_clean = "1"
    IsFixingDependencies = "1"
    InstallXnViewMP = "1"
    InstallCaja = "1"  #  For Open The Trash by The Plank on Debian
    InstallKrita = "1"
    InstallKdenline = "1"
    InstallGnomeDisk = "1"
    InstallDoubleCmd = "1"
    InstallBaobab = "1"
    InstallKolourPaint = "1"
    InstallStacer = "1"
    InstallGnomeSoftware = "1"
    ChooseMethodForDebian = False
    ChooseflatpakMethod = False

if Selected == "Y":
    UpdateMicroCodeIntel = "1"
    Installflatpak = "1"
    InstallGIMP = "1"
    InstallVLC = "1"
    InstallQbitTorrent = "1"
    InstallLibreOffice = "1"
    InstallPeaZip = "1"
    InstallStacer = "1"
    InstallNotepadqq = "1"
    InstallThunderBird = "1"
    InstallSteam = "1"
    InstallTelegram = "2"
    InstallSSR = "1"
    InstallScratch3 = "1"
    InstallVBOX = "1"
    InstallDiscord = "1"
    InstallGnomeSoftware = "1"
    ChooseMethodForDebian = False
    ChooseflatpakMethod = False

if Selected == "0":
    IsUpdate = "1"
    IsUpgrade = "1"
    print("==================== Set Basic Setting ====================")
    UpdateMicroCodeIntel = input("Update MicroCode For Intel (No = 0/Yes = 1): = ")
    UpdateMicroCodeAmd64 = input("Update MicroCode For Amd64 (No = 0/Yes = 1): = ")
    InstallMediaCodes = input("Install Media Codes (No = 0/Yes = 1): = ")
    Isfix_gedit = input("Use this If Cyrillic is not displayed in the Gedit text editor! (No = 0/Yes = 1): = ")
    Isfix_plank = input("Remove anchor icon in Plank (No = 0/Yes = 1): = ")
    print("==================== Install Programs ====================")
    Installflatpak = input("[Open-Source] Flatpak - System for collecting self-sufficient packages (No = 0/Yes = 1): = ")
    InstallVLC = input("[Open-Source] VLC - MediaPlayer (No = 0/Yes = 1): = ")
    InstallGIMP = input("[Open-Source] GIMP - Raster Graphic Editor (No = 0/Yes = 1): = ")
    InstallKrita = input("[Open-Source] Krita - Raster Graphic Editor (No = 0/Yes = 1/Yes[flatpak] = 2): = ")
    InstallMyPaint = input("[Open-Source] MyPaint - Raster Graphic Editor (No = 0/Yes = 1): = ")
    InstallKolourPaint = input("[Open-Source] KolourPaint - Raster Graphic Editor (No = 0/Yes = 1): = ")
    InstallInkScape = input("[Open-Source] InkScape - Vector Graphic Editor (No = 0/Yes = 1): = ")
    InstallBlender = input("[Open-Source] Blender - 3D Editor (No = 0/Yes = 1/Yes[flatpak] = 2): = ")
    InstallSweetHome3D = input("[Open-Source] Sweet Home 3D - 3D Home Editor (No = 0/Yes = 1): = ")
    InstallScratch = input("[Open-Source] Scratch - Game Developer Tools (No = 0/Yes = 1): = ")
    InstallScratch3 = input("[Open-Source] Scratch 3 - Game Developer Tools (No = 0/Yes = 1): = ")
    InstallFileZilla = input("[Open-Source] FileZilla - FTP Client (No = 0/Yes = 1): = ")
    InstallCaja = input("[Open-Source] Caja - The File Manager of MATE (No = 0/Yes = 1): = ")
    InstallTimeShift = input("[Open-Source] TimeShift - Alternative to Time Machine (No = 0/Yes = 1): = ")
    InstallPeaZip = input("[Open-Source] PeaZip - Alternative to WinRar (No = 0/Yes = 1/Yes[flatpak] = 2): = ")
    InstallKdenline = input("[Open-Source] Kdenline - Open KDE Video Editor (No = 0/Yes = 1): = ")
    InstallOpenShot = input("[Open-Source] OpenShot - Open Video Editor (No = 0/Yes = 1): = ")
    InstallPitivi = input("[Open-Source] Pitivi - Open Video Editor (No = 0/Yes = 1): = ")
    InstallAudacity = input("[Open-Source] Audacity - Open Audio Editor (No = 0/Yes = 1): = ")
    InstallGrubCustomizer = input("[Unknown] Grub Customizer - For Grub Customition (No = 0/Yes = 1): = ")
    InstallVBOX = input("[Open-Source] Virtual Box - Virtual Computer (No = 0/Yes = 1): = ")
    InstallNotepadqq = input("[Open-Source] Notepadqq - Text Editor (No = 0/Yes = 1): = ")
    InstallNotepadplusplus = input("[Open-Source] Notepad++ - Text Editor (No = 0/Yes = 1): = ")
    InstallWine = input("[Open-Source] Wine - Windows API (No = 0/Yes = 1): = ")
    InstallPlayOnLinux = input("[Open-Source] PlayOnLinux - For Run Windows Apps (No = 0/Yes = 1): = ")
    InstallLutris = input("[Open-Source] Lutris - For Run Windows Games (No = 0/Yes = 1): = ")
    InstallThunderBird = input("[Open-Source] ThunderBird - Open Mail Client(No = 0/Yes = 1): = ")
    InstallLibreWolf = input("[Open-Source] LibreWolf - Open Web-broweser(No = 0/Yes = 1): = ")
    InstallFireFox = input("[Open-Source] FireFox - Open Web-broweser(No = 0/Yes = 1): = ")
    InstallChromium = input("[Open-Source] Chromium - Open Web-broweser(No = 0/Yes = 1): = ")
    InstallUnGoogledChromium = input("[Open-Source] Ungoogled Chromium - Open Web-broweser(No = 0/Yes = 1): = ")
    InstallTor = input("[Open-Source] Tor Browser - Web-broweser by Tor Project (No = 0/Yes = 1): = ")
    InstallShotWell = input("[Open-Source] ShotWell - Image Viewer, Alternative to XnView MP (No = 0/Yes = 1): = ")
    InstallKate = input("[Open-Source] Kate - KDE Text Editor, Alternative to Sublime Text(No = 0/Yes = 1): = ")
    InstallMousePad = input("[Open-Source] MousePad - XFCE Text Editor (No = 0/Yes = 1): = ")
    InstallPyCharm = input("[Open-Source] PyCharm Community - Community IDE Editor (No = 0/Yes = 1/Yes = 2[flatpak]): = ")
    InstallVSC = input("[Open-Source] VScodium - Development Environment (No = 0/Yes = 1): = ")
    InstallLibreOffice = input("[Open-Source] Libre Office - OpenSource Office (No = 0/Yes = 1): = ")
    InstallBleachBit = input("[Open-Source] BleachBit - Alternative to Piriform Capt_clean (No = 0/Yes = 1): = ")
    InstallStacer = input("[Open-Source] Stacer - Alternative to Piriform Capt_clean (No = 0/Yes = 1): = ")
    InstallCheese = input("[Open-Source] Cheese - Camera (No = 0/Yes = 1): = ")
    InstallGparted = input("[Open-Source] Gparted - Disk Utility (No = 0/Yes = 1): = ")
    InstallQbitTorrent = input("[Open-Source] Qbittorrent - Torrent Client  (No = 0/Yes = 1): = ")
    InstallTransmission = input("[Open-Source] Transmission - Torrent Client  (No = 0/Yes = 1): = ")
    InstallSSR = input("[Open-Source] Simple Screen Recorder - Screen Recorder  (No = 0/Yes = 1): = ")
    InstallOBS = input("[Open-Source] OBS Studio - Screen Recorder  (No = 0/Yes = 1): = ")
    InstallSteam = input("[Proprietary Freeware] Steam - Center For Games and Software (No = 0/Yes = 1): = ")
    InstallPidgin = input("[Open-Source] Pidgin - For Chating (No = 0/Yes = 1): = ")
    InstallTelegram = input("[Open-Source Client/Proprietary Server] Telegram - For Chating (No = 0/Yes = 1/Yes[flatpak] = 2): = ")
    InstallTeams = input("[Proprietary Software] Microsoft Teams - For Study (No = 0/Yes = 1): = ")
    InstallGpp = input("[Open-Source] G++ - C++ Compiler (No = 0/Yes = 1): = ")
    InstallArduinoIDLE = input("[Open-Source] Arduino IDLE - IDLE for Arduino (No = 0/Yes = 1): = ")
    InstallPython3IDLE = input("[Open-Source] Python3 IDLE - IDLE for Python (No = 0/Yes = 1): = ")
    InstallClamAV = input("[Open-Source] ClamAV - AntiVirus Program(No = 0/Yes = 1): = ")
    InstallGodotEngine = input("[Open-Source] Godot Engine - Game Engine(No = 0/Yes = 1[flatpak]): = ")
    InstallCodeBlocks = input("[Open-Source] Code::Blocks - Alternative to Dev-C++ (No = 0/Yes = 1/Yes[flatpak] = 2): = ")
    InstallGnomeDisk = input("[Open-Source] Gnome Disk - Disk Utility (No = 0/Yes = 1/Yes[flatpak]): = ")
    InstallDoubleCmd = input("[Open-Source] Double commander - Alternative to Total commander (No = 0/Yes = 1): = ")
    InstallBaobab = input("[Open-Source] Baobab - Disk Analyzer (No = 0/Yes = 1): = ")

print("\n==================== Start ====================\n")

#Update
if IsUpdate == "1":
	update_packege(root_password)
if IsUpgrade == "1":
	upgrade_packeges(root_password)

# Check
if UpdateMicroCodeIntel == "1":
    what_is_it("MicroCode For Intel")
    apt_install(root_password,"--reinstall intel-microcode")

if UpdateMicroCodeAmd64 == "1":
    what_is_it("MicroCode For Amd64")
    apt_install(root_password,"--reinstall amd64-microcode")

# TODO Redo
if InstallMediaCodes == "1":
    what_is_it("Media Codes")
    apt_install(root_password,"ubuntu-restricted-extras")

#Fixes
if Isfix_gedit == "1":
    fix_gedit(root_password)

if Isfix_plank == "1":
    fix_plank(root_password)

#Installs
if Installflatpak == "1":
    flatpak(root_password)

if InstallVLC == "1":
    what_is_it("VLC")
    apt_install(root_password,"vlc")

if InstallVLC == "1":
    what_is_it("MPV")
    apt_install(root_password,"mpv")

if InstallGIMP == "1":
    what_is_it("GIMP")
    apt_install(root_password,"gimp")

if InstallKrita == "1":
    what_is_it("Krita")
    apt_install(root_password,"krita")

if InstallKrita == "2":
    what_is_it("Krita [flatpak]")
    execute_as_root(root_password,"flatpak install flathub org.kde.krita -y")

if InstallMyPaint == "1":
    what_is_it("MyPaint")
    apt_install(root_password,"mypaint-data")
    apt_install(root_password,"mypaint")

if InstallMyPaint == "1":
    what_is_it("KolourPaint")
    apt_install(root_password,"kolourpaint")

if InstallInkScape == "1":
    what_is_it("InkScape")
    apt_install(root_password,"inkscape")

if InstallBlender == "1":
    what_is_it("Blender")
    apt_install(root_password,"blender")
elif InstallBlender == "2":
    what_is_it("Blender")
    execute_as_root(root_password,"flatpak install flathub <!!!> -y") # TODO

if InstallSweetHome3D == "1":
    what_is_it("SweetHome3D")
    apt_install(root_password,"sweethome3d")

# TODO Add Turbowarp
if InstallScratch == "1":
    what_is_it("Scratch")
    apt_install(root_password,"scratch")

if InstallScratch3 == "1":
    what_is_it("Scratch 3")
    flatpak(root_password)
    execute_as_root(root_password,"flatpak install flathub edu.mit.Scratch -y")

if InstallFileZilla == "1":
    what_is_it("FileZilla")
    apt_install(root_password,"filezilla")

if InstallCaja == "1":
    what_is_it("Caja")
    apt_install(root_password,"caja")

if InstallKdenline == "1":
    what_is_it("Kdenline")
    if not ChooseMethodForDebian:
        execute_as_root(root_password,"sudo add-apt-repository ppa:kdenlive/kdenlive-stable --yes")
    update_packege(root_password)
    apt_install(root_password,"kdenlive")

if InstallOpenShot == "1":
    what_is_it("OpenShot")
    apt_install(root_password,"openshot")

if InstallPitivi == "1":
    what_is_it("Pitivi")
    apt_install(root_password,"pitivi")

if InstallAudacity == "1":
    what_is_it("Audacity")
    apt_install(root_password,"audacity")

if InstallGrubCustomizer == "1":
    what_is_it("GrubCustomizer")
    apt_install(root_password,"grub-customizer")

# TODO Check
if InstallVBOX == "1":
    what_is_it("Virtualbox")
    if ChooseMethodForDebian:
        update_packege(root_password)
        execute_as_root(root_password,"wget -q https://www.virtualbox.org/download/oracle_vbox_2016.asc -O- | sudo apt-key add -")
        execute_as_root(root_password,'echo "deb [arch=amd64] http://download.virtualbox.org/virtualbox/debian bionic contrib" | sudo tee /etc/apt/sources.list.d/virtualbox.list')
        update_packege(root_password)
        apt_install(root_password,"virtualbox-6.1")
        '''
        virtualbox-6.1 (6.1.24-145767~Ubuntu~bionic)
        virtualbox-6.0 (6.0.24-139119~Ubuntu~bionic)
        virtualbox-5.2 (5.2.44-139111~Ubuntu~bionic)
        virtualbox-5.1 (5.1.38-122592~Ubuntu~bionic)
        '''
    else:
        apt_install(root_password,"virtualbox")

if InstallNotepadplusplus == "1":
    what_is_it("Notepad++")
    update_packege(root_password)
    # TODO !!!

if InstallNotepadqq == "1":
    what_is_it("Notepadqq")
    apt_install(root_password,"notepadqq")

if InstallPidgin == "1":
    what_is_it("Pidgin")
    apt_install(root_password,"pidgin")

if InstallTelegram == "2":
    what_is_it("Telegram [flatpak]")
    flatpak(root_password)
    execute_as_root(root_password,"flatpak install flathub org.telegram.desktop -y")

if InstallTelegram == "1":
    what_is_it("Telegram")
    # TODO !!!

if InstallWine == "1":
    what_is_it("Wine")
    apt_install(root_password,"wine")

if InstallGparted == "1":
    what_is_it("Gparted")
    apt_install(root_password,"gparted")

# TODO Check
if InstallPlayOnLinux == "1":
    what_is_it("PlayOnLinux")
    if ChooseMethodForDebian:
        execute_as_root(root_password,"sudo dpkg --add-architecture i386")
        apt_install(root_password,"netcat")
        execute_as_root(root_password,'wget -q "http://deb.playonlinux.com/public.gpg" -O- | apt-key add -')
        execute_as_root(root_password,"wget http://deb.playonlinux.com/playonlinux_wheezy.list -O /etc/apt/sources.list.d/playonlinux.list")
        update_packege(root_password)
        apt_install(root_password,"playonlinux")
        execute_as_root(root_password,"sudo apt-get update && sudo apt-get upgrade && sudo apt-get dist-upgrade")
        apt_install(root_password,"multiarch-support libgl1-mesa-glx:i386")
    else:
        apt_install(root_password,"playonlinux")
        apt_install(root_password,"winbind")
        apt_install(root_password,"winetricks")

if InstallLutris == "1":
    what_is_it("Lutris")
    execute_as_root(root_password,"sudo add-apt-repository ppa:lutris-team/lutris --yes")
    update_packege(root_password)
    apt_install(root_password,"lutris")

if InstallThunderBird == "1":
    what_is_it("ThunderBird")
    apt_install(root_password,"thunderbird")

# TODO Check
if InstallLibreWolf == "1":
    what_is_it("LibreWolf")
    execute_as_root(root_password,'distro=$(if echo " bullseye focal impish jammy uma una " | grep -q " $(lsb_release -sc) "; then echo $(lsb_release -sc); else echo focal; fi) && echo "deb [arch=amd64] http://deb.librewolf.net $distro main" | sudo tee /etc/apt/sources.list.d/librewolf.list && sudo wget https://deb.librewolf.net/keyring.gpg -O /etc/apt/trusted.gpg.d/librewolf.gpg && sudo apt update -y && sudo apt install librewolf -y')

if InstallFireFox == "1":
    what_is_it("FireFox")
    if ChooseMethodForDebian:
        apt_install(root_password,"firefox-esr")
    else:
        apt_install(root_password,"firefox")

if InstallChromium == "1":
    what_is_it("Chromium")
    apt_install(root_password,"chromium-browser")

if InstallChromium == "2":
    what_is_it("Chromium [flatpak]")
    flatpak(root_password)
    execute_as_root(root_password,"flatpak install flathub org.chromium.Chromium -y")

if InstallUnGoogledChromium == "1":
    what_is_it("Ungoogled Chromium")
    flatpak(root_password)
    execute_as_root(root_password,"flatpak install flathub com.github.Eloston.UngoogledChromium -y")

if InstallTor == "1":
    what_is_it("Tor Browser")
    apt_install(root_password,"torbrowser-launcher")

if InstallTor == "2":
    what_is_it("Tor Browser [flatpak]")
    flatpak(root_password)
    execute_as_root(root_password,"flatpak install flathub com.github.micahflee.torbrowser-launcher -y")

if InstallShotWell == "1":
    what_is_it("ShotWell")
    apt_install(root_password,"shotwell")


if InstallTimeShift == "1":
    what_is_it("TimeShift")
    if not ChooseMethodForDebian:
        execute_as_root(root_password,'sudo apt-add-repository -y ppa:teejee2008/ppa')
    update_packege(root_password)
    apt_install(root_password,"timeshift")

# TODO Redo installation processs
if InstallPeaZip == "1":
    what_is_it("PeaZip")
    execute_as_root(root_password,"wget https://github.com/peazip/PeaZip/releases/download/7.8.0/peazip_7.8.0.LINUX.x86_64.GTK2.deb")
    apt_install(root_password,"gdebi-core")
    apt_install(root_password,"libatk1.0-0:i386 libc6:i386 libcairo2:i386 libgdk-pixbuf2.0-0:i386 libglib2.0-0:i386 libgtk2.0-0:i386 libpango1.0-0:i386 libx11-6:i386 libcanberra-gtk-module:i386")
    apt_install(root_password,"./peazip_7.8.0.LINUX.x86_64.GTK2.deb")
    execute_as_root(root_password,"sudo rm peazip_7.8.0.LINUX.x86_64.GTK2.deb")

if InstallPeaZip == "2":
    what_is_it("PeaZip[flatpak]")
    update_packege(root_password)
    apt_install(root_password,"flatpak")
    execute_as_root(root_password,"flatpak install flathub io.github.peazip.PeaZip -y")

if InstallVSC == "1":
    # TODO Replace with VScodium
    what_is_it("Visual Studio Code")
    apt_install(root_password,"software-properties-common apt-transport-https wget")
    execute_as_root(root_password,"wget -q https://packages.microsoft.com/keys/microsoft.asc -O- | sudo apt-key add -")
    execute_as_root(root_password,'sudo add-apt-repository "deb [arch=amd64] https://packages.microsoft.com/repos/vscode stable main"')
    update_packege(root_password)
    apt_install(root_password,"code")

if InstallVSC == "1":
    # TODO Replace with VScodium
    what_is_it("Visual Studio Code [flatpak]")
    flatpak(root_password)
    execute_as_root(root_password,"flatpak install flathub com.visualstudio.code -y")

if InstallPyCharm == "1":
    what_is_it("PyCharm")
    # TODO !!!

if InstallPyCharm == "2":
    what_is_it("PyCharm [flatpak]")
    flatpak(root_password)
    execute_as_root(root_password,"flatpak install flathub com.jetbrains.PyCharm-Community -y")

if InstallKate == "1":
    what_is_it("Kate")
    apt_install(root_password,"kate")

if InstallMousePad == "1":
    what_is_it("MousePad")
    apt_install(root_password,"mousepad")

if InstallLibreOffice == "1":
    what_is_it("LibreOffice")
    if not ChooseMethodForDebian:
        execute_as_root(root_password,"sudo add-apt-repository ppa:libreoffice/ppa --yes")
    update_packege(root_password)
    apt_install(root_password,"libreoffice")

if InstallBleachBit == "1":
    what_is_it("Bleach Bit")
    apt_install(root_password,"bleachbit")

if InstallStacer == "1":
    what_is_it("Stacer")
    if ChooseMethodForDebian:
        execute_as_root(root_password,"wget https://sourceforge.net/projects/stacer/files/v1.0.8/stacer_1.0.8_amd64.deb")
        execute_as_root(root_password,"dpkg --install stacer_1.0.8_amd64.deb ")
    else:
        apt_install(root_password,"stacer")

if InstallCheese == "1":
    what_is_it("Cheese")
    apt_install(root_password,"cheese")

if InstallQbitTorrent == "1":
    what_is_it("qBittorrent")
    apt_install(root_password,"qbittorrent")

if InstallSSR == "1":
    what_is_it("Simple Screen Recorder")
    update_packege(root_password)
    apt_install(root_password,"simplescreenrecorder")

if InstallOBS == "1":
    what_is_it("OBS Studio")
    update_packege(root_password)
    apt_install(root_password,"obs-studio")

if InstallSteam == "1":
    what_is_it("Steam")
    apt_install(root_password,"steam")

if InstallSteam == "2":
    what_is_it("Steam [flatpak]")
    flatpak(root_password)
    execute_as_root(root_password,"flatpak install flathub com.valvesoftware.Steam -y")

# TODO REDO
if InstallTeams == "1":
    what_is_it("MS Teams")
    execute_as_root(root_password,"curl https://packages.microsoft.com/keys/microsoft.asc | sudo apt-key add -")
    execute_as_root(root_password, "sudo sh -c 'echo " + '"deb [arch=amd64] https://packages.microsoft.com/repos/ms-teams stable main"' + " > /etc/apt/sources.list.d/teams.list"+"'")
    update_packege(root_password)
    apt_install(root_password,"teams")

if InstallTeams == "2":
    what_is_it("MS Teams [flatpak]")
    flatpak(root_password)
    execute_as_root(root_password,"flatpak install flathub com.microsoft.Teams -y")
# TODO REDO *


if InstallGpp == "1":
    what_is_it("G++")
    execute_as_root(root_password,"sudo apt update --yes")
    execute_as_root(root_password,"sudo apt-get install g++ -y")
    print("\nHint: Use to build $ g++ <YourCode>.cpp -o <NameYouFutureProgram> ")
    print("Hint: Use to run $ ./<NameYouProgram>\n")

if InstallArduinoIDLE == "1":
    what_is_it("Arduino IDLE")
    execute_as_root(root_password,"sudo apt install arduino --yes")

if InstallPython3IDLE == "1":
    what_is_it("Python IDLE")
    execute_as_root(root_password,"sudo apt-get install idle3 --yes")

if InstallGnomeSoftware == "1":
    what_is_it("Gnome Software")
    execute_as_root(root_password,"sudo snap remove gnome-software")
    apt_install(root_password,"gnome-software gnome-software-plugin-flatpak")

if InstallClamAV == "1":
    what_is_it("ClamAV")
    execute_as_root(root_password,"sudo apt-get install clamav --yes")
    execute_as_root(root_password,"sudo apt-get install clamav-daemon --yes")
    execute_as_root(root_password,"sudo apt install clamtk --yes")
    execute_as_root(root_password,"sudo apt-get install libclamunrar6 --yes")

if InstallGnomeDisk == "1":
    what_is_it("Gnome Disk")
    execute_as_root(root_password,"sudo apt-get install gnome-disk-utility --yes")

if InstallDoubleCmd == "1":
    what_is_it("Double commander")
    execute_as_root(root_password,"sudo apt-get install doublecmd-gtk --yes")

if InstallBaobab == "1":
    what_is_it("Baobab Disk Analyzer")
    execute_as_root(root_password,"sudo apt-get install baobab --yes")


if InstallCodeBlocks == "1":
    what_is_it("Code::Blocks")
    apt_install(root_password,"codeblocks")

if InstallCodeBlocks == "2":
    what_is_it("Code::Blocks via flatpak")
    flatpak(root_password)
    execute_as_root(root_password,"flatpak install flathub org.codeblocks.codeblocks")

if InstallGodotEngine == "1":
    flatpak(root_password)
    execute_as_root(root_password,"flatpak install flathub org.godotengine.Godot -y")

if IsFixingDependencies == "1":
    print("\n===================== Updating and fixing dependencies =====================")
    for i in range(3):
        print(str(i)+")")
        execute_as_root(root_password,"sudo apt --fix-broken install --yes")
        execute_as_root(root_password,"sudo apt install -f -y")  #  Updating and fixing dependencies
        execute_as_root(root_password,"sudo apt install dpkg --fix-missing")
        execute_as_root(root_password,"sudo dpkg --configure -a")

if do_clean == "1":
    apt_clean(root_password)

print("\n===================== End =====================")
if EnableTempCaffiene:
    IsDeleteTempCaffeine = input("Is Delete Temp Caffeine? (No = 0/Yes = 1): = ")
    if IsDeleteTempCaffeine == "1":
        execute_as_root(root_password,"sudo apt remove caffeine -y")

isReboot = input("ReBoot? (No = 0/Yes = 1): = ")
if isReboot == "1":
    execute_as_root(root_password,"sudo shutdown -r now")
