# ForenZmap

```
___________                         __________
\_   _____/__________   ____   ____ \____    / _____ _____  ______
 |    __)/  _ \_  __ \_/ __ \ /    \  /     / /     \__  \ \____ \
 |     \(  <_> )  | \/\  ___/|   |  \/     /_|  Y Y  \/ __ \|  |_> >
 \___  / \____/|__|    \___  >___|  /_______ \__|_|  (____  /   __/
     \/                    \/     \/        \/     \/     \/|__|

```

ForenZmap is a digital forensics registry parsing triage tool developed by Sameer Fakhoury based on Python that allows users to extract and analyze important Windows registry keys, presenting the results in a mind map format for easier visualization. It operates by providing the paths to the SYSTEM.hiv and SOFTWARE.hiv files, automatically performing the extraction and parsing of the relevant data.

Currently, it supports the extraction and parsing of 14 significant keys along with their subkeys and associated values. Additionally, it can decode certain time-related values to streamline the timeline of your investigation. Upon completion, ForenZmap generates an HTML report that visualizes the data as a mind map.

In terms of usage, the tool's creator disclaims any responsibility for misuse, underscoring its educational intent. Users wishing to add features must seek permission from the creator and are not permitted to reuse the code without proper authorization.

---
Steps to follow to install the tool:
```
1. Download the tool as a ZIP file by clicking the "Code" button.
2. Extract the contents of the ZIP file.
3. Open your command line and navigate to the ForenZmap-main directory.
4. Run cd ForenZmap.
5. Use ls to verify that the requirements.txt file is present.
6. Install the required dependencies with pip install -r requirements.txt.
7. Start the tool by executing python3 ForenZmap.py.
8. You can now use the tool by supplying the SYSTEM.hiv, SOFTWARE.hiv, or both.
```
---
This is the text that will be displayed when you run the tool.
```
[x] Welcome to ForenZmap! You can perform triage parsing on the SOFTWARE.hiv, SYSTEM.hiv, or both. Press spacebar to continue.
[x] Enter the path for SOFTWARE.hiv (or press Enter to skip) ex: C:\Users\semo\Desktop\SOFTWARE.hiv

[x] Enter the path for SYSTEM.hiv (or press Enter to skip): ex: C:\Users\semo\Desktop\SYSTEM.hiv
```
