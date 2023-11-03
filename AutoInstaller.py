#! /usr/bin/python3
# -*- coding: utf-8 -*-

from os import system as execute
from getpass import getpass as input_password


def execute_as_root(root_password="live", command="echo"):
    execute("echo %s|sudo -S %s" % (root_password, command))


def what_is_it(program_name="vim"):
    print("\n==================== Install " + program_name + " ====================")


def update_packege(root_password="live"):
    print("\n==================== Update ====================")
    execute("echo %s|sudo -S %s" % (root_password, "sudo apt update"))


def upgrade_packeges(root_password="live"):
    print("\n==================== Upgrade ====================")
    execute("echo %s|sudo -S %s" % (root_password, "sudo apt upgrade --yes"))


def apt_install(root_password="live", program_name="vim"):
    execute(
        "echo %s|sudo -S %s"
        % (root_password, "sudo apt install " + program_name + " --yes")
    )


def flatpak_install(program_domain="org.example.Example"):
    execute("flatpak install flathub " + program_domain + " -y")


def flatpak(root_password="live"):
    what_is_it("flatpak")
    apt_install(root_password, "flatpak")
    update_packege(root_password)
    execute_as_root(
        root_password,
        "flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo",
    )


def fix_plank(root_password):
    """Remove anchor icon in Plank"""
    print("==================== Fix Plank ====================")
    execute(
        "echo %s|sudo -S %s"
        % (
            root_password,
            "gsettings set net.launchpad.plank.dock.settings:/net/launchpad/plank/docks/dock1/ show-dock-item false",
        )
    )
    print("Done!")


def fix_gedit(root_password):
    print("==================== Fix Gedit ====================")
    execute(
        "echo %s|sudo -S %s"
        % (
            root_password,
            "gsettings set org.gnome.gedit.preferences.encodings candidate-encodings"
            + '"'
            + "['UTF-8', 'WINDOWS-1251', 'KOI8-R', 'CURRENT', 'ISO-8859-15', 'UTF-16']"
            + '"',
        )
    )
    print("Done!")


def apt_clean(root_password="live"):
    print("==================== Cleaning ====================")
    print("> autoremove")
    execute("echo %s|sudo -S %s" % (root_password, "sudo apt autoremove --yes"))
    print("> autoclean")
    execute("echo %s|sudo -S %s" % (root_password, "sudo apt autoclean --yes"))
    print("> clean")
    execute("echo %s|sudo -S %s" % (root_password, "sudo apt clean --yes"))


def logo():
    print("######################################")
    print("#            AutoInstaller           #")
    print("######################################")
    print("By AlexNottaBen")


def clear():
    execute("clear")


# Begin
clear()
logo()
root_password = input_password("Input Root Password > ")
if not root_password:
    root_password = "live"
clear()
logo()

choose_method_for_Debian = False

do_clean = "0"
is_fixing_dependencies = "0"
is_update = "0"
is_upgrade = "0"
update_intel_microcodes = "0"
update_amd64_microcodes = "0"
is_fix_gedit = "0"
is_fix_plank = "0"
install_flatpak = "0"
install_VLC = "0"
install_MPV = "0"
install_GIMP = "0"
install_Krita = "0"
install_MyPaint = "0"
install_InkScape = "0"
install_blender = "0"
install_SweetHome3D = "0"
install_Scratch = "0"
install_Scratch3 = "0"
install_TurboWarp = "0"
install_FileZilla = "0"
install_Caja = "0"
install_TimeShift = "0"
install_PeaZip = "0"
install_Kdenline = "0"
install_OpenShot = "0"
install_Audacity = "0"
install_GrubCustomizer = "0"
install_VBOX = "0"
install_Notepadqq = "0"
install_Wine = "0"
install_PlayOnLinux = "0"
install_FireFox = "0"
install_LibreWolf = "0"
install_ThunderBird = "0"
install_Chromium = "0"
install_UnGoogledChromium = "0"
install_Tor = "0"
install_ShotWell = "0"
install_VSC = "0"
install_LibreOffice = "0"
install_BleachBit = "0"
install_Stacer = "0"
install_Cheese = "0"
install_Gparted = "0"
install_QbitTorrent = "0"
install_SSR = "0"
install_OBS = "0"
install_Steam = "0"
install_Pidgin = "0"
install_Telegram = "0"
install_Teams = "0"
install_Lutris = "0"
install_Gpp = "0"
install_ArduinoIDLE = "0"
install_Python3IDLE = "0"
install_ClamAV = "0"
install_IPTables = "0"
install_UFW = "0"
install_Pitivi = "0"
install_MousePad = "0"
install_Kate = "0"
install_PyCharm = "0"
install_GodotEngine = "0"
install_CodeBlocks = "0"
install_MediaCodes = "0"
install_KolourPaint = "0"
install_DoubleCmd = "0"
install_GnomeDisk = "0"
install_Baobab = "0"
install_Blender = "0"
install_GnomeSoftware = "0"
install_FlashPlayer = "0"
install_MSFonts = "0"
install_OnlyOffice = "0"
install_Synaptic = "0"

