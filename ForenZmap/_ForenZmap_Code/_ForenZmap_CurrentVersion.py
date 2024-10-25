from _ForenZmap_Code import _ForenZmap_MindMap
import datetime

def CurrentVersioDef(current_version_key):
    try:
        RegValues = []

        for value in current_version_key.iter_values():

            if value.name in ("BuildLab","CompositionEditionID","CurrentBuild","CurrentBuildNumber","CurrentVersion", "DisplayVersion","EditionID",
                                "InstallationType", "InstallDate", "ProductName", "InstallTime", "RegisteredOwner"):
                
                if value.name in ("InstallDate", "InstallTime"):

                    if value.name == "InstallDate":
                        HumanReadableDate = UnixTimestampToDatetime(int(value.value))
                        RegValues.append({'name': value.name, 'data': HumanReadableDate.strftime('%Y-%m-%d %H:%M:%S') if HumanReadableDate else 'N/A'})
                        
                    elif value.name == "InstallTime":
                        HumanReadableTime = FiletimeTODatetime(int(value.value))
                        RegValues.append({'name': value.name, 'data': HumanReadableTime.strftime('%Y-%m-%d %H:%M:%S') if HumanReadableTime else 'N/A'})
                        
                else:
                    RegValues.append({'name': value.name, 'data': value.value})
                    
        RegPath = r"SOFTWARE\Microsoft\Windows NT\CurrentVersion"
        RegKey = value.name
        _ForenZmap_MindMap.HtmlPares(RegValues, RegKey, RegPath)

    except Exception:
        pass

try:
    def FiletimeTODatetime(FileTime):
        if isinstance(FileTime, int):
            return datetime.datetime(1601, 1, 1) + datetime.timedelta(microseconds=FileTime // 10)
        return None

    def UnixTimestampToDatetime(UnixTimeStamp):
        if isinstance(UnixTimeStamp, int):
            return datetime.datetime.fromtimestamp(UnixTimeStamp)
        return None
    
except Exception:
    pass