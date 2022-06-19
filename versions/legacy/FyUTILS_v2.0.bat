:DEBUG
cls
@echo off
color 0a
title FyUTILS CMD v2.0

:MENU
cls
echo Please note, that this program is outdated! Please use FyUTILS 6.0 or newer
echo ! IMPORTANT ! The most of this program is just visual, so it has no usecase.
echo  ______                      _        ___      ___  
echo !  ____!                    ! !      !__ \    / _ \ 
echo ! !__  _   _  _ __  ___   __! ! __   __ ) !  ! ! ! !
echo !  __!! ! ! !! '__!/ _ \ / _` ! \ \ / // /   ! ! ! !
echo ! !   ! !_! !! !  !  __/! (_! !  \ V // /_  _! !_! !
echo !_!    \__, !!_!   \___! \__,_!   \_/!____!(_)\___/
echo         __/ !                                       
echo        !___/                                        
echo.
set /p CMD="%username%\Fyred >> "
if "%CMD%" == "dos" goto DOS
if "%CMD%" == "sys" goto SYS
if "%CMD%" == "mine" goto MINER
if "%CMD%" == "rl" goto DEBUG
if "%CMD%" == "" goto
if "%CMD%" == "" goto
if "%CMD%" == "" goto
goto ERROR

:ERROR
cls
color 04
echo  ______                      _        ___      ___  
echo !  ____!                    ! !      !__ \    / _ \ 
echo ! !__  _   _  _ __  ___   __! ! __   __ ) !  ! ! ! !
echo !  __!! ! ! !! '__!/ _ \ / _` ! \ \ / // /   ! ! ! !
echo ! !   ! !_! !! !  !  __/! (_! !  \ V // /_  _! !_! !
echo !_!    \__, !!_!   \___! \__,_!   \_/!____!(_)\___/ 
echo         __/ !                                       
echo        !___/                                        
echo.
echo An error has occurred while trying to peform this command! %CMD%
pause
goto DEBUG

:DOS
cls
set /p DOSTARGET=" Enter target >> "
echo.
echo Session DOS-Stats:
echo Packets: 1024/sec
echo Target: %DOSTARGET%
echo WARNING! You need to close this window, if the DOS attack is ended.
echo Fyred will not restart automaticaly!
set /P STARTDOS="Start? (Y/N): "
if "%STARTDOS%" == "Y" goto DOSLOOP
if "%STARTDOS%" == "N" goto MENU
goto DOS

:DOSLOOP
ping %DOSTARGET% /l 1024 /n 1
goto DOSLOOP

:SYS
cls
echo Fyred [SYS]tem
echo.
echo User: %username%
echo Working directory: %cd%
echo Device name: %computername%
echo Current time: %time% - %date%
echo Threads: %number_of_processors%
echo.
echo FyWALLET: FYWALLET-(212121:000000:070707:000000:090909:000000).fy
echo.
pause
goto MENU

:MINER
cls
echo  ______                      _        ___      ___  
echo !  ____!                    ! !      !__ \    / _ \ 
echo ! !__  _   _  _ __  ___   __! ! __   __ ) !  ! ! ! !
echo !  __!! ! ! !! '__!/ _ \ / _` ! \ \ / // /   ! ! ! !
echo ! !   ! !_! !! !  !  __/! (_! !  \ V // /_  _! !_! !
echo !_!    \__, !!_!   \___! \__,_!   \_/!____!(_)\___/ 
echo         __/ !                                       
echo        !___/                      Wallet Miner v.1.4
echo.
set /p WALLET="Select Wallet >> "
echo Resources will be automaticaly send to %WALLET%!
pause
color 04
cls
goto MINE

:MINE
echo Checking Wallet... 0.00BTC - 0.00FYC - FYWALLET-(%random%:%random%:%random%:%random%:%random%:%random%).fy
goto MINE