print("0 - Custom")
print("1 - Default (For Debian and Debian-based OS)")
print("2 - Default (For Ubuntu and Ubuntu-based OS)")
print("3 - Education")
print("4 - Entertaiments")
print('5 - "Fast" MS Teams')
print("6 - Content Creation")
print("7 - Only Updating")
print("8 - Only Basic Fixing and Cleaning")
print("P1 - All For Python Developer")
print("P2 - All For Godot Developer")

Selected = input("Select > ")

if Selected == "1" or Selected == "2":
    update_amd64_microcodes = "1"
    install_MediaCodes = "1"
    install_flatpak = "1"
    is_update = "1"
    is_upgrade = "1"
    is_fix_plank = "1"
    install_VLC = "2"
    install_MPV = "1"
    install_GIMP = "1"
    install_PeaZip = "1"
    install_VBOX = "1"
    install_Wine = "1"
    install_LibreWolf = "1"
    install_Tor = "1"
    install_VSC = "1"
    install_UnGoogledChromium = "1"
    install_LibreOffice = "1"
    install_Gparted = "1"
    install_QbitTorrent = "1"
    install_SSR = "1"
    install_Steam = "1"
    install_Telegram = "2"
    install_Teams = "1"
    install_Gpp = "1"
    install_ArduinoIDLE = "0"
    install_Python3IDLE = "0"
    do_clean = "1"
    is_fixing_dependencies = "1"
    install_ShotWell = "1"
    install_Stacer = "1"
    install_CodeBlocks = "1"
    install_Kdenline = "1"
    install_KolourPaint = "1"
    install_GnomeDisk = "1"
    install_DoubleCmd = "1"
    install_Baobab = "1"
    install_GnomeSoftware = "1"
    install_FlashPlayer = "1"
    install_MSFonts = "1"
    install_OnlyOffice = "1"
    install_Synaptic = "1"
    choose_method_for_Debian = True if Selected == "1" else False

if Selected == "3":
    install_flatpak = "0"
    is_update = "1"
    is_upgrade = "1"
    is_fix_plank = "1"
    install_VLC = "1"
    install_GIMP = "1"
    install_PeaZip = "1"
    install_VBOX = "1"
    install_FireFox = "1"
    install_VSC = "1"
    install_LibreOffice = "1"
    install_BleachBit = "1"
    install_Gparted = "1"
    install_QbitTorrent = "1"
    install_SSR = "1"
    install_Teams = "1"
    install_GnomeSoftware = "1"
    do_clean = "1"
    is_fixing_dependencies = "1"

if Selected == "4":
    install_flatpak = "0"
    is_update = "1"
    is_upgrade = "1"
    install_SSR = "1"
    install_Steam = "1"
    install_Wine = "1"
    install_PlayOnLinux = "1"
    install_Lutris = "1"
    install_GnomeSoftware = "1"
    do_clean = "1"
    is_fixing_dependencies = "1"

if Selected == "5":
    install_flatpak = "0"
    is_update = "1"
    is_fix_plank = "1"
    install_SSR = "1"
    install_Teams = "1"
    do_clean = "1"
    is_fixing_dependencies = "1"

if Selected == "6":
    install_flatpak = "0"
    is_update = "1"
    is_upgrade = "1"
    install_GIMP = "1"
    install_VLC = "1"
    install_Kdenline = "1"
    do_clean = "1"
    is_fixing_dependencies = "1"

if Selected == "7":
    install_flatpak = "0"
    is_update = "1"
    is_upgrade = "1"

if Selected == "8":
    install_flatpak = "0"
    is_update = "1"
    is_upgrade = "1"
    do_clean = "1"
    is_fixing_dependencies = "1"

