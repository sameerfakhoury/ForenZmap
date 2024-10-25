from _ForenZmap_Code import _ForenZmap_MindMap
import struct
from datetime import datetime

def ProfilesDef(ProfilesKey):
    try:
        for subkey in ProfilesKey.iter_subkeys():
            RegValues = []

            for value in subkey.iter_values():
                
                if value.name in ("DateCreated", "DateLastConnected", "Description", "ProfileName"):
                    
                    if value.name == ("DateCreated"):
                        
                        HexString = value.value
                        HexString = HexString.replace("-", "")
                        DataBytes = bytes.fromhex(HexString)

                        TimestampBytes = DataBytes[:4]
                        Timestamp = struct.unpack('<I', TimestampBytes)[0]
                        RelatedTime = datetime.utcfromtimestamp(Timestamp)
                        RelatedTime = RelatedTime.strftime('%Y-%m-%d %H:%M:%S')
                        value.value = RelatedTime + " - " + value.value
                        
                    if value.name == ("DateLastConnected"):

                        HexString = value.value
                        HexString = HexString.replace("-", "")
                        DataBytes = bytes.fromhex(HexString)

                        TimestampBytes = DataBytes[:4]
                        timestamp = struct.unpack('<I', TimestampBytes)[0]
                        RelatedTime = datetime.utcfromtimestamp(timestamp)
                        RelatedTime = RelatedTime.strftime('%Y-%m-%d %H:%M:%S')
                        value.value = RelatedTime + " - " + value.value

                RegValues.append({'name': value.name, 'data': value.value})

            RegPath = r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\NetworkList\Profiles"
            RegKey = {subkey.name}
            _ForenZmap_MindMap.HtmlPares(RegValues, RegKey, RegPath)  
              
    except Exception:
        pass