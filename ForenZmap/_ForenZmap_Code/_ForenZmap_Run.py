from _ForenZmap_Code import _ForenZmap_MindMap

def RunKeyDef(RunKey):
    try:
        RegValues = []

        for value in RunKey.iter_values():
            RegValues.append({'name': value.name, 'data': value.value})   

        RegPath = r"SOFTWARE\Microsoft\Windows\CurrentVersion\Run"
        RegKey = {RunKey.name}
        _ForenZmap_MindMap.HtmlPares(RegValues, RegKey, RegPath)    

    except Exception:
        pass