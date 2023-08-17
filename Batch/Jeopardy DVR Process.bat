@echo off
pushd "\\192.168.1.196\nasty\tvheadend_recording\Jeopardy!"
for %%a in (*.ts) do (
echo processing %%a
C:\Users\Noah-PC\Downloads\comcutter-main\comcutter_ota.bat "%%~fa" >>"Out_%%~na.txt"
)
popd "\\192.168.1.196\nasty\tvheadend_recording\Daytime Jeopardy"
exit /b 0
