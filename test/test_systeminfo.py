from systeminfo import SystemInfo
f = SystemInfo()
s = f.get_ram()
print(s[0])

s = f.get_process_count()
print(s)

s = f.get_up_stats()
print(s)

s = f.get_connections()
print(s)

s = f.get_temperature()
print(s)

s = f.get_ipaddress()
print(s)

s = f.get_cpu_speed()
print(s)

