from _ForenZmap_Code import _ForenZmap_MindMap

def ComputerNameDef(ComputerNameKey, SelectKeyNum):
    try:
        RegValues = []
        for value in ComputerNameKey.iter_values():

            if value.name in ("ComputerName"):
                RegValues.append({'name': value.name, 'data': value.value})

        RegPath = r'SYSTEM\ControlSet00'+ SelectKeyNum +r'\Control\ComputerName\ComputerName'
        RegKey = {value.name}
        _ForenZmap_MindMap.HtmlPares(RegValues, RegKey, RegPath)  

    except Exception:
        pass