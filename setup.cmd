@REM run as Administrator
@echo off

set PYTHON_DIR=%USERPROFILE%\Downloads\python-3.10.8-amd64-portable
set PYTHON_EXE=%PYTHON_DIR%\python.exe

if not exist %PYTHON_EXE% (
cd /d "%TEMP%" && ^
%SystemRoot%\System32\curl.exe "https://github.com/dirkarnez/python-portable/releases/download/v3.10.8/python-3.10.8-amd64-portable.zip" -L -O  && ^
C:\PROGRA~1\7-Zip\7z.exe x python-3.10.8-amd64-portable.zip -o"%PYTHON_DIR%"  && ^
del python-3.10.8-amd64-portable.zip
) else (
    echo python %PYTHON_EXE% found
)

pause