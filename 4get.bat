@echo off
setlocal
cls
for /f tokens^=2-5^ delims^=.-_^" %%j in ('python --version 2^>^&1') do set "pyver=%%k%%m%%j"
echo.%pyver%|findstr "35" >nul 2>&1
if %ERRORLEVEL% == 0 goto 4get
echo Python 3.5 not found on this system. Please install Python and try again.
goto end
:4get
python threadDownloader.py
goto end
:end
endlocal
exit /b %ERRORLEVEL%
