#! /usr/bin/python3
# -*- coding: utf-8 -*-
import os
import sys

IsAllowSnap = False
EnableTempCaffiene = False


#sudo dpkg --configure -a

''' === Note ===

To add the PPA, open terminal from the Dash or by pressing Ctrl+Alt+T. When it opens, run command:

sudo add-apt-repository ppa:caffeine-developers/ppa

After that, update package cache and install the indicator by running below two commands one by one:

sudo apt-get update

sudo apt-get install caffeine

Now to run the caffeine indicator from terminal easily open your terminal and run the command:

caffeine

Note that whenever you start a command by first letters then use the tricky double tab key to autocomplete or show all commands starting with those letters.

===

sudo add-apt-repository ppa:nilarimogard/webupd8
sudo apt-get update
sudo apt-get install caffeine-plus       

'''
def DoThis(RootPassword,Command):
    os.system('echo %s|sudo -S %s' % (RootPassword,Command))

def WhatItIs(ProgrammeName):
    print("\n==================== Install " + ProgrammeName + " ====================")

def UpdatePackege(RootPassword):
    print("\n==================== Update ====================")
    os.system('echo %s|sudo -S %s' % (RootPassword, "sudo apt update"))

def UpgradePackege(RootPassword):
    print("\n==================== Upgrade ====================")
    os.system('echo %s|sudo -S %s' % (RootPassword, "sudo apt upgrade --yes"))

def SimpleInstall(RootPassword,ProgrammeName):
    os.system('echo %s|sudo -S %s' % (RootPassword, "sudo apt install " + ProgrammeName + " --yes"))

#def SimpleBackportsInstall(RootPassword,ProgrammeName):
#   os.system('echo %s|sudo -S %s' % (RootPassword, "sudo apt install -t stretch-backports " + ProgrammeName + " --yes"))

def SnapRefresh(RootPassword):
    if IsAllowSnap:
        print("\n==================== Snap Refresh ====================")
        SimpleInstall(RootPassword,"snap")
        SimpleInstall(RootPassword,"snapd")
        os.system('echo %s|sudo -S %s' % (RootPassword, "sudo snap refresh"))
    else:
        print("\nSnap is Detected!\nIsAllowSnap = False")

def FlatPak(RootPassword):
    WhatItIs("FlatPak")
    SimpleInstall(RootPassword,"flatpak")
    if not ChooseMethodForDebian:
        DoThis(RootPassword,"sudo add-apt-repository ppa:alexlarsson/flatpak")
    UpdatePackege(RootPassword)
    DoThis(RootPassword,"flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo")
    #DoThis(RootPassword,"flatpak update") #almost aborted!

def SnapSimpleInstall(RootPassword,ProgrammeName):
    if IsAllowSnap:
        os.system('echo %s|sudo -S %s' % (RootPassword, "sudo snap install " + ProgrammeName))# No "--yes"
    else:
        print("Snap is Detected!\nIsAllowSnap = False")

def FixPlank(RootPassword):
    print("==================== Fix Plank ====================")
    os.system('echo %s|sudo -S %s' % (RootPassword,"gsettings set net.launchpad.plank.dock.settings:/net/launchpad/plank/docks/dock1/ show-dock-item false"))#remove anchor icon in Plank
    print("Done!")

def FixGedit(RootPassword):
    #gsettings set org.gnome.gedit.preferences.encodings candidate-encodings "['UTF-8', 'WINDOWS-1251', 'KOI8-R', 'CURRENT', 'ISO-8859-15', 'UTF-16']"
    print("==================== Fix Gedit ====================")
    os.system('echo %s|sudo -S %s' % (RootPassword,'gsettings set org.gnome.gedit.preferences.encodings candidate-encodings' + '"' + "['UTF-8', 'WINDOWS-1251', 'KOI8-R', 'CURRENT', 'ISO-8859-15', 'UTF-16']" + '"'))
    print("Done!")

def Cleaner(RootPassword):
    print("==================== Cleaning ====================")
    print("> autoremove")
    os.system('echo %s|sudo -S %s' % (RootPassword, "sudo apt autoremove --yes"))
    print("> autoclean")
    os.system('echo %s|sudo -S %s' % (RootPassword, "sudo apt autoclean --yes"))
    print("> clean")
    os.system('echo %s|sudo -S %s' % (RootPassword, "sudo apt clean --yes"))

def Logo():
    print("######################################")
    print("#            AutoInstaller           #")
    print("######################################")
    print("By AlexNottaBen")

def ClearScreen():
    os.system("clear")


#Begin
ClearScreen()
Logo()
RootPassword = input("Input Root Password > ")
ClearScreen()
Logo()

ChooseMethodForDebian = False
ChooseFlatPakMethod = False

