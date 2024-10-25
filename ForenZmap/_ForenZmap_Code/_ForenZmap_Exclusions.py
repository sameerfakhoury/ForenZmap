from _ForenZmap_Code import _ForenZmap_MindMap

def ExclusionsDef(Exclusionskey):
        try: 
                RegValues = []
                for value in Exclusionskey.iter_values():
                        RegValues.append({'name': value.name, 'data': value.value})   

                RegPath = r"SOFTWARE\Microsoft\Windows Defender\Exclusions\Paths"
                RegKey = {Exclusionskey.name}
                _ForenZmap_MindMap.HtmlPares(RegValues, RegKey, RegPath)  
                  
        except Exception:
                pass