if Selected == "F":
    update_intel_microcodes = "1"
    install_flatpak = "1"
    is_update = "1"
    is_upgrade = "1"
    install_VLC = "1"
    install_GIMP = "1"
    install_PeaZip = "1"
    install_Wine = "1"
    install_PlayOnLinux = "1"
    install_FireFox = "0"
    install_Chromium = "0"
    install_UnGoogledChromium = "1"
    install_Tor = "1"
    install_LibreOffice = "1"
    install_BleachBit = "0"
    install_Gparted = "1"
    install_QbitTorrent = "1"
    install_SSR = "1"
    install_Teams = "0"
    do_clean = "1"
    is_fixing_dependencies = "1"
    install_XnViewMP = "1"
    install_Caja = "1"
    install_Krita = "1"
    install_Kdenline = "1"
    install_GnomeDisk = "1"
    install_DoubleCmd = "1"
    install_Baobab = "1"
    install_KolourPaint = "1"
    install_Stacer = "1"
    install_GnomeSoftware = "1"
    choose_method_for_Debian = False

if Selected == "Y":
    update_intel_microcodes = "1"
    install_flatpak = "1"
    install_GIMP = "1"
    install_VLC = "1"
    install_QbitTorrent = "1"
    install_LibreOffice = "1"
    install_PeaZip = "1"
    install_Stacer = "1"
    install_Notepadqq = "1"
    install_ThunderBird = "1"
    install_Steam = "1"
    install_Telegram = "2"
    install_SSR = "1"
    install_Scratch3 = "1"
    install_VBOX = "1"
    install_Discord = "1"
    install_GnomeSoftware = "1"
    choose_method_for_Debian = False