IsCleaner = "0"
IsFixingDependencies = "0"
IsUpdate = "0"
IsUpgrade = "0"
IsSnapRefresh = "0"
UpdateMicroCodeIntel = "0"
UpdateMicroCodeAmd64 = "0"
IsFixGedit = "0"
IsFixPlank = "0"
InstallFlatPak = "0"
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
InstallCaffeine = "0"
InstallFileZilla = "0"
InstallCaja = "0"
InstallCajaDrobBox = "0"
InstallTimeShift = "0"
InstallPeaZip = "0"
FlatpakInstallPeaZip = "0"
InstallKdenline = "0"
InstallOpenShot = "0"
InstallAudacity = "0"
InstallGrubCustomizer = "0"
InstallVBOX = "0"
InstallNotepadplusplus = "0"
InstallWine = "0"
InstallPlayOnLinux = "0"
InstallFireFox = "0"
InstallThunderBird = "0"
InstallChromium = "0"
InstallUnGoogledChromium = "0"
InstallEdge = "0"
InstallChrome = "0"
InstallTor = "0"
InstallShotWell = "0"
InstallXnViewMP = "0"
InstallVSC = "0"
InstallSublimeText = "0"
InstallLibreOffice = "0"
InstallBleachBit = "0"
InstallStacer = "0"
InstallCheese = "0"
InstallGparted = "0"
InstallQbitTorrent = "0"
InstallTransmission = "0"
InstallSSR = "0"
InstallOBS = "0"
InstallSteam = "0"
InstallZoom = "0"
InstallViber = "0"
InstallPidgin = "0"
InstallTelegram = "0"
InstallTeams = "0"
InstallSkype = "0"
InstallLutris = "0"
InstallGpp = "0"
InstallArduinoIDLE = "0"
InstallPython3IDLE = "0"
InstallClamAV = "0"
InstallIPTables = "0" #!!!
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
InstallDoubleCmd = "0"
InstallBaobab = "0"
ProfPythonDeveloper = "0"
InstallUnity = "0"

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
print('P2 - All For Unity Developer')

Selected = input("Select > ")

if Selected == "1":
    UpdateMicroCodeIntel = "1"
    InstallFlatPak = "1"
    IsUpdate = "1"
    IsUpgrade = "1"
    IsSnapRefresh = "1"
    IsFixPlank = "1"
    InstallVLC = "1"
    InstallGIMP = "1"
    InstallTimeShift = "1"
    InstallPeaZip = "1"
    InstallVBOX = "1"
    InstallNotepadplusplus = "0"
    InstallWine = "1"
    InstallPlayOnLinux = "1"
    InstallFireFox = "0"
    InstallEdge = "1"
    InstallTor = "0"
    InstallVSC = "0"
    InstallUnGoogledChromium = "1"
    InstallSublimeText = "2"
    InstallLibreOffice = "1"
    InstallBleachBit = "1"
    InstallGparted = "1"
    InstallQbitTorrent = "1"
    InstallSSR = "1"
    InstallSteam = "1"
    InstallZoom = "1"
    InstallTelegram = "2"
    InstallTeams = "1"
    InstallCaffeine = "1"
    InstallGpp = "1"
    InstallArduinoIDLE = "0"
    InstallPython3IDLE = "0"
    IsCleaner = "1"
    IsFixingDependencies = "1"
    InstallShotWell = "1"
    InstallStacer = "0"
    InstallPyCharm = "0"
    InstallCaja = "1" #For Open The Trash by The Plank on Debian
    InstallCodeBlocks = "1"
    InstallKrita = "1"
    InstallKdenline = "1"
    InstallKolourPaint = "1"
    InstallGnomeDisk = "1"
    InstallDoubleCmd = "1"
    InstallBaobab = "1"
    InstallKolourPaint = "1"
    ChooseMethodForDebian = True
    ChooseFlatPakMethod = True

if Selected == "2":
    UpdateMicroCodeIntel = "1"
    InstallFlatPak = "1"
    IsUpdate = "1"
    IsUpgrade = "1"
    IsSnapRefresh = "1"
    IsFixPlank = "1"
    InstallVLC = "1"
    InstallGIMP = "1"
    InstallTimeShift = "1"
    InstallPeaZip = "1"
    InstallVBOX = "1"
    InstallNotepadplusplus = "0"
    InstallWine = "1"
    InstallPlayOnLinux = "1"
    InstallFireFox = "0"
    InstallChromium = "0"
    InstallUnGoogledChromium = "1"
    InstallTor = "1"
    InstallVSC = "0"
    InstallSublimeText = "2"
    InstallLibreOffice = "1"
    InstallBleachBit = "0"
    InstallGparted = "1"
    InstallQbitTorrent = "1"
    InstallSSR = "1"
    InstallSteam = "1"
    InstallTelegram = "2"
    InstallTeams = "0"
    InstallCaffeine = "0"
    IsCleaner = "1"
    IsFixingDependencies = "1"
    InstallShotWell = "1"
    InstallXnViewMP = "0"
    InstallStacer = "0"
    InstallKate = "1"
    InstallGpp = "1"
    InstallPyCharm = "0"
    InstallCaja = "1" #For Open The Trash by The Plank on Debian
    InstallCodeBlocks = "1"
    InstallKrita = "1"
    InstallKdenline = "1"
    InstallKolourPaint = "1"
    InstallGnomeDisk = "1"
    InstallDoubleCmd = "1"
    InstallBaobab = "1"
    InstallKolourPaint = "1"
    ChooseMethodForDebian = False
    ChooseFlatPakMethod = False

if Selected == "3":
    InstallFlatPak = "0"
    IsUpdate = "1"
    IsUpgrade = "1"
    IsSnapRefresh = "1"
    IsFixPlank = "1"
    InstallVLC = "1"
    InstallGIMP = "1"
    InstallPeaZip = "1"
    InstallVBOX = "1"
    InstallFireFox = "1"
    InstallVSC = "1"
    InstallSublimeText = "1"
    InstallLibreOffice = "1"
    InstallBleachBit = "1"
    InstallGparted = "1"
    InstallQbitTorrent = "1"
    InstallSSR = "1"
    InstallZoom = "1"
    InstallTeams = "1"
    IsCleaner = "1"
    IsFixingDependencies = "1"

if Selected == "4":
    InstallFlatPak = "0"
    IsUpdate = "1"
    IsUpgrade = "1"
    IsSnapRefresh = "1"
    InstallSSR = "1"
    InstallSteam = "1"
    InstallWine = "1"
    InstallPlayOnLinux = "1"
    InstallLutris = "1"
    IsCleaner = "1"
    IsFixingDependencies = "1"

