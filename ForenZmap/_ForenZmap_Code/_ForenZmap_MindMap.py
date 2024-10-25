from jinja2 import Template
from pwn import log
import os

try:
    def HtmlPares(RegValues, RegKey, RegPath):
        
        HtmlTemplate = """
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <style>
                    body {
                        font-family: 'Courier New', Courier, monospace;
                        font-size: 16px;
                        color: #33FF00;
                        background-color: #f0f0f0;
                        line-height: 1.5;
                        overflow-x: hidden;
                        overflow-y: auto;
                        max-width: 100vw;
                        max-height: 100vh;
                        padding: 10px;
                        box-sizing: border-box;
                        word-wrap: break-word;
                        white-space: normal;
                    }
                    h3 {
                        color: #1E1E1E;
                    }
                    ul {
                        list-style-type: none;
                        padding-left: 20px;
                        margin: 0;
                    }
                    li {
                        margin: 10px 0;
                        position: relative;
                    }
                    li::before {
                        content: "";
                        border-left: 2px solid #000;
                        position: absolute;
                        left: -15px;
                        top: 0;
                        height: 100%;
                    }
                    li > ul::before {
                        content: "";
                        border-top: 2px solid #000;
                        position: absolute;
                        top: 15px;
                        left: -15px;
                        width: 20px;
                    }
                    .box {
                        display: inline-block;
                        background-color: #1E1E1E;
                        border: 1px solid #ccc;
                        border-radius: 8px;
                        padding: 5px 10px;
                        box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.2);
                        font-family: Arial, sans-serif;
                        font-size: 0.9em;
                        word-wrap: break-word;
                        white-space: normal;
                        max-width: 100%;
                        overflow: hidden;
                    }
                    .horizontal-box {
                        display: flex;
                        align-items: center;
                    }
                    .line {
                        border-top: 2px solid #000;
                        margin: 0 5px;
                        width: 30px;
                    }
                </style>
            </head>
            <body>
                <ul>
                    <h3>{{ RegPath }}</h3>
                    <li><div class="box">{{ RegKey }}</div>
                        <ul>
                            {% for value in RegValues %}
                            <li class="horizontal-box">
                                <div class="box">{{ value.name }}</div>
                                <div class="line"></div>
                                <div class="box">{{ value.data }}</div>
                            </li>
                            {% endfor %}
                        </ul>
                    </li>
                </ul>
            </body>
            </html>
        """

        try:
            global OutputReport
            OutputReport = "ForenZmap_Report.html"

            with log.progress("Parsing Registry") as progress:
                template = Template(HtmlTemplate)
                RenderedHtml = template.render(RegValues=RegValues, RegKey=RegKey, RegPath=RegPath)

                with open(OutputReport, 'a') as file:
                    file.write(RenderedHtml)
                progress.success(f"Data is being appended to the HTML file {OutputReport}")

        except Exception as e:
            with log.progress("Parsing Registry") as progress:
                progress.failure(f"Failed to create HTML file")
        

    def OpenFile():
        try:
            os.startfile(OutputReport)
        except Exception as e:
            print(f"Failed to open the file:")

except Exception:
        pass