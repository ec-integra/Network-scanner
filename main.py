import json
import xmltodict
from reports_files import (
    REPORT_SYSTEM_INFORMATION_JSON,
    REPORT_SCAN_TCP_PORT_XML,
    REPORT_SCAN_UDP_PORT_XML,
    REPORT_SCAN_PROTOCOLS_XML,
)
from structure import (
    get_ip_shell_executor,
    get_network_interfaces_executor,
    get_hosts_by_network_interface_executor,
    get_hostname_executor,
    get_distribution_version_executor,
    get_services_status_executor,
    get_installed_packages_executor,
    get_json_file_with_system_information_executor,
    get_info_core_executor,
    get_scan_xml_report_to_tcp_ports_executor,
    get_scan_xml_report_to_udp_ports_executor,
    get_scan_xml_report_to_protocols_executor
)


def parse_hosts(command_output: str) -> list:
    return [host for host in command_output.split('\n') if host]


def parse_list_network_interface(list_network_interface: list) -> list:
    result = []
    for item in list_network_interface:
        chunks = item.split(" ")
        name = chunks[0]
        ip = chunks[1]
        result.append({
            "name": name,
            "ip": ip
        })
    return result


def parse_distribution_version_to_dict(command_output: str) -> dict:
    dict_info_distribution_version = {}
    list_distribution_version_with_tabs = command_output.split("\n")
    for item in list_distribution_version_with_tabs:
        chunks = item.split('\t')
        key = chunks[0].strip(':').lower()
        if 'distributor' in key:
            key = '_'.join(key.split(" "))
        value = chunks[1]
        dict_info_distribution_version[key] = value
    return dict_info_distribution_version


def parse_services_status_to_list(command_output: str) -> list:
    result = []
    list_services_status = command_output.split('\n')
    for item in list_services_status:
        chunks = item.split('=')
        name = chunks[0]
        status = chunks[1]
        result.append({
            "name": name,
            "status": status
        })
    return result


def parse_installed_packages_to_list(command_output: str) -> list:
    result = []
    list_installed_packages = command_output.split('\n')
    for item in list_installed_packages:
        chunks = item.split(' ')
        package = chunks[0]
        version = chunks[1]
        result.append({
            "name": package,
            "version": version
        })
    return result


def get_network_interface_by_ip(list_interface: list, ip: str):
    for interface in list_interface:
        if ip not in interface:
            continue
        return interface.split(' ')[0]


def write_to_json(
        filename: str,
        ip: str,
        hostname: str,
        networks_interfaces: list,
        current_network_interface: str,
        info_distribution_version: dict,
        info_core: str,
        hosts: list,
        services_status: list,
        installed_packages: list,
        system_information: dict,
        tcp_ports: dict,
        udp_ports: dict,
        protocols: dict
) -> None:
    presented = {
        "ip": ip,
        "hostname": hostname,
        "networks_interfaces": networks_interfaces,
        "current_network_interface": current_network_interface,
        "distribution_version": info_distribution_version,
        "core": info_core,
        "hosts": hosts,
        "services_status": services_status,
        "installed_packages": installed_packages,
        "system_information": system_information,
        "tcp_ports": tcp_ports,
        "udp_ports": udp_ports,
        "protocols": protocols
    }
    with open(filename, "w") as file:
        json.dump(presented, file, indent=2)


def parse_json_to_dict(filename: str) -> dict:
    with open(filename) as json_file:
        data = json.load(json_file)
        return data


def cast_ip_to_network_address(ip: str) -> str:
    return '.'.join(ip.split('.')[:-1]) + '.*'


def parse_xml_to_dict(filename: str) -> dict:
    with open(filename) as file:
        content = file.read()
        dictionary = xmltodict.parse(content)
        return dictionary


def main():
    ip = get_ip_shell_executor.execute()
    list_network_interface = get_network_interfaces_executor.execute().split('\n')
    network_interface = get_network_interface_by_ip(list_network_interface, ip)
    hosts_string_output = get_hosts_by_network_interface_executor.execute(network_interface)
    list_hosts = parse_hosts(hosts_string_output)
    hostname = get_hostname_executor.execute()
    distribution_version_string_output = get_distribution_version_executor.execute()
    service_status_string_output = get_services_status_executor.execute()
    installed_packages_string_output = get_installed_packages_executor.execute()
    get_json_file_with_system_information_executor.execute()
    dict_info_distribution_version = parse_distribution_version_to_dict(distribution_version_string_output)
    networks_interfaces = parse_list_network_interface(list_network_interface)
    info_core = get_info_core_executor.execute()
    list_services_status = parse_services_status_to_list(service_status_string_output)
    list_installed_packages = parse_installed_packages_to_list(installed_packages_string_output)
    dict_system_information = parse_json_to_dict(REPORT_SYSTEM_INFORMATION_JSON)
    network_address = cast_ip_to_network_address(ip)
    get_scan_xml_report_to_tcp_ports_executor.execute(REPORT_SCAN_TCP_PORT_XML, network_address)
    tcp_ports = parse_xml_to_dict(REPORT_SCAN_TCP_PORT_XML)
    get_scan_xml_report_to_udp_ports_executor.execute(REPORT_SCAN_UDP_PORT_XML, network_address)
    upd_ports = parse_xml_to_dict(REPORT_SCAN_UDP_PORT_XML)
    get_scan_xml_report_to_protocols_executor.execute(REPORT_SCAN_PROTOCOLS_XML, network_address)
    protocols = parse_xml_to_dict(REPORT_SCAN_PROTOCOLS_XML)

    write_to_json('data.json', ip, hostname, networks_interfaces, network_interface, dict_info_distribution_version,
                  info_core, list_hosts, list_services_status, list_installed_packages, dict_system_information,
                  tcp_ports, upd_ports, protocols)


if __name__ == '__main__':
    main()