if Selected == "5":
    InstallFlatPak = "0"
    IsUpdate = "1"
    IsFixPlank = "1"
    InstallSSR = "1"
    InstallTeams = "1"
    IsCleaner = "1"
    IsFixingDependencies = "1"

if Selected == "6":
    InstallFlatPak = "0"
    IsUpdate = "1"
    IsUpgrade = "1"
    IsSnapRefresh = "1"
    InstallGIMP = "1"
    InstallVLC = "1"
    InstallKdenline = "1"
    IsCleaner = "1"
    IsFixingDependencies = "1"

if Selected == "7":
    InstallFlatPak = "0"
    IsUpdate = "1"
    IsUpgrade = "1"
    IsSnapRefresh = "1"

if Selected == "8":
    InstallFlatPak = "0"
    IsUpdate = "1"
    IsUpgrade = "1"
    IsSnapRefresh = "1"
    IsCleaner = "1"
    IsFixingDependencies = "1"

if Selected == "F":
    UpdateMicroCodeIntel = "1"
    InstallFlatPak = "1"
    IsUpdate = "1"
    IsUpgrade = "1"
    IsSnapRefresh = "1"
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
    IsCleaner = "1"
    IsFixingDependencies = "1"
    InstallXnViewMP = "1"
    InstallCaja = "1" #For Open The Trash by The Plank on Debian
    InstallKrita = "1"
    InstallKdenline = "1"
    InstallGnomeDisk = "1"
    InstallDoubleCmd = "1"
    InstallBaobab = "1"
    InstallKolourPaint = "1"
    InstallStacer = "1"
    ChooseMethodForDebian = False
    ChooseFlatPakMethod = False

if Selected == "Y":
    UpdateMicroCodeIntel = "1"
    InstallFlatPak = "1"
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
    ChooseMethodForDebian = False
    ChooseFlatPakMethod = False

if Selected == "P1":
    UpdatePackege(RootPassword)
    UpgratePackege(RootPassword)
    print("\n===================== Ipython3 and Git =====================")
    SimpleInstall(RootPassword,"git")
    SimpleInstall(RootPassword,"ipython3")
    InstallPyCharm = input("\n\n[Open-Source] PyCharm Community - Community IDE Editor (No = 0/Yes = 1/Yes = 2[Flatpak]): = ")

if Selected == "P2":
    IsUpdate = "1"
    IsUpgrade = "1"
    InstallUnity = "1"

