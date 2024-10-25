from _ForenZmap_Code import _ForenZmap_MindMap

def NetworkCardsDef(network_cards_key):
    try:
        for subkey in network_cards_key.iter_subkeys():
            RegValues = []

            for value in subkey.iter_values():
                if value.name in ("Description, ServiceName"):
                    RegValues.append({'name': value.name, 'data': value.value})

            RegPath = r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\NetworkCards"
            RegKey = {subkey.name}
            _ForenZmap_MindMap.HtmlPares(RegValues, RegKey, RegPath) 

    except Exception:
        pass