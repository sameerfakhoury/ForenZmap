from _ForenZmap_Code import _ForenZmap_MindMap

def ApplicationDef(InterfaceKey):
    try:
        for subkey in InterfaceKey.iter_subkeys():
            RegValues = []
            for value in subkey.iter_values():
                RegValues.append({'name': value.name, 'data': value.value})

            RegPath = r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall"
            RegKey = {subkey.name}
            _ForenZmap_MindMap.HtmlPares(RegValues, RegKey, RegPath)    

    except Exception:
        pass