if Selected == "0":
    IsUpdate = "1"
    IsUpgrade = "1"
    IsSnapRefresh = "1"
    print("==================== Set Basic Setting ====================")
    UpdateMicroCodeIntel = input("Update MicroCode For Intel (No = 0/Yes = 1): = ")
    UpdateMicroCodeAmd64 = input("Update MicroCode For Amd64 (No = 0/Yes = 1): = ")
    InstallMediaCodes = input("Install Media Codes (No = 0/Yes = 1): = ")
    IsFixGedit = input("Use this If Cyrillic is not displayed in the Gedit text editor! (No = 0/Yes = 1): = ")
    IsFixPlank = input("Remove anchor icon in Plank (No = 0/Yes = 1): = ")
    print("==================== Install Programs ====================")
    InstallFlatPak = input("[Open-Source] FlatPak - System for collecting self-sufficient packages (No = 0/Yes = 1): = ")
    InstallVLC = input("[Open-Source] VLC - MediaPlayer (No = 0/Yes = 1): = ")
    InstallGIMP = input("[Open-Source] GIMP - Raster Graphic Editor (No = 0/Yes = 1): = ")
    InstallKrita = input("[Open-Source] Krita - Raster Graphic Editor (No = 0/Yes = 1/Yes[FlatPak] = 2): = ")
    InstallMyPaint = input("[Open-Source] MyPaint - Raster Graphic Editor (No = 0/Yes = 1): = ")
    InstallKolourPaint = input("[Open-Source] KolourPaint - Raster Graphic Editor (No = 0/Yes = 1): = ")
    InstallInkScape = input("[Open-Source] InkScape - Vector Graphic Editor (No = 0/Yes = 1): = ")
    Installblender = input("[Open-Source] Blender - 3D Editor (No = 0/Yes = 1): = ")
    InstallSweetHome3D = input("[Open-Source] Sweet Home 3D - 3D Home Editor (No = 0/Yes = 1): = ")
    InstallScratch = input("[Open-Source] Scratch - Game Developer Tools (No = 0/Yes = 1): = ")
    InstallScratch3 = input("[Open-Source] Scratch 3 - Game Developer Tools (No = 0/Yes = 1): = ")
    InstallCaffeine = input("[Open-Source] Caffeine - Deactive sleep mode (No = 0/Yes = 1): = ")
    InstallFileZilla = input("[Open-Source] FileZilla - FTP Client (No = 0/Yes = 1): = ")
    InstallCaja = input("[Open-Source] Caja - The File Manager of MATE (No = 0/Yes = 1): = ")
    InstallCajaDrobBox = input("[Addons] Caja DrobBox - Alternative to One Drive (No = 0/Yes = 1): = ")
    InstallTimeShift = input("[Open-Source] TimeShift - Alternative to Time Machine (No = 0/Yes = 1): = ")
    InstallPeaZip = input("[Open-Source] PeaZip - Alternative to WinRar (No = 0/Yes = 1/Yes[FlatPak] = 2): = ")
    #FlatpakInstallPeaZip = input("[Open-Source] PeaZip(FlatPak) - Alternative to WinRar (No = 0/Yes = 1): = ")   
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
    InstallFireFox = input("[Open-Source] FireFox - Open Web-broweser(No = 0/Yes = 1): = ")
    InstallChromium = input("[Open-Source] Chromium - Open Web-broweser(No = 0/Yes = 1): = ")
    InstallUnGoogledChromium = input("[Open-Source] Ungoogled Chromium - Open Web-broweser(No = 0/Yes = 1): = ")
    InstallEdge = input("[Proprietary Software] Edge dev - Web-broweser by Microsoft (No = 0/Yes = 1): = ")
    InstallChrome = input("[Proprietary Freeware] Google Chrome - Web-broweser by Google (No = 0/Yes = 1): = ")
    InstallTor = input("[Open-Source] Tor Browser - Web-broweser by Tor Project (No = 0/Yes = 1): = ")
    InstallShotWell = input("[Open-Source] ShotWell - Image Viewer, Alternative to XnView MP (No = 0/Yes = 1): = ")
    InstallXnViewMP = input("[Proprietary Freeware] XnView MP - Image Viewer (No = 0/Yes = 1): = ")
    InstallKate = input("[Open-Source] Kate - KDE Text Editor, Alternative to Sublime Text(No = 0/Yes = 1): = ")
    InstallMousePad = input("[Open-Source] MousePad - XFCE Text Editor (No = 0/Yes = 1): = ")
    InstallPyCharm = input("[Open-Source] PyCharm Community - Community IDE Editor (No = 0/Yes = 1/Yes = 2[Flatpak]): = ")   
    InstallSublimeText  = input("[Proprietary] Sublime Text - Text Editor (No = 0/Yes = 1): = ")
    InstallVSC = input("[Proprietary] Visual Studio Code - Development Environment (No = 0/Yes = 1): = ")
    InstallLibreOffice = input("[Open-Source] Libre Office - OpenSource Office (No = 0/Yes = 1): = ")
    InstallBleachBit = input("[Open-Source] BleachBit - Alternative to Piriform CCleaner (No = 0/Yes = 1): = ")
    InstallStacer = input("[Open-Source] Stacer - Alternative to Piriform CCleaner (No = 0/Yes = 1): = ")
    InstallCheese = input("[Open-Source] Cheese - Camera (No = 0/Yes = 1): = ")
    InstallGparted = input("[Open-Source] Gparted - Disk Utility (No = 0/Yes = 1): = ")
    InstallQbitTorrent = input("[Open-Source] Qbittorrent - Torrent Client  (No = 0/Yes = 1): = ")
    InstallTransmission = input("[Open-Source] Transmission - Torrent Client  (No = 0/Yes = 1): = ")
    InstallSSR = input("[Open-Source] Simple Screen Recorder - Screen Recorder  (No = 0/Yes = 1): = ")
    InstallOBS = input("[Open-Source] OBS Studio - Screen Recorder  (No = 0/Yes = 1): = ")
    InstallSteam = input("[Proprietary Freeware] Steam - Center For Games and Software (No = 0/Yes = 1): = ")
    InstallZoom = input("[Proprietary Freemium] Zoom - For Vidio Rings (No = 0/Yes = 1): = ")
    InstallViber = input("[Proprietary Shareware] Viber - For Chating (No = 0/Yes = 1): = ")
    InstallPidgin = input("[Open-Source] Pidgin - For Chating (No = 0/Yes = 1): = ")
    InstallTelegram = input("[Open-Source Client/Proprietary Server] Telegram - For Chating (No = 0/Yes[Snap] = 1/Yes[FlatPak] = 2): = ")
    InstallTeams = input("[Proprietary Software] Microsoft Teams - For Study (No = 0/Yes = 1): = ")
    InstallDiscord = input("[Proprietary Software] Discord - Modern Apps For Chating, Vidio Rings (No = 0/Yes = 1): = ")
    InstallSkype = input("[Proprietary Software] Microsoft Skype - For Vidio Rings (No = 0/Yes = 1): = ")
    InstallGpp = input("[Maybe,Open-Source] G++ - C++ Compiler (No = 0/Yes = 1): = ")
    InstallArduinoIDLE = input("[Open-Source] Arduino IDLE - IDLE for Arduino (No = 0/Yes = 1): = ")
    InstallPython3IDLE = input("[Maybe,Open-Source] Python3 IDLE - IDLE for Python (No = 0/Yes = 1): = ")
    InstallClamAV = input("[Open-Source] ClamAV - AntiVirus Program(No = 0/Yes = 1): = ")
    InstallGodotEngine = input("[Open-Source] Godot Engine - Game Engine(No = 0/Yes = 1[Flatpak]): = ")
    InstallUnity = input("[Proprietary Software] Unity Engine - Game Engine(No = 0/Yes = 1): = ")
    InstallCodeBlocks = input("[Open-Source] Code::Blocks - Alternative to Dev-C++ (No = 0/Yes = 1/Yes[FlatPak] = 2): = ")
    InstallGnomeDisk = input("[Open-Source] Gnome Disk - Disk Utility (No = 0/Yes = 1/Yes[FlatPak]): = ")
    InstallDoubleCmd = input("[Open-Source] Double Commander - Alternative to Total Commander (No = 0/Yes = 1): = ")
    InstallBaobab = input("[Open-Source] Baobab - Disk Analyzer (No = 0/Yes = 1): = ")

print("\n==================== Start ====================\n")

if EnableTempCaffiene:
    #Temp Caffeine
    WhatItIs("Temp Caffeine")
    if not ChooseMethodForDebian:
        DoThis(RootPassword,"sudo add-apt-repository ppa:caffeine-developers/ppa")
    UpdatePackege(RootPassword)
    SimpleInstall(RootPassword,"caffeine")
    #os.system("caffeine")
    input("Active Caffeine and press any key! ")

