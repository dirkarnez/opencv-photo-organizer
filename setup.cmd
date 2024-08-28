@REM run as Administrator
@echo off

if not exist "%USERPROFILE%\Downloads\python-3.10.8-amd64-portable" (
cd /d "%TEMP%" && ^
%SystemRoot%\System32\curl.exe "https://github.com/dirkarnez/python-portable/releases/download/v3.10.8/python-3.10.8-amd64-portable.zip" -L -O  && ^
C:\PROGRA~1\7-Zip\7z.exe x python-3.10.8-amd64-portable.zip -o"%USERPROFILE%\Downloads\python-3.10.8-amd64-portable"  && ^
del python-3.10.8-amd64-portable.zip
)
