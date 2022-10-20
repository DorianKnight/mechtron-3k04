
cd .

if "%1"=="" ("C:\PROGRA~1\MATLAB\R2022b\bin\win64\gmake"  -f Group44PACEMAKER_Debug_Requirements_Flashing.mk all) else ("C:\PROGRA~1\MATLAB\R2022b\bin\win64\gmake"  -f Group44PACEMAKER_Debug_Requirements_Flashing.mk %1)
@if errorlevel 1 goto error_exit

exit /B 0

:error_exit
echo The make command returned an error of %errorlevel%
exit /B 1