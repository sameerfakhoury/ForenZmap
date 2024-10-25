from _ForenZmap_Code import _ForenZmap_MindMap

def TimeZoneInformationDef(TimeZoneInformationKey, SelectKeyNum):
    try: 
        RegValues = []
        
        for value in TimeZoneInformationKey.iter_values():
            
            if value.name in ("Bias"):
                UTC = str(((int(value.value) - 4294967296) // 60) * -1)
                UTC = "UTC" + str(UTC) + " - " + str(value.value)
                RegValues.append({'name': value.name, 'data': UTC})
            else:
                RegValues.append({'name': value.name, 'data': value.value})
        
        RegPath = r"SYSTEM\ControlSet00" + SelectKeyNum + r"\Control\TimeZoneInformation"
        _ForenZmap_MindMap.HtmlPares(RegValues, "TimeZoneInformation", RegPath)

    except Exception:
        pass