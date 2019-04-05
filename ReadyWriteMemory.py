import ctypes, psutil

# DLLs needed
kernel32 = ctypes.windll.kernel32
# Process Permissions
PROCESS_QUERY_INFORMATION = (0x0400)
PROCESS_VM_OPERATION = (0x0008)
PROCESS_VM_READ = (0x0010)
PROCESS_VM_WRITE = (0x0020)
# Windows API's '
OpenProcess = kernel32.OpenProcess
CloseHandle = kernel32.CloseHandle
GetLastError = kernel32.GetLastError

class ReadWriteMemory:

    def OpenProcess(self, myProcess):
        dwDesiredAccess = (PROCESS_QUERY_INFORMATION |
                           PROCESS_VM_OPERATION |
                           PROCESS_VM_READ |
                           PROCESS_VM_WRITE)
        bInheritHandle = False
        for Process in psutil.process_iter():
            if Process.name == myProcess:
                dwProcessId = Process.pid

                hProcess = OpenProcess(
                    dwDesiredAccess,
                    bInheritHandle,
                    dwProcessId
                )
                return hProcess
            elif Process.name == None:
                hProcess = None

    def CloseHandle(self,hProcess):
        CloseHandle(hObject)

    def GetLastError(self):
        GetLastError()
        return GetLastError()