#Update
if IsUpdate == "1":
	UpdatePackege(RootPassword)
if IsUpgrade == "1":
	UpgradePackege(RootPassword)
if IsSnapRefresh == "1":
	SnapRefresh(RootPassword)

if UpdateMicroCodeIntel == "1":
    WhatItIs("MicroCode For Intel")
    SimpleInstall(RootPassword,"--reinstall intel-microcode")

if UpdateMicroCodeAmd64 == "1":
    WhatItIs("MicroCode For Amd64")
    SimpleInstall(RootPassword,"--reinstall amd64-microcode")

if InstallMediaCodes == "1":
    WhatItIs("Media Codes")
    SimpleInstall(RootPassword,"ubuntu-restricted-extras")

#Fixes
if IsFixGedit == "1":
    FixGedit(RootPassword)

if IsFixPlank == "1":
    FixPlank(RootPassword)

#Installs

if InstallFlatPak == "1":
    FlatPak(RootPassword)

if InstallVLC == "1":
    WhatItIs("VLC")
    SimpleInstall(RootPassword,"vlc")
   
if InstallVLC == "1":
    WhatItIs("MPV")
    SimpleInstall(RootPassword,"mpv")

    '''
	To install the latest VLC media player you might want to consider the VLC installation 
	from a 3rd-party PPA repository. To do so first step is to include VLC PPA repository:

	$ sudo add-apt-repository ppa:videolan/master-daily

	Next, install the actual VLC player:

	$ sudo apt install vlc

    '''

if InstallGIMP == "1":
    WhatItIs("GIMP")
    SimpleInstall(RootPassword,"gimp")

if InstallKrita == "1":
    WhatItIs("Krita")
    SimpleInstall(RootPassword,"krita")

if InstallKrita == "2":
    WhatItIs("Krita [FlatPak]")
    DoThis(RootPassword,"flatpak install flathub org.kde.krita -y")

if InstallMyPaint == "1":
    WhatItIs("MyPaint")
    SimpleInstall(RootPassword,"mypaint-data")
    SimpleInstall(RootPassword,"mypaint")

if InstallMyPaint == "1":
    WhatItIs("KolourPaint")
    SimpleInstall(RootPassword,"kolourpaint")

if InstallInkScape == "1":
    WhatItIs("InkScape")
    SimpleInstall(RootPassword,"inkscape")

if Installblender == "1":
    WhatItIs("Blender")
    SimpleInstall(RootPassword,"blender")

if InstallSweetHome3D == "1":
    WhatItIs("SweetHome3D")
    SimpleInstall(RootPassword,"sweethome3d")

if InstallScratch == "1":
    WhatItIs("Scratch")
    SimpleInstall(RootPassword,"scratch")

if InstallScratch3 == "1":
    WhatItIs("Scratch 3")
    FlatPak(RootPassword)
    DoThis(RootPassword,"flatpak install flathub edu.mit.Scratch -y")

if InstallFileZilla == "1":
    WhatItIs("FileZilla")
    SimpleInstall(RootPassword,"filezilla")

if InstallCaja == "1":
    WhatItIs("Caja")
    SimpleInstall(RootPassword,"caja")

if InstallCajaDrobBox == "1":
    WhatItIs("Caja - DrobBox")
    SimpleInstall(RootPassword,"caja-dropbox")

if InstallKdenline == "1":
    WhatItIs("Kdenline")
    if not ChooseMethodForDebian:
        DoThis(RootPassword,"sudo add-apt-repository ppa:kdenlive/kdenlive-stable --yes")
    UpdatePackege(RootPassword)
    SimpleInstall(RootPassword,"kdenlive")

if InstallOpenShot == "1":
    WhatItIs("OpenShot")
    SimpleInstall(RootPassword,"openshot")

if InstallPitivi == "1":
    WhatItIs("Pitivi")
    SimpleInstall(RootPassword,"pitivi")

if InstallAudacity == "1":
    WhatItIs("Audacity")
    SimpleInstall(RootPassword,"audacity")

if InstallGrubCustomizer == "1":
    WhatItIs("GrubCustomizer")
    SimpleInstall(RootPassword,"grub-customizer")

if InstallVBOX == "1":
    WhatItIs("Virtualbox")
    if ChooseMethodForDebian:
        UpdatePackege(RootPassword)
        DoThis(RootPassword,"wget -q https://www.virtualbox.org/download/oracle_vbox_2016.asc -O- | sudo apt-key add -")
        DoThis(RootPassword,'echo "deb [arch=amd64] http://download.virtualbox.org/virtualbox/debian bionic contrib" | sudo tee /etc/apt/sources.list.d/virtualbox.list')
        UpdatePackege(RootPassword)
        SimpleInstall(RootPassword,"virtualbox-6.1")
        '''
        virtualbox-6.1 (6.1.24-145767~Ubuntu~bionic)
        virtualbox-6.0 (6.0.24-139119~Ubuntu~bionic)
        virtualbox-5.2 (5.2.44-139111~Ubuntu~bionic)
        virtualbox-5.1 (5.1.38-122592~Ubuntu~bionic)
        '''
    else:
        SimpleInstall(RootPassword,"virtualbox")

if InstallNotepadplusplus == "1":
    WhatItIs("Notepad++") #FlatPak Package does not exists! /!\
    UpdatePackege(RootPassword)
    if IsAllowSnap:
        SimpleInstall(RootPassword,"snapd")
        SnapSimpleInstall(RootPassword,"notepad-plus-plus")
    else:
        print("Snap is Detected!\nIsAllowSnap = False")

if InstallNotepadqq == "1":
    WhatItIs("Notepadqq")
    SimpleInstall(RootPassword,"notepadqq")

