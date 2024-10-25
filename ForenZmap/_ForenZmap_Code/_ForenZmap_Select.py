from _ForenZmap_Code import _ForenZmap_MindMap

try: 
    def SelectDef(Selectkey):
        RegValues = []

        for value in Selectkey.iter_values():

            if value.name in ("Current"):
                Current = RegValues.append({'name': value.name, 'data': value.value})   

        Current = str(RegValues[-1]['data'] if RegValues else 1)

        RegPath = r"SYSTEM\Select"
        RegKey = {Selectkey.name}
        _ForenZmap_MindMap.HtmlPares(RegValues, RegKey, RegPath)    
        return Current
    
except Exception:
    pass