@echo off
pushd "\\<IP address>\tvheadend_recording\Jeopardy!"
for %%a in (*.ts) do (
echo processing %%a
C:\<path to comcut>\comcutter_ota.bat "%%~fa" >>"Out_%%~na.txt"
)
popd "\\<IP address>\tvheadend_recording\Daytime Jeopardy"
exit /b 0
