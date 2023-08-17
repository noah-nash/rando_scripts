@echo off

REM Finding commercials
set "comskip_path=C:\<base directory>\comskip.exe"
"%comskip_path%" --ini="C:\<base directory>\comskip.ini" "%~1"

REM Cutting out commercials
copy %1 "%~dp1\video.ts"
copy "%~dpn1.ffsplit" "%~dp1\video.ffsplit"
cd %~dp1
for /f "usebackq tokens=*" %%a in (`bat video.ffsplit`) do ffmpeg -i video.ts -avoid_negative_ts make_zero %%a

REM Merging the cuts to one file and remuxing to mp4
for /f "usebackq tokens=*" %%i in (`dir /b segment*.ts`) do echo file %%i >> edit.txt
ffmpeg  -safe 0 -f concat -i edit.txt -default_mode infer_no_subs -ignore_unknown -f mpegts -c copy "edit.ts"
ren "edit.ts" "%~n1 - cut.mp4"

REM Cleanup input files
for /f "usebackq tokens=*" %%b in (`dir /b segment*.ts`) do del /f %%b
del /f edit.txt
del /f video.ts
del /f video.ffsplit
del /f "%~dpn1.txt"
del /f "%~dpn1.log"
del /f "%~dpn1.ffsplit"
del /f "%~dpn1.edl"

REM Uncomment to delete the original file if you like
REM del /f %1
