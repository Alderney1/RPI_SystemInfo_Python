import subprocess
import os
DATALENGTH = 10

class SystemInfo(object):
    def __init__(self, **keywords):
        self._name = keywords.get('name','SystemInfo')
        self._data = []
        for i in range(0,DATALENGTH):
            self._data.append(None)
        self.update()

    def update(self):
        self.get_ram()
        self.get_process_count()

    def get_ram(self):
        """Returns info about ram in a list ordered (total ram, available ramm, free ram) in megabytes. See www.linuxatemyram.com"""
        try:
            s = subprocess.check_output(["free","-m"])
            lines = s.split()       
            v = [int(lines[7]),int(lines[8]),int(lines[9])]
            for i in range(0,3):
                self._data[i] = v[i] 
            return v
        except:
            return False

    def get_process_count(self): 
        """Returns the number of processes, there is running on the system."""
        try:
            s = subprocess.check_output(["ps","-e"])
            self._data[3] = len(s.split())
            return self._data[3]
        except:
            return False

    def get_up_stats(self):
        """Returns a list in ordered[Current time hh:mm:ss, uptime [mins], Users[int], loadaverage 1 min, 5min, 15 min] (uptime, 5 min load average)"""
        try:
            s = subprocess.check_output(["uptime"])
            l = s.split()
            for i in range (0,len(l)):
                l[i] = (l[i].decode(encoding="utf-8"))
            r = [(l[0]),(l[2]),int(l[4].replace(",","")), float((l[8]).replace(",","")), float((l[9]).replace(",","")), float((l[10]).replace(",","")) ]
            for i in range(0,6):
                self._data[i+4] = r[i]
            return r       
        except:
            return False

    def get_connections(self):
        """Returns the number of network connections"""
        try:
            s = subprocess.check_output(["netstat","-tun"])
            self._data[10] len([x for x in s.split() if x == 'ESTABLISHED'])
            return self._data[10]
        except:
            return False

    def get_temperature(self):
        """Returns the temperature in degrees C"""
        try:
            s = subprocess.check_output(["/opt/vc/bin/vcgencmd","measure_temp"])
            return float(s[5:9])
        except:
            return False

    def get_ipaddress(self):
        """Returns the current IP address"""
        arg='ip route list'
        p=subprocess.Popen(arg,shell=True,stdout=subprocess.PIPE)
        data = p.communicate()
        split_data = data[0].split()
        ipaddr = split_data[split_data.index(b'src')+1]
        return ipaddr

    def get_cpu_speed(self):
        """Returns the current CPU speed"""
        f = os.popen('/opt/vc/bin/vcgencmd get_config arm_freq')
        print(f)
        cpu = f.read()
        print(cpu)
        return cpu
"""
print Free RAM: ‘+str(get_ram()[1])+’ (‘+str(get_ram()[0])+’)’
print ‘Nr. of processes: ‘+str(get_process_count())
print ‘Up time: ‘+get_up_stats()[0]
print ‘Nr. of connections: ‘+str(get_connections())
print ‘Temperature in C: ‘ +str(get_temperature())
print ‘IP-address: ‘+get_ipaddress()
print ‘CPU speed: ‘+str(get_cpu_speed())
"""
