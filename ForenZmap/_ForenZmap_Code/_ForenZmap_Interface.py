from _ForenZmap_Code import _ForenZmap_MindMap
import datetime

def InterfaceDef(InterfaceKey, SelectKeyNum):
    try:
        for subkey in InterfaceKey.iter_subkeys():
            RegValues = []

            for value in subkey.iter_values():

                if value.name in ("DhcpDefaultGateway", "DhcpDomain", "DhcpNameServer", "DhcpServer", "DhcpSubnetMask", "Domain", "EnableDHCP", "LeaseObtainedTime", "LeaseTerminatesTime"):
                    
                    if value.name == "EnableDHCP":
                        if value.value == 1:
                            value.value = str(value.value) + " - DHCP-assigned IP"
                        else:
                            value.value = str(value.value) + " - static IP"
                        
                    if value.name == ("LeaseObtainedTime"):
                        LeaseObtainedTime = datetime.datetime.fromtimestamp(int(value.value))
                        value.value = str(value.value) + " - " + str(LeaseObtainedTime)
                            
                        
                    if value.name == ("LeaseTerminatesTime"):
                        LeaseTerminatesTime = datetime.datetime.fromtimestamp(int(value.value))
                        value.value = str(value.value) + " - " + str(LeaseTerminatesTime)

                RegValues.append({'name': value.name, 'data': value.value})
                
            RegPath = r'SYSTEM\ControlSet00'+ SelectKeyNum +r'\Services\Tcpip\Parameters\Interfaces'
            RegKey = {subkey.name}
            _ForenZmap_MindMap.HtmlPares(RegValues, RegKey, RegPath)   

    except Exception:
        pass