if InstallPidgin == "1":
    WhatItIs("Pidgin")
    SimpleInstall(RootPassword,"pidgin")

if InstallTelegram == "2":
    WhatItIs("Telegram [FlatPak]")
    FlatPak(RootPassword)
    DoThis(RootPassword,"flatpak install flathub org.telegram.desktop -y")

if InstallTelegram == "1":
    WhatItIs("Telegram [Snap]")
    if IsAllowSnap:
        DoThis(RootPassword,"snap find | grep telegram")
        SnapSimpleInstall(RootPassword,"telegram-desktop")
    else:
        print("Snap is Detected!\nIsAllowSnap = False")

if InstallViber == "1":
    WhatItIs("Viber")
    DoThis(RootPassword,"wget https://download.cdn.viber.com/cdn/desktop/Linux/viber.deb")
    SimpleInstall(RootPassword,"./viber.deb")

if InstallPidgin == "1":
    WhatItIs("Pidgin")
    SimpleInstall(RootPassword,"pidgin")

if InstallWine == "1":
    WhatItIs("Wine")
    SimpleInstall(RootPassword,"wine")

if InstallGparted == "1":
    WhatItIs("Gparted")
    SimpleInstall(RootPassword,"gparted")

if InstallPlayOnLinux == "1":
    WhatItIs("PlayOnLinux") #FlatPak Package does not exists! /!\
    if ChooseMethodForDebian:
        DoThis(RootPassword,"sudo dpkg --add-architecture i386")
        SimpleInstall(RootPassword,"netcat")
        DoThis(RootPassword,'wget -q "http://deb.playonlinux.com/public.gpg" -O- | apt-key add -')
        DoThis(RootPassword,"wget http://deb.playonlinux.com/playonlinux_wheezy.list -O /etc/apt/sources.list.d/playonlinux.list")
        UpdatePackege(RootPassword)
        SimpleInstall(RootPassword,"playonlinux")
        DoThis(RootPassword,"sudo apt-get update && sudo apt-get upgrade && sudo apt-get dist-upgrade")
        SimpleInstall(RootPassword,"multiarch-support libgl1-mesa-glx:i386")
    else:
        SimpleInstall(RootPassword,"playonlinux")
        SimpleInstall(RootPassword,"winbind")
        SimpleInstall(RootPassword,"winetricks")

if InstallLutris == "1":
    WhatItIs("Lutris") #FlatPak Package does not exists! /!\
    DoThis(RootPassword,"sudo add-apt-repository ppa:lutris-team/lutris --yes")
    UpdatePackege(RootPassword)
    SimpleInstall(RootPassword,"lutris")

if InstallDiscord == "1":
    WhatItIs("Discord")
    DoThis(RootPassword,"wget https://dl.discordapp.net/apps/linux/0.0.18/discord-0.0.18.deb")
    SimpleInstall(RootPassword,"./discord-0.0.18.deb")
    DoThis(RootPassword,"sudo rm discord-0.0.18.deb")

if InstallSkype == "1":
    WhatItIs("MS Skype")
    DoThis(RootPassword,"wget https://go.skype.com/skypeforlinux-64.deb")
    SimpleInstall(RootPassword,"./skypeforlinux-64.deb")
    DoThis(RootPassword,"sudo rm ./skypeforlinux-64.deb --yes")

if InstallThunderBird == "1":
    WhatItIs("ThunderBird")
    SimpleInstall(RootPassword,"thunderbird")

if InstallFireFox == "1":
    WhatItIs("FireFox")
    if ChooseMethodForDebian:
        SimpleInstall(RootPassword,"firefox-esr")
    else:
        SimpleInstall(RootPassword,"firefox")

if InstallChromium == "1":
    WhatItIs("Chromium")  #ungoogled-chromium need flatpak 1.8.2 /!\
    SimpleInstall(RootPassword,"chromium-browser")

if InstallChromium == "2":
    WhatItIs("Chromium [FlatPak]")  #ungoogled-chromium need flatpak 1.8.2 /!\
    FlatPak(RootPassword)
    DoThis(RootPassword,"flatpak install flathub org.chromium.Chromium -y")

if InstallUnGoogledChromium == "1":
    WhatItIs("Ungoogled Chromium")  #ungoogled-chromium need flatpak 1.8.2 /!\
    FlatPak(RootPassword)
    DoThis(RootPassword,"flatpak install flathub com.github.Eloston.UngoogledChromium -y")

if InstallEdge == "1":
    WhatItIs("MS Edge") #FlatPak Package does not exists! /!\
    DoThis(RootPassword,"curl https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > microsoft.gpg")
    DoThis(RootPassword,"sudo install -o root -g root -m 644 microsoft.gpg /etc/apt/trusted.gpg.d/")
    DoThis(RootPassword," sudo sh -c 'echo " + '"deb [arch=amd64] https://packages.microsoft.com/repos/edge stable main"' + " > /etc/apt/sources.list.d/microsoft-edge-dev.list'")
    #sudo sh -c 'echo "deb [arch=amd64] https://packages.microsoft.com/repos/edge stable main" > /etc/apt/sources.list.d/microsoft-edge-dev.list'
    DoThis(RootPassword,"sudo rm microsoft.gpg")
    UpdatePackege(RootPassword)
    SimpleInstall(RootPassword,"microsoft-edge-dev")

if InstallChrome == "1":
    WhatItIs("Google Chrome") #FlatPak Package does not exists! /!\
    DoThis(RootPassword,"wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb") 
    DoThis(RootPassword,"sudo dpkg -i google-chrome-stable_current_amd64.deb")

if InstallTor == "1":
    WhatItIs("Tor Browser")
    # '''letterboxing'''
    SimpleInstall(RootPassword,"torbrowser-launcher")

