@echo off

:_debut
dir *.jpg /X /B /O:N > liste.txt

call :size_file LISTE.txt

:suite
if %size%==0 goto fin

set "ligne="
set /a Numéro=0
for /f "delims=" %%a in ('more/e +%%Numéro%% ^< liste.txt') do (
if not defined ligne set "ligne=%%a"
)

md %ligne:~0,-5%
move %ligne:~0,-5%*.jpg %ligne:~0,-5%

goto _debut

:size_file
set size=%~z1
goto suite

:fin

del liste.txt 