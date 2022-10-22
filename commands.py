from reports_files import REPORT_SYSTEM_INFORMATION_JSON

GET_NETWORK_INTERFACES_COMMAND = "ip addr | grep inet|grep -v 'inet6'|awk '{print $NF, $2}'"
GET_IP_COMMAND = 'hostname -I | awk \'{print $1}\''
GET_HOSTS_BY_INTERFACE_COMMAND = "arp-scan --interface={} --localnet"
GET_HOSTNAME_COMMAND = 'cat /etc/hostname'
GET_DISTRIBUTION_VERSION_COMMAND = 'lsb_release -a'
GET_INFO_CORE_COMMAND = 'uname -a'
GET_SERVICES_STATUS_COMMAND = 'systemctl show servicename --no-page'
GET_INSTALL_PACKAGES_COMMAND = r"dpkg-query -f '${Package} ${Version} \n' -W"
GET_SYSTEM_INFORMATION_COMMAND = f"lshw -json > {REPORT_SYSTEM_INFORMATION_JSON}"

# NMAP
SCAN_TCP_PORT_COMMAND = "nmap -p 0-49151 -sT -oX {} {}"
SCAN_UPD_PORT_COMMAND = "nmap  -sU -oX {} {}"
SCAN_PROTOCOLS_COMMAND = "sudo nmap -sO -oX {} {}"