if InstallTor == "2":
    WhatItIs("Tor Browser [FlatPak]")
    # '''letterboxing'''
    FlatPak(RootPassword)
    DoThis(RootPassword,"flatpak install flathub com.github.micahflee.torbrowser-launcher -y") 
    
if InstallShotWell == "1":
    WhatItIs("ShotWell")
    SimpleInstall(RootPassword,"shotwell")
    
if InstallXnViewMP == "1":
    WhatItIs("XnView MP")
    DoThis(RootPassword,"wget https://download.xnview.com/XnViewMP-linux-x64.deb")
    DoThis(RootPassword,"sudo dpkg -i XnViewMP-linux-x64.deb")

if InstallTimeShift == "1":
    WhatItIs("TimeShift")
    if not ChooseMethodForDebian:
        DoThis(RootPassword,'sudo apt-add-repository -y ppa:teejee2008/ppa')
    UpdatePackege(RootPassword)
    SimpleInstall(RootPassword,"timeshift")

if InstallPeaZip == "1":
    WhatItIs("PeaZip")
    DoThis(RootPassword,"wget https://github.com/peazip/PeaZip/releases/download/7.8.0/peazip_7.8.0.LINUX.x86_64.GTK2.deb")
    SimpleInstall(RootPassword,"gdebi-core")
    SimpleInstall(RootPassword,"libatk1.0-0:i386 libc6:i386 libcairo2:i386 libgdk-pixbuf2.0-0:i386 libglib2.0-0:i386 libgtk2.0-0:i386 libpango1.0-0:i386 libx11-6:i386 libcanberra-gtk-module:i386")
    SimpleInstall(RootPassword,"./peazip_7.8.0.LINUX.x86_64.GTK2.deb")
    DoThis(RootPassword,"sudo rm peazip_7.8.0.LINUX.x86_64.GTK2.deb")
	
if InstallPeaZip == "2":
    WhatItIs("PeaZip[FlatPak]")
    DoThis(RootPassword,"sudo add-apt-repository ppa:alexlarsson/flatpak")
    UpdatePackege(RootPassword)
    SimpleInstall(RootPassword,"flatpak")
    DoThis(RootPassword,"flatpak install flathub io.github.peazip.PeaZip -y")

if InstallVSC == "1":
    WhatItIs("Visual Studio Code")
    SimpleInstall(RootPassword,"software-properties-common apt-transport-https wget")
    DoThis(RootPassword,"wget -q https://packages.microsoft.com/keys/microsoft.asc -O- | sudo apt-key add -")
    DoThis(RootPassword,'sudo add-apt-repository "deb [arch=amd64] https://packages.microsoft.com/repos/vscode stable main"')
    UpdatePackege(RootPassword)
    SimpleInstall(RootPassword,"code")

if InstallVSC == "1":
    WhatItIs("Visual Studio Code [FlatPak]")
    FlatPak(RootPassword)
    DoThis(RootPassword,"flatpak install flathub com.visualstudio.code -y")

if InstallPyCharm == "1":
    WhatItIs("PyCharm")
    SnapSimpleInstall(RootPassword,"pycharm-community --classic")

if InstallPyCharm == "2":
    WhatItIs("PyCharm [FlatPak]")
    FlatPak(RootPassword)
    DoThis(RootPassword,"flatpak install flathub com.jetbrains.PyCharm-Community -y")

if InstallKate == "1":
    WhatItIs("Kate")
    SimpleInstall(RootPassword,"kate")

if InstallMousePad  == "1":
    WhatItIs("MousePad")
    SimpleInstall(RootPassword,"mousepad")

if InstallSublimeText == "1":
    WhatItIs("Sublime Text [Snap]")
    DoThis(RootPassword,"wget -qO - https://download.sublimetext.com/sublimehq-pub.gpg | sudo apt-key add -")
    DoThis(RootPassword,'sudo apt-add-repository "deb https://download.sublimetext.com/ apt/stable/')
    SnapSimpleInstall(RootPassword,"sublime-text --classic")
    DoThis(RootPassword,"sudo apt install libgtk2.0-0")

if InstallSublimeText == "2":
    WhatItIs("Sublime Text [Flatpak]")
    FlatPak(RootPassword)
    DoThis(RootPassword,"flatpak install flathub com.sublimetext.three -y")

if InstallLibreOffice == "1":
    WhatItIs("LibreOffice")
    if not ChooseMethodForDebian:
        DoThis(RootPassword,"sudo add-apt-repository ppa:libreoffice/ppa --yes")
    UpdatePackege(RootPassword)
    #DoThis(RootPassword,"sudo apt-get install libreoffice --yes"))
    SimpleInstall(RootPassword,"libreoffice")

if InstallBleachBit == "1":
    WhatItIs("Bleach Bit")
    SimpleInstall(RootPassword,"bleachbit")

if InstallStacer == "1":
    WhatItIs("Stacer")
    if ChooseMethodForDebian:
        DoThis(RootPassword,"wget https://sourceforge.net/projects/stacer/files/v1.0.8/stacer_1.0.8_amd64.deb")
        DoThis(RootPassword,"dpkg --install stacer_1.0.8_amd64.deb ")
    else:
        SimpleInstall(RootPassword,"stacer")

if InstallCheese == "1":
    WhatItIs("Cheese")
    SimpleInstall(RootPassword,"cheese")

if InstallQbitTorrent == "1":
    WhatItIs("qBittorrent")
    SimpleInstall(RootPassword,"qbittorrent")

if InstallTransmission == "1":
    WhatItIs("Transmission")
    SimpleInstall(RootPassword,"transmission")

