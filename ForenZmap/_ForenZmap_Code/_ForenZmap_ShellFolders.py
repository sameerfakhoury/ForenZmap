from _ForenZmap_Code import _ForenZmap_MindMap

def ShellFoldersDef(ShellFoldersKey):
        try:
                RegValues = []
                
                for value in ShellFoldersKey.iter_values():
                        RegValues.append({'name': value.name, 'data': value.value})   

                RegPath = r"SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders"
                RegKey = {ShellFoldersKey.name}
                _ForenZmap_MindMap.HtmlPares(RegValues, RegKey, RegPath) 
                   
        except Exception:
                pass