if Selected == "0":
    is_update = "1"
    is_upgrade = "1"
    print("==================== Set Basic Setting ====================")
    update_intel_microcodes = input("Update MicroCode For Intel (No = 0/Yes = 1): = ")
    update_amd64_microcodes = input("Update MicroCode For Amd64 (No = 0/Yes = 1): = ")
    install_MediaCodes = input("Install Media Codes (No = 0/Yes = 1): = ")
    is_fix_gedit = input(
        "Use this If Cyrillic is not displayed in the Gedit text editor! (No = 0/Yes = 1): = "
    )
    is_fix_plank = input("Remove anchor icon in Plank (No = 0/Yes = 1): = ")
    install_FlashPlayer = input("Install FlashPlayer (No = 0/Yes[flatpak] = 1): = ")
    install_MSFonts = input(
        "Install Microsoft's fonts - for example, Times New Roman (No = 0/Yes = 1): = "
    )
    print("==================== Install Programs ====================")
    install_flatpak = input(
        "[Open-Source] Flatpak - System for collecting self-sufficient packages (No = 0/Yes = 1): = "
    )
    install_VLC = input(
        "[Open-Source] VLC - MediaPlayer (No = 0/Yes = 1/Yes[flatpak] = 2): = "
    )
    install_MPV = input("[Open-Source] MPV - MediaPlayer (No = 0/Yes = 1): = ")
    install_GIMP = input(
        "[Open-Source] GIMP - Raster Graphic Editor (No = 0/Yes = 1): = "
    )
    install_Krita = input(
        "[Open-Source] Krita - Raster Graphic Editor (No = 0/Yes = 1/Yes[flatpak] = 2): = "
    )
    install_MyPaint = input(
        "[Open-Source] MyPaint - Raster Graphic Editor (No = 0/Yes = 1): = "
    )
    install_KolourPaint = input(
        "[Open-Source] KolourPaint - Raster Graphic Editor (No = 0/Yes = 1): = "
    )
    install_InkScape = input(
        "[Open-Source] InkScape - Vector Graphic Editor (No = 0/Yes = 1): = "
    )
    install_Blender = input(
        "[Open-Source] Blender - 3D Editor (No = 0/Yes = 1/Yes[flatpak] = 2): = "
    )
    install_SweetHome3D = input(
        "[Open-Source] Sweet Home 3D - 3D Home Editor (No = 0/Yes = 1): = "
    )
    install_Scratch = input(
        "[Open-Source] Scratch - Game Developer Tools (No = 0/Yes = 1): = "
    )
    install_Scratch3 = input(
        "[Open-Source] Scratch 3 - Game Developer Tools (No = 0/Yes[Flatpak only] = 1): = "
    )
    install_TurboWarp = input(
        "[Open-Source] TurboWarp - Improved Scratch 3 (No = 0/Yes[Flatpak only] = 1): = "
    )
    install_FileZilla = input(
        "[Open-Source] FileZilla - FTP Client (No = 0/Yes = 1): = "
    )
    install_Caja = input(
        "[Open-Source] Caja - The File Manager of MATE (No = 0/Yes = 1): = "
    )
    install_TimeShift = input(
        "[Open-Source] TimeShift - Alternative to Time Machine (No = 0/Yes = 1): = "
    )
    install_PeaZip = input(
        "[Open-Source] PeaZip - Alternative to WinRar (No = 0/Yes = 1/Yes[flatpak] = 2): = "
    )
    install_Kdenline = input(
        "[Open-Source] Kdenline - Open KDE Video Editor (No = 0/Yes = 1): = "
    )
    install_OpenShot = input(
        "[Open-Source] OpenShot - Open Video Editor (No = 0/Yes = 1): = "
    )
    install_Pitivi = input(
        "[Open-Source] Pitivi - Open Video Editor (No = 0/Yes = 1): = "
    )
    install_Audacity = input(
        "[Open-Source] Audacity - Open Audio Editor (No = 0/Yes = 1): = "
    )
    install_GrubCustomizer = input(
        "[Unknown] Grub Customizer - For Grub Customition (No = 0/Yes = 1): = "
    )
    install_VBOX = input(
        "[Open-Source] Virtual Box - Virtual Computer (No = 0/Yes = 1): = "
    )
    install_Notepadqq = input(
        "[Open-Source] Notepadqq - Text Editor (No = 0/Yes = 1): = "
    )
    install_Wine = input("[Open-Source] Wine - Windows API (No = 0/Yes = 1): = ")
    install_PlayOnLinux = input(
        "[Open-Source] PlayOnLinux - For Run Windows Apps (No = 0/Yes = 1): = "
    )
    install_Lutris = input(
        "[Open-Source] Lutris - For Run Windows Games (No = 0/Yes = 1): = "
    )
    install_ThunderBird = input(
        "[Open-Source] ThunderBird - Open Mail Client(No = 0/Yes = 1): = "
    )
    install_LibreWolf = input(
        "[Open-Source] LibreWolf - Open Web-broweser(No = 0/Yes = 1/Yes[flatpak] = 2): = "
    )
    install_FireFox = input(
        "[Open-Source] FireFox - Open Web-broweser(No = 0/Yes = 1): = "
    )
    install_Chromium = input(
        "[Open-Source] Chromium - Open Web-broweser(No = 0/Yes = 1/Yes[flatpak] = 2): = "
    )
    install_UnGoogledChromium = input(
        "[Open-Source] Ungoogled Chromium - Open Web-broweser(No = 0/Yes = 1): = "
    )
    install_Tor = input(
        "[Open-Source] Tor Browser - Web-broweser by Tor Project (No = 0/Yes = 1/Yes[flatpak] = 2): = "
    )
    install_ShotWell = input(
        "[Open-Source] ShotWell - Image Viewer, Alternative to XnView MP (No = 0/Yes = 1): = "
    )
    install_Kate = input(
        "[Open-Source] Kate - KDE Text Editor, Alternative to Sublime Text(No = 0/Yes = 1): = "
    )
    install_MousePad = input(
        "[Open-Source] MousePad - XFCE Text Editor (No = 0/Yes = 1): = "
    )
    install_PyCharm = input(
        "[Open-Source] PyCharm Community - Community IDE Editor (No = 0/Yes = 1/Yes = 2[flatpak]): = "
    )
    install_VSC = input(
        "[Open-Source] VScodium - Development Environment (No = 0/Yes = 1/Yes[flatpak] = 2): = "
    )
    install_LibreOffice = input(
        "[Open-Source] LibreOffice - Open Source Office (No = 0/Yes = 1): = "
    )
    install_OnlyOffice = input(
        "[Open-Source] OnlyOffice - Open Source Office (No = 0/Yes[flatpak only] = 1): = "
    )
    install_BleachBit = input(
        "[Open-Source] BleachBit - Alternative to Piriform Capt_clean (No = 0/Yes = 1): = "
    )
    install_Stacer = input(
        "[Open-Source] Stacer - Alternative to Piriform Capt_clean (No = 0/Yes = 1): = "
    )
    install_Cheese = input("[Open-Source] Cheese - Camera (No = 0/Yes = 1): = ")
    install_Gparted = input("[Open-Source] Gparted - Disk Utility (No = 0/Yes = 1): = ")
    install_QbitTorrent = input(
        "[Open-Source] Qbittorrent - Torrent Client  (No = 0/Yes = 1): = "
    )
    install_SSR = input(
        "[Open-Source] Simple Screen Recorder - Screen Recorder  (No = 0/Yes = 1): = "
    )
    install_OBS = input(
        "[Open-Source] OBS Studio - Screen Recorder  (No = 0/Yes = 1): = "
    )
    install_Steam = input(
        "[Proprietary Freeware] Steam - Center For Games and Software (No = 0/Yes = 1/Yes[flatpak] = 2): = "
    )
    install_Pidgin = input("[Open-Source] Pidgin - For Chating (No = 0/Yes = 1): = ")
    install_Telegram = input(
        "[Open-Source Client/Proprietary Server] Telegram - For Chating (No = 0/Yes[flatpak only] = 1): = "
    )
    install_Teams = input(
        "[Proprietary Software] Microsoft Teams - For Study (No = 0/Yes[Unofficial flatpak] = 1/Yes[flatpak] = 2): = "
    )
    install_Gpp = input("[Open-Source] G++ - C++ Compiler (No = 0/Yes = 1): = ")
    install_ArduinoIDLE = input(
        "[Open-Source] Arduino IDLE - IDLE for Arduino (No = 0/Yes = 1): = "
    )
    install_Python3IDLE = input(
        "[Open-Source] Python3 IDLE - IDLE for Python (No = 0/Yes = 1): = "
    )
    install_GnomeSoftware = input(
        "[Open-Source] Gnome Software - Application Manager (No = 0/Yes = 1): = "
    )
    install_Synaptic = input(
        "[Open-Source] Synaptic - Application Manager (No = 0/Yes = 1): = "
    )
    install_ClamAV = input(
        "[Open-Source] ClamAV - AntiVirus Program(No = 0/Yes = 1): = "
    )
    install_GnomeDisk = input(
        "[Open-Source] Gnome Disk - Disk Utility (No = 0/Yes = 1/Yes = 2): = "
    )
    install_DoubleCmd = input(
        "[Open-Source] Double commander - Alternative to Total commander (No = 0/Yes = 1): = "
    )
    install_Baobab = input("[Open-Source] Baobab - Disk Analyzer (No = 0/Yes = 1): = ")
    install_CodeBlocks = input(
        "[Open-Source] Code::Blocks - Alternative to Dev-C++ (No = 0/Yes = 1/Yes[flatpak] = 2): = "
    )
    install_GodotEngine = input(
        "[Open-Source] Godot Engine - Game Engine(No = 0/Yes = 1/Yes[flatpak] = 2): = "
    )
    install_IPTables = input(
        "[Open-Source] IPTables - Net Tools(No = 0/Yes = 1[flatpak]): = "
    )
    install_UFW = input("[Open-Source] UFW - Firewall(No = 0/Yes = 1[flatpak]): = ")

