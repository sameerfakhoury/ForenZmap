from _ForenZmap_Code import _ForenZmap_MindMap

def ConnectionsHistoryDef(ConnectionsHistoryKey):
    try:
        for subkey in ConnectionsHistoryKey.iter_subkeys():
            RegValues = []

            for value in subkey.iter_values():
                if value.name in ("ProfileGuid", "FirstNetwork", "DnsSuffix", "DefaultGatewayMac", "Description"):
                    RegValues.append({'name': value.name, 'data': value.value})

            RegPath = r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\NetworkList\Signatures\Unmanaged"
            RegKey = subkey.name
            _ForenZmap_MindMap.HtmlPares(RegValues, RegKey, RegPath)
            
    except Exception:
        pass