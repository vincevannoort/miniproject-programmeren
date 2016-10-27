@echo off

cd %~dp0%\applicatie
%~dp0%\applicatie\setup.py install 
RD /S /Q "%~dp0%\applicatie\twilio.egg-info"
RD /S /Q "%~dp0%\applicatie\build"
RD /S /Q "%~dp0%\applicatie\dist"
