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


call :log "========= init repository in a new folder"
mkdir %mydir%
@cd %mydir%
git init


call :log "========= first commit: file1.txt"
echo 'state 1' > file1.txt
git add file1.txt
git commit -m "first commit"
git status
git log --oneline --decorate --graph --all


call :log "=========  edit and add file1.txt"
echo 'state 2' > file1.txt
git add file1.txt
git status
git log --oneline --decorate --graph --all


call :log "========= hide last data in master branch"
git stash
git stash list
git status
git log --oneline --decorate --graph --all


pause


call :log "========= create branch_2"
git checkout -b branch_2
git log --oneline --decorate --graph --all


call :log "========= first commit in branch_2: file1.txt"
echo 'state 1 in branch_2' > file1.txt
git add file1.txt
git commit -m "first commit in branch_2"
git status
git log --oneline --decorate --graph --all


call :log "=========  edit and add file1.txt in branch_2"
echo 'state 2 in branch_2' > file1.txt
git add file1.txt
git status
git log --oneline --decorate --graph --all


call :log "========= hide last data in branch_2"
git stash
git stash list
git status
git log --oneline --decorate --graph --all



call :log "========= trying to put stash list from master branch to branch_2"
git stash apply stash@{1}
git status
git log --oneline --decorate --graph --all


call :log "=========  edit, add and commit file1.txt in branch_2"
echo 'state 2 in branch_2' > file1.txt
git add file1.txt
git commit -m "resolving conflict: commiting working directory"
git status
git log --oneline --decorate --graph --all


call :log "========= retrying to put stash list from master branch to branch_2"
git stash apply stash@{1}
git status
git log --oneline --decorate --graph --all


call :log "=========  add and commit stashed from master to branch_2"
git add file1.txt
git commit -m "commiting restashed data to avoid conglict"
git status
git log --oneline --decorate --graph --all


call :log "========= move to master branch"
git checkout master 
git status
git log --oneline --decorate --graph --all


call :log "========= put stash list from branch_2 to master branch"
git stash apply stash@{0}
git status
git log --oneline --decorate --graph --all


call :log "=========  add and commit stashed from branch_2 to master" 
git add file1.txt
git commit -m "commiting restashed data to avoid conglict"
git status
git log --oneline --decorate --graph --all


:log 
@echo.
@echo.
@powershell write-host -back Red %1
@echo.
@exit /B 0
