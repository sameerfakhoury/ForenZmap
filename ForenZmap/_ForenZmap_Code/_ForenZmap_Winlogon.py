from _ForenZmap_Code import _ForenZmap_MindMap

def WinlogonKeyDef(WinlogonKey):
        try:
                RegValues = []

                for value in WinlogonKey.iter_values():
                        RegValues.append({'name': value.name, 'data': value.value})   

                RegPath = r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon"
                RegKey = {WinlogonKey.name}
                _ForenZmap_MindMap.HtmlPares(RegValues, RegKey, RegPath) 
                   
        except Exception:
                pass