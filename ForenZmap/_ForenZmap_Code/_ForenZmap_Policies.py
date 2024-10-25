from _ForenZmap_Code import _ForenZmap_MindMap

def PoliciesDef(Policieskey):
        try:
                RegValues = []
                for value in Policieskey.iter_values():
                        RegValues.append({'name': value.name, 'data': value.value})   

                RegPath = r"SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System"
                RegKey = {Policieskey.name}
                _ForenZmap_MindMap.HtmlPares(RegValues, RegKey, RegPath)  

        except Exception:
                pass