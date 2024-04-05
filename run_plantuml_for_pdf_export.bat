@echo off
setlocal

REM Set the URL to download the latest version of PlantUML
set PLANTUML_URL=https://github.com/plantuml/plantuml/releases/download/v1.2021.14/plantuml-1.2021.14.jar

REM Check if the plantuml.jar file exists. If it doesn't, download it from the URL.
if not exist plantuml.jar (
    echo Downloading PlantUML...
    curl -L %PLANTUML_URL% -o plantuml.jar
)

REM Run PlantUML on all .puml files in the current directory and its subdirectories, and output files to the plantuml folder
java -classpath C:\Users\ugur.coruh\Desktop\rteu-intern\plantuml -jar plantuml.jar -charset UTF-8 -tpdf -v -r "./**.puml"

pause