if InstallSSR == "1":
    WhatItIs("Simple Screen Recorder")
    if not ChooseMethodForDebian:
        DoThis(RootPassword,"sudo add-apt-repository ppa:maarten-baert/simplescreenrecorder --yes")
    UpdatePackege(RootPassword)
    SimpleInstall(RootPassword,"simplescreenrecorder")

if InstallOBS == "1":
    WhatItIs("OBS Studio")
    UpdatePackege(RootPassword)
    SimpleInstall(RootPassword,"obs-studio")

if InstallZoom == "1":
    WhatItIs("Zoom")
    DoThis(RootPassword,"wget https://zoom.us/client/latest/zoom_amd64.deb")
    SimpleInstall(RootPassword,"./zoom_amd64.deb")

if InstallSteam == "1":
    WhatItIs("Steam")
    SimpleInstall(RootPassword,"steam")
    # For Debian
    # deb http://deb.debian.org/debian/ buster main contrib non-free 
    # dpkg --add-architecture i386
    # Update & Steam

if InstallSteam == "2":
    WhatItIs("Steam [FlatPak]")
    FlatPak(RootPassword)
    DoThis(RootPassword,"flatpak install flathub com.valvesoftware.Steam -y")

if InstallTeams == "1":
    WhatItIs("MS Teams")
    DoThis(RootPassword,"curl https://packages.microsoft.com/keys/microsoft.asc | sudo apt-key add -")
    #sudo sh -c 'echo "deb [arch=amd64] https://packages.microsoft.com/repos/ms-teams stable main" > /etc/apt/sources.list.d/teams.list'
    DoThis(RootPassword, "sudo sh -c 'echo " + '"deb [arch=amd64] https://packages.microsoft.com/repos/ms-teams stable main"' + " > /etc/apt/sources.list.d/teams.list"+"'")
    UpdatePackege(RootPassword)
    SimpleInstall(RootPassword,"teams")

if InstallTeams == "2":
    WhatItIs("MS Teams [FlatPak]")
    FlatPak(RootPassword)
    DoThis(RootPassword,"flatpak install flathub com.microsoft.Teams -y")

if InstallGpp == "1":
    WhatItIs("G++")
    DoThis(RootPassword,"sudo apt update --yes")
    DoThis(RootPassword,"sudo apt-get install g++ -y")
    #=================================================
    print("\nHint: Use to build $ g++ <YourCode>.cpp -o <NameYouFutureProgram> ")
    print("Hint: Use to run $ ./<NameYouProgram>\n")

if InstallArduinoIDLE == "1":
    WhatItIs("Arduino IDLE")
    DoThis(RootPassword,"sudo apt install arduino --yes")

if InstallPython3IDLE == "1":
    WhatItIs("Python IDLE")
    DoThis(RootPassword,"sudo apt-get install idle3 --yes")

if InstallUnity == "1":
    WhatItIs("Unity Hub")
    DoThis(RootPassword,"sudo sh -c 'echo \"deb https://hub.unity3d.com/linux/repos/deb stable main\" > /etc/apt/sources.list.d/unityhub.list'")
    DoThis(RootPassword,"wget -qO - https://hub.unity3d.com/linux/keys/public | sudo apt-key add -")
    UpdatePackege(RootPassword)
    DoThis(RootPassword,"sudo apt-get install unityhub --yes")

if InstallClamAV == "1":
    WhatItIs("ClamAV")
    DoThis(RootPassword,"sudo apt-get install clamav --yes")
    DoThis(RootPassword,"sudo apt-get install clamav-daemon --yes")
    DoThis(RootPassword,"sudo apt install clamtk --yes")
    DoThis(RootPassword,"sudo apt-get install libclamunrar6 --yes")

if InstallGnomeDisk == "1":
    WhatItIs("Gnome Disk")
    DoThis(RootPassword,"sudo apt-get install gnome-disk-utility --yes")

if InstallDoubleCmd == "1":
    WhatItIs("Double Commander")
    DoThis(RootPassword,"sudo apt-get install doublecmd-gtk --yes")

if InstallBaobab == "1":
    WhatItIs("Baobab Disk Analyzer")
    DoThis(RootPassword,"sudo apt-get install baobab --yes")


if InstallCodeBlocks == "1":
    WhatItIs("Code::Blocks")
    SimpleInstall(RootPassword,"codeblocks")

if InstallCodeBlocks == "2":
    WhatItIs("Code::Blocks via Flatpak")
    FlatPak(RootPassword)
    DoThis(RootPassword,"flatpak install flathub org.codeblocks.codeblocks")

if InstallGodotEngine == "1":
    FlatPak(RootPassword)
    DoThis(RootPassword,"flatpak install flathub org.godotengine.Godot -y")

if IsFixingDependencies == "1":
    print("\n===================== Updating and fixing dependencies =====================")
    for i in range(3):
        print(str(i)+")")
        DoThis(RootPassword,"sudo apt --fix-broken install --yes")
        DoThis(RootPassword,"sudo apt install -f -y") # Updating and fixing dependencies
        DoThis(RootPassword,"sudo apt install dpkg --fix-missing")
        DoThis(RootPassword,"sudo dpkg --configure -a")
    
if IsCleaner == "1":
    Cleaner(RootPassword)

print("\n===================== End =====================")
if EnableTempCaffiene:
    IsDeleteTempCaffeine = input("Is Delete Temp Caffeine? (No = 0/Yes = 1): = ")
    if IsDeleteTempCaffeine == "1":
        DoThis(RootPassword,"sudo apt remove caffeine -y")

isReboot = input("ReBoot? (No = 0/Yes = 1): = ")
if isReboot == "1":
    DoThis(RootPassword,"sudo shutdown -r now")