print("\n==================== Start ====================\n")

# Update
if is_update == "1":
    update_packege(root_password)
if is_upgrade == "1":
    upgrade_packeges(root_password)

# Check
# You will have to enable both contrib and non-free
if update_intel_microcodes == "1":
    what_is_it("MicroCode For Intel")
    apt_install(root_password, "intel-microcode")

if update_amd64_microcodes == "1":
    what_is_it("MicroCode For Amd64")
    apt_install(root_password, "amd64-microcode")

# TODO Check
if install_MediaCodes == "1":
    what_is_it("Media Codes")
    apt_install(root_password, "libavcodec-extra")

# Fixes
if is_fix_gedit == "1":
    fix_gedit(root_password)

if is_fix_plank == "1":
    fix_plank(root_password)

# Installs
if install_flatpak == "1":
    flatpak(root_password)

if install_FlashPlayer == "1":
    what_is_it("Flash Player")
    flatpak_install("com.adobe.Flash-Player-Projector")

if install_MSFonts == "1":
    what_is_it("Microsoft's Fonts")
    apt_install(root_password, "ttf-mscorefonts-installer")
    apt_install(root_password, "msttcorefonts")

if install_VLC == "1":
    what_is_it("VLC")
    apt_install(root_password, "vlc")
elif install_VLC == "2":
    what_is_it("VLC [flatpak]")
    flatpak_install("org.videolan.VLC")

if install_MPV == "1":
    what_is_it("MPV")
    apt_install(root_password, "mpv")

if install_GIMP == "1":
    what_is_it("GIMP")
    apt_install(root_password, "gimp")

if install_Krita == "1":
    what_is_it("Krita")
    apt_install(root_password, "krita")
elif install_Krita == "2":
    what_is_it("Krita [flatpak]")
    flatpak_install("org.kde.krita")

if install_MyPaint == "1":
    what_is_it("MyPaint")
    apt_install(root_password, "mypaint-data")
    apt_install(root_password, "mypaint")

if install_MyPaint == "1":
    what_is_it("KolourPaint")
    apt_install(root_password, "kolourpaint")

if install_InkScape == "1":
    what_is_it("InkScape")
    apt_install(root_password, "inkscape")

if install_Blender == "1":
    what_is_it("Blender")
    apt_install(root_password, "blender")
elif install_Blender == "2":
    what_is_it("Blender [Flatpak]")
    flatpak_install("org.blender.Blender")

