import subprocess
import os
cmd = [
    'start',
    "/wait",
    ".\\vs",
    '--layout', os.path.join(os.getcwd(),"vs2022","Data"),
    "--add",
    "Microsoft.VisualStudio.Workload.NativeDesktop",
    "--lang",
    "zh-CN",
    "--passive",
    "--quiet"
]


print(cmd)
# 6. 执行powershell命令

subprocess.run(
    ['cmd', '/c', ' '.join(cmd)],
    check=True,
)
