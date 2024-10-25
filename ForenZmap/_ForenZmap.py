from regipy.registry import RegistryHive
from pwn import log
import keyboard
import os

from _ForenZmap_Code import _ForenZmap_Exclusions, _ForenZmap_ProfileList, _ForenZmap_ComputerName, _ForenZmap_NetworkCards, _ForenZmap_Interface
from _ForenZmap_Code import _ForenZmap_ConnectionsHistory, _ForenZmap_CurrentVersion, _ForenZmap_Run, _ForenZmap_Application, _ForenZmap_Policies
from _ForenZmap_Code import _ForenZmap_Banner, _ForenZmap_ShellFolders, _ForenZmap_Winlogon, _ForenZmap_TimeZoneInformation, _ForenZmap_Select
from _ForenZmap_Code import _ForenZmap_MindMap



try:

    def Delete():
        OutputReport = "ForenZmap_Report.html"

        if os.path.exists(OutputReport):
            os.remove(OutputReport)

    _ForenZmap_Banner.ForenZmapBannerDef()

    def HiveInput(): 
        try:
            print("[x] Welcome to ForenZmap! You can perform triage parsing on the SOFTWARE.hiv, SYSTEM.hiv, or both. Press spacebar to continue.")
            keyboard.wait('space')

            global SOFTWAREHIV
            global SYSTEMHIV

            SOFTWAREHIV = input(r"""[x] Enter the path for SOFTWARE.hiv (or press Enter to skip) ex: C:\Users\semo\Desktop\SOFTWARE.hiv """).strip()
            print(SOFTWAREHIV)
            SYSTEMHIV = input(r"""[x] Enter the path for SYSTEM.hiv (or press Enter to skip): ex: C:\Users\semo\Desktop\SYSTEM.hiv """).strip()

            print(f"[x] You entered the following paths:")

            if SOFTWAREHIV:
                print(f"[+] SOFTWARE.hiv: {SOFTWAREHIV}")
            else:
                print("[-] SOFTWARE.hiv: Not provided")

            if SYSTEMHIV:
                print(f"[+] SYSTEM.hiv: {SYSTEMHIV}")
            else:
                print("[-] SYSTEM.hiv: Not provided")

            print("Press the spacebar to continue...")
            keyboard.wait('space')

        except Exception:
            pass  

    def SOFTWARE():
        try:
            with log.progress("Parsing Registry") as progress:
                if SOFTWAREHIV:
                    SoftwareHive = RegistryHive(SOFTWAREHIV)
                    progress.status("Opened SOFTWARE.hiv")

                    CurrentVersionKey = SoftwareHive.get_key(r'SOFTWARE\Microsoft\Windows NT\CurrentVersion')
                    _ForenZmap_CurrentVersion.CurrentVersioDef(CurrentVersionKey)

                    ProfilesKey = SoftwareHive.get_key(r'SOFTWARE\Microsoft\Windows NT\CurrentVersion\NetworkList\Profiles')
                    _ForenZmap_ProfileList.ProfilesDef(ProfilesKey)

                    NetworkCardsKey = SoftwareHive.get_key(r'SOFTWARE\Microsoft\Windows NT\CurrentVersion\NetworkCards')
                    _ForenZmap_NetworkCards.NetworkCardsDef(NetworkCardsKey)

                    ConnectionsHistoryKey = SoftwareHive.get_key(r'SOFTWARE\Microsoft\Windows NT\CurrentVersion\NetworkList\Signatures\Unmanaged')
                    _ForenZmap_ConnectionsHistory.ConnectionsHistoryDef(ConnectionsHistoryKey)

                    RunKey = SoftwareHive.get_key(r'SOFTWARE\Microsoft\Windows\CurrentVersion\Run')
                    _ForenZmap_Run.RunKeyDef(RunKey)

                    ApplicationKey = SoftwareHive.get_key(r'SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall')
                    _ForenZmap_Application.ApplicationDef(ApplicationKey)

                    Exclusionskey = SoftwareHive.get_key(r'SOFTWARE\Microsoft\Windows Defender\Exclusions\Paths')
                    _ForenZmap_Exclusions.ExclusionsDef(Exclusionskey)
                    
                    Policieskey = SoftwareHive.get_key(r'SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System')
                    _ForenZmap_Policies.PoliciesDef(Policieskey)

                    ShellFoldersKey = SoftwareHive.get_key(r'SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders')
                    _ForenZmap_ShellFolders.ShellFoldersDef(ShellFoldersKey)

                    WinlogonKey = SoftwareHive.get_key(r'SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon')
                    _ForenZmap_Winlogon.WinlogonKeyDef(WinlogonKey)

        except Exception:
            pass 

    def SYSTEM():
        try:
            with log.progress("Parsing Registry") as progress:
                if SYSTEMHIV:
                    SYSTEMHive = RegistryHive(SYSTEMHIV)
                    progress.status("Opened SYSTEM.hiv")

                    SelectKey = SYSTEMHive.get_key(r'SYSTEM\Select')
                    SelectKeyNum = _ForenZmap_Select.SelectDef(SelectKey)

                    InterfaceKey = SYSTEMHive.get_key(r'SYSTEM\ControlSet00' + SelectKeyNum + r'\Services\Tcpip\Parameters\Interfaces')
                    _ForenZmap_Interface.InterfaceDef(InterfaceKey, SelectKeyNum)

                    ComputerNameKey = SYSTEMHive.get_key(r'SYSTEM\ControlSet00' + SelectKeyNum + r'\Control\ComputerName\ComputerName')
                    _ForenZmap_ComputerName.ComputerNameDef(ComputerNameKey, SelectKeyNum)

                    TimeZoneInformationKey = SYSTEMHive.get_key(r'SYSTEM\ControlSet00' + SelectKeyNum + r'\Control\TimeZoneInformation')
                    _ForenZmap_TimeZoneInformation.TimeZoneInformationDef(TimeZoneInformationKey, SelectKeyNum)


        except Exception:
            pass  

    Delete()
    HiveInput()
    SOFTWARE()
    SYSTEM()
    _ForenZmap_MindMap.OpenFile()

except KeyboardInterrupt:
    print("\n[x] Process interrupted by user. Exiting gracefully.")