if install_SweetHome3D == "1":
    what_is_it("SweetHome3D")
    apt_install(root_password, "sweethome3d")

if install_Scratch == "1":
    what_is_it("Scratch")
    apt_install(root_password, "scratch")

if install_Scratch3 == "1":
    what_is_it("Scratch 3 [Flatpak only]")
    flatpak_install("edu.mit.Scratch")

if install_TurboWarp == "1":
    what_is_it("TurboWarp [Flatpak only]")
    flatpak_install("org.turbowarp.TurboWarp")

if install_FileZilla == "1":
    what_is_it("FileZilla")
    apt_install(root_password, "filezilla")

if install_Caja == "1":
    what_is_it("Caja")
    apt_install(root_password, "caja")

if install_TimeShift == "1":
    what_is_it("TimeShift")
    if not choose_method_for_Debian:
        execute_as_root(root_password, "sudo apt-add-repository -y ppa:teejee2008/ppa")
    update_packege(root_password)
    apt_install(root_password, "timeshift")

# TODO Check
if install_PeaZip == "1":
    what_is_it("PeaZip")
    execute_as_root(
        root_password,
        "wget -nc https://github.com/peazip/PeaZip/releases/download/9.5.0/peazip_9.5.0.LINUX.GTK2-1_amd64.deb",
    )
    apt_install(root_password, "./peazip_*")
elif install_PeaZip == "2":
    what_is_it("PeaZip[flatpak]")
    update_packege(root_password)
    apt_install(root_password, "flatpak")
    flatpak_install("io.github.peazip.PeaZip")

if install_Kdenline == "1":
    what_is_it("Kdenline")
    if not choose_method_for_Debian:
        execute_as_root(
            root_password, "sudo add-apt-repository ppa:kdenlive/kdenlive-stable --yes"
        )
    update_packege(root_password)
    apt_install(root_password, "kdenlive")

if install_OpenShot == "1":
    what_is_it("OpenShot")
    apt_install(root_password, "openshot")

if install_Pitivi == "1":
    what_is_it("Pitivi")
    apt_install(root_password, "pitivi")

if install_Audacity == "1":
    what_is_it("Audacity")
    apt_install(root_password, "audacity")

if install_GrubCustomizer == "1":
    what_is_it("GrubCustomizer")
    apt_install(root_password, "grub-customizer")

# TODO Check
if install_VBOX == "1":
    what_is_it("Virtualbox")
    if choose_method_for_Debian:
        execute(
            "wget -nc https://download.virtualbox.org/virtualbox/7.0.12/virtualbox-7.0_7.0.12-159484~Debian~bookworm_amd64.deb"
        )
        apt_install(root_password, "./virtualbox-*")
    else:
        apt_install(root_password, "virtualbox")

if install_Notepadqq == "1":
    what_is_it("Notepadqq")
    apt_install(root_password, "notepadqq")

if install_Wine == "1":
    what_is_it("Wine")
    apt_install(root_password, "wine")

# TODO Check
if install_PlayOnLinux == "1":
    what_is_it("PlayOnLinux")
    if choose_method_for_Debian:
        execute_as_root(root_password, "sudo dpkg --add-architecture i386")
        apt_install(root_password, "netcat")
        execute_as_root(
            root_password,
            'wget -q "http://deb.playonlinux.com/public.gpg" -O- | apt-key add -',
        )
        execute_as_root(
            root_password,
            "wget http://deb.playonlinux.com/playonlinux_wheezy.list -O /etc/apt/sources.list.d/playonlinux.list",
        )
        update_packege(root_password)
        apt_install(root_password, "playonlinux")
        execute_as_root(
            root_password,
            "sudo apt-get update && sudo apt-get upgrade && sudo apt-get dist-upgrade",
        )
        apt_install(root_password, "multiarch-support libgl1-mesa-glx:i386")
    else:
        apt_install(root_password, "playonlinux")
        apt_install(root_password, "winbind")
        apt_install(root_password, "winetricks")

if install_Lutris == "1":
    what_is_it("Lutris")
    execute_as_root(
        root_password, "sudo add-apt-repository ppa:lutris-team/lutris --yes"
    )
    update_packege(root_password)
    apt_install(root_password, "lutris")

if install_ThunderBird == "1":
    what_is_it("ThunderBird")
    apt_install(root_password, "thunderbird")

