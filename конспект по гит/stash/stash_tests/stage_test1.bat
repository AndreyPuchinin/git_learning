@echo off
SETLOCAL

for /f "delims=" %%a in ('wmic OS get localdatetime  ^| find "."') do set datetime=%%a
set "YYYY=%datetime:~0,4%"
set "MM=%datetime:~4,2%"
set "DD=%datetime:~6,2%"
set "HH=%datetime:~8,2%"
set "MI=%datetime:~10,2%"
set "SS=%datetime:~12,2%"
set mydir=%YYYY%-%MM%-%DD%-%HH%-%MI%-%SS%

@echo on
@prompt $g 

@call :log "========= init repository in a new folder"
mkdir %mydir%
@cd %mydir%
git init

@call :log "========= first commit: file1.txt"
echo 'state 1' > file1.txt
git add file1.txt
git commit -m "first commit"
git status
git log --oneline --decorate --graph --all

@call :log "=========  edit and add file1.txt"
echo 'state 2' > file1.txt
git add file1.txt
git status
git log --oneline --decorate --graph --all

@call :log "========= hide last data in master branch"
git stash
git stash list
git status
git log --oneline --decorate --graph --all

pause

@call :log "========= refresh last data in master branch"
git stash apply
git status
git log --oneline --decorate --graph --all

pause


:log 
@echo.
@echo.
@powershell write-host -back Red %1
@echo.
@exit /B 0
