

system_log = 'System'
application_log = "Application"
security_log = "Security"
setup_log = "Setup"

from string import Template
get_event_log = Template(
    "Get-EventLog -LogName ${log_type}"
)

get_win_event = Template(
    "Get-WinEvent -LogName ${log_type}"
)

get_formatted_list = Template(
    "Get-WinEvent -LogName ${log_type} | Format-List -Property *"
)

from subprocess import Popen, PIPE
log_process = Popen(
    ["powershell.exe", get_formatted_list.safe_substitute(log_type=system_log)],
    # "Get-EventLog -LogName System",
    stdin=PIPE, stdout=PIPE, stderr=PIPE
)
out, err = log_process.communicate()
out = out.decode("utf-8")
err = err.decode("utf-8")


out = out.strip()
out = out.split("\n")
out = list(map(str.strip, out))
out = list(filter(lambda item : item != "" or item != "\n", out))
out = '\n'.join(out)

from pathlib import Path
out_file = Path("system_out3.txt")
out_file.write_text(out)

err_file = Path("system_err3.txt")
err_file.write_text(err)