# TODO Check
if install_LibreWolf == "1":
    what_is_it("LibreWolf")
    if not choose_method_for_Debian:
        execute_as_root(
            root_password,
            'distro=$(if echo " bullseye focal impish jammy uma una " | grep -q " $(lsb_release -sc) "; then echo $(lsb_release -sc); else echo focal; fi) && echo "deb [arch=amd64] http://deb.librewolf.net $distro main" | sudo tee /etc/apt/sources.list.d/librewolf.list && sudo wget https://deb.librewolf.net/keyring.gpg -O /etc/apt/trusted.gpg.d/librewolf.gpg && sudo apt update -y && sudo apt install librewolf -y',
        )
    elif choose_method_for_Debian:
        execute_as_root(
            root_password,
            """sudo apt update && sudo apt install -y wget gnupg lsb-release apt-transport-https ca-certificates
distro=$(if echo " una bookworm vanessa focal jammy bullseye vera uma " | grep -q " $(lsb_release -sc) "; then lsb_release -sc; else echo focal; fi) && wget -O- https://deb.librewolf.net/keyring.gpg | sudo gpg --dearmor -o /usr/share/keyrings/librewolf.gpg && sudo tee /etc/apt/sources.list.d/librewolf.sources << EOF > /dev/null
Types: deb
URIs: https://deb.librewolf.net
Suites: $distro
Components: main
Architectures: amd64
Signed-By: /usr/share/keyrings/librewolf.gpg
EOF
sudo apt update && sudo apt install librewolf -y""",
        )

elif install_LibreWolf == "2":
    flatpak_install("io.gitlab.librewolf-community")

if install_FireFox == "1":
    what_is_it("FireFox")
    if choose_method_for_Debian:
        apt_install(root_password, "firefox-esr")
    else:
        apt_install(root_password, "firefox")

if install_Chromium == "1":
    what_is_it("Chromium")
    apt_install(root_password, "chromium-browser")
elif install_Chromium == "2":
    what_is_it("Chromium [Flatpak]")

    flatpak_install("org.chromium.Chromium")

if install_UnGoogledChromium == "1":
    what_is_it("Ungoogled Chromium [Flatpak]")

    flatpak_install("com.github.Eloston.UngoogledChromium")

if install_Tor == "1":
    what_is_it("Tor Browser")
    apt_install(root_password, "torbrowser-launcher")
elif install_Tor == "2":
    what_is_it("Tor Browser [flatpak]")

    flatpak_install("com.github.micahflee.torbrowser-launcher")

if install_ShotWell == "1":
    what_is_it("ShotWell")
    apt_install(root_password, "shotwell")

if install_Kate == "1":
    what_is_it("Kate")
    apt_install(root_password, "kate")

if install_MousePad == "1":
    what_is_it("MousePad")
    apt_install(root_password, "mousepad")

# TODO Check
if install_PyCharm == "1":
    what_is_it("PyCharm Community")
    execute(
        "wget -nc https://download-cdn.jetbrains.com/python/pycharm-community-2023.2.3.tar.gz"
    )
    execute("tar xvf pycharm-community-2023.2.3.tar.gz -C ~/pycharm-community")
elif install_PyCharm == "2":
    what_is_it("PyCharm Community [flatpak]")

    flatpak_install("com.jetbrains.PyCharm-Community")

# TODO Check
if install_VSC == "1":
    what_is_it("VScodium")
    execute(
        "wget -nc https://github.com/VSCodium/vscodium/releases/download/1.84.0.23306/codium_1.84.0.23306_amd64.deb"
    )
    apt_install(root_password, "./codium_*")
elif install_VSC == "2":
    what_is_it("VScodium [flatpak]")

    flatpak_install("com.vscodium.codium")

if install_LibreOffice == "1":
    what_is_it("LibreOffice")
    if not choose_method_for_Debian:
        execute_as_root(
            root_password, "sudo add-apt-repository ppa:libreoffice/ppa --yes"
        )
    update_packege(root_password)
    apt_install(root_password, "libreoffice")

if install_OnlyOffice == "1":
    what_is_it("OnlyOffice [Flatpak only]")
    flatpak_install("org.onlyoffice.desktopeditors")

if install_BleachBit == "1":
    what_is_it("Bleach Bit")
    apt_install(root_password, "bleachbit")

if install_Stacer == "1":
    what_is_it("Stacer")
    if choose_method_for_Debian:
        execute_as_root(
            root_password,
            "wget -nc https://github.com/oguzhaninan/Stacer/releases/download/v1.1.0/stacer_1.1.0_amd64.deb",
        )
        apt_install(root_password, "./stacer_*")
    else:
        apt_install(root_password, "stacer")

if install_Cheese == "1":
    what_is_it("Cheese")
    apt_install(root_password, "cheese")

if install_Gparted == "1":
    what_is_it("Gparted")
    apt_install(root_password, "gparted")

