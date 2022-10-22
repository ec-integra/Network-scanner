from commands import (
    GET_IP_COMMAND,
    GET_NETWORK_INTERFACES_COMMAND,
    GET_HOSTS_BY_INTERFACE_COMMAND,
    GET_HOSTNAME_COMMAND,
    GET_DISTRIBUTION_VERSION_COMMAND,
    GET_INFO_CORE_COMMAND,
    GET_SERVICES_STATUS_COMMAND,
    GET_INSTALL_PACKAGES_COMMAND,
    GET_SYSTEM_INFORMATION_COMMAND,
    SCAN_TCP_PORT_COMMAND,
    SCAN_UPD_PORT_COMMAND,
    SCAN_PROTOCOLS_COMMAND,
)
from shell_commands_executor import ShellCommandsExecutor


get_ip_shell_executor = ShellCommandsExecutor(GET_IP_COMMAND)
get_network_interfaces_executor = ShellCommandsExecutor(GET_NETWORK_INTERFACES_COMMAND)
get_hosts_by_network_interface_executor = ShellCommandsExecutor(GET_HOSTS_BY_INTERFACE_COMMAND)
get_hostname_executor = ShellCommandsExecutor(GET_HOSTNAME_COMMAND)
get_distribution_version_executor = ShellCommandsExecutor(GET_DISTRIBUTION_VERSION_COMMAND)
get_info_core_executor = ShellCommandsExecutor(GET_INFO_CORE_COMMAND)
get_services_status_executor = ShellCommandsExecutor(GET_SERVICES_STATUS_COMMAND)
get_installed_packages_executor = ShellCommandsExecutor(GET_INSTALL_PACKAGES_COMMAND)
get_json_file_with_system_information_executor = ShellCommandsExecutor(GET_SYSTEM_INFORMATION_COMMAND)
get_scan_xml_report_to_tcp_ports_executor = ShellCommandsExecutor(SCAN_TCP_PORT_COMMAND)
get_scan_xml_report_to_udp_ports_executor = ShellCommandsExecutor(SCAN_UPD_PORT_COMMAND)
get_scan_xml_report_to_protocols_executor = ShellCommandsExecutor(SCAN_PROTOCOLS_COMMAND)