if install_QbitTorrent == "1":
    what_is_it("qBittorrent")
    apt_install(root_password, "qbittorrent")

if install_SSR == "1":
    what_is_it("Simple Screen Recorder")
    update_packege(root_password)
    apt_install(root_password, "simplescreenrecorder")

if install_OBS == "1":
    what_is_it("OBS Studio")
    update_packege(root_password)
    apt_install(root_password, "obs-studio")

if install_Steam == "1":
    what_is_it("Steam")
    apt_install(root_password, "steam")
elif install_Steam == "2":
    what_is_it("Steam [flatpak]")

    flatpak_install("com.valvesoftware.Steam")

if install_Pidgin == "1":
    what_is_it("Pidgin")
    apt_install(root_password, "pidgin")

if install_Telegram == "1":
    what_is_it("Telegram [flatpak only]")

    flatpak_install("org.telegram.desktop")

# TODO Check
if install_Teams == "1":
    what_is_it("MS Teams [Unofficial flatpak]")

    flatpak_install("com.github.IsmaelMartinez.teams_for_linux")
elif install_Teams == "2":
    what_is_it("MS Teams [flatpak]")

    flatpak_install("com.microsoft.Teams")

if install_Gpp == "1":
    what_is_it("G++")
    execute_as_root(root_password, "sudo apt update --yes")
    execute_as_root(root_password, "sudo apt-get install g++ -y")
    print("\nHint: Use to build $ g++ <YourCode>.cpp -o <NameYouFutureProgram> ")
    print("Hint: Use to run $ ./<NameYouProgram>\n")

if install_ArduinoIDLE == "1":
    what_is_it("Arduino IDLE")
    execute_as_root(root_password, "sudo apt install arduino --yes")

if install_Python3IDLE == "1":
    what_is_it("Python IDLE")
    execute_as_root(root_password, "sudo apt-get install idle3 --yes")

if install_GnomeSoftware == "1":
    what_is_it("Gnome Software")
    execute_as_root(root_password, "sudo snap remove gnome-software")
    apt_install(root_password, "gnome-software gnome-software-plugin-flatpak")

if install_Synaptic == "1":
    what_is_it("Synaptic")
    apt_install(root_password, "synaptic")

if install_ClamAV == "1":
    what_is_it("ClamAV")
    execute_as_root(root_password, "sudo apt-get install clamav --yes")
    execute_as_root(root_password, "sudo apt-get install clamav-daemon --yes")
    execute_as_root(root_password, "sudo apt install clamtk --yes")
    execute_as_root(root_password, "sudo apt-get install libclamunrar6 --yes")

if install_GnomeDisk == "1":
    what_is_it("Gnome Disk")
    execute_as_root(root_password, "sudo apt-get install gnome-disk-utility --yes")

if install_DoubleCmd == "1":
    what_is_it("Double commander")
    execute_as_root(root_password, "sudo apt-get install doublecmd-gtk --yes")

if install_Baobab == "1":
    what_is_it("Baobab Disk Analyzer")
    execute_as_root(root_password, "sudo apt-get install baobab --yes")

if install_CodeBlocks == "1":
    what_is_it("Code::Blocks")
    apt_install(root_password, "codeblocks")
elif install_CodeBlocks == "2":
    what_is_it("Code::Blocks via flatpak")

    flatpak_install("org.codeblocks.codeblocks")

if install_GodotEngine == "1":
    what_is_it("Godot 3")
    execute_as_root(root_password, "godot3")
elif install_GodotEngine == "2":
    what_is_it("Godot 3 [Flatpak]")

    flatpak_install("org.godotengine.Godot3")

if install_IPTables == "1":
    what_is_it("IPTables")
    apt_install(root_password, "iptables iptables-persistent")

if install_UFW == "1":
    what_is_it("UFW")
    apt_install(root_password, "ufw")
    execute_as_root(root_password, "sudo systemctl enable ufw --now")
    execute("systemctl status ufw")

if is_fixing_dependencies == "1":
    print(
        "\n===================== Updating and fixing dependencies ====================="
    )
    for i in range(3):
        print(f"{i})")
        execute_as_root(root_password, "sudo apt --fix-broken install --yes")
        execute_as_root(root_password, "sudo apt install -f -y")
        execute_as_root(root_password, "sudo apt install dpkg --fix-missing")
        execute_as_root(root_password, "sudo dpkg --configure -a")

if do_clean == "1":
    apt_clean(root_password)

print("\n===================== End =====================")

if int(input("ReBoot? (No = 0/Yes = 1): = ")):
    execute_as_root(root_password, "sudo shutdown -r now")
