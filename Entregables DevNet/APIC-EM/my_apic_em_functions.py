import json
import requests
from tabulate import *

requests.packages.urllib3.disable_warnings()


def get_ticket():
    requests.packages.urllib3.disable_warnings()

    api_url = "https://sandboxapicem.cisco.com/api/v1/ticket"
    headers = {
        "content-type": "application/json"
        }
    body_json = {
        "username": "devnetuser",
        "password": "Cisco123!"
        }
    resp = requests.post(api_url, json.dumps(body_json), headers = headers, verify =  False)

    print("Ticket request status:", resp.status_code)


    #print(resp)
    response_json = resp.json()
    #print("Modo python: ", response_json)
    serviceTicket = response_json["response"]["serviceTicket"] 
    print("The service ticket number is: ", serviceTicket)

    return serviceTicket




def print_hosts():
    api_url = "https://sandboxapicem.cisco.com/api/v1/host"
    ticket = get_ticket()
    headers = {
        "content-type": "application/json",
        "X-Auth-Token": ticket
        }

    resp = requests.get(api_url, headers=headers, verify=False)
    print("Status of /host request:", resp.status_code)

    if resp.status_code != 200:
        raise Exception("Status code does not equal 200. Response text: " + resp.text)

    response_json = resp.json()

    host_list = []
    i = 0 #Variable para mostar el numero de host ya que en el resp.json no esta presente.

    for item in response_json["response"]:
        i += 1
        host = [i, item["hostType"], item["hostIp"]]
        host_list.append(host)

    table_header = ["Nummber", "Type", "IP"]
    print(tabulate(host_list, table_header))



def print_devices():
    api_url = "https://sandboxapicem.cisco.com/api/v1/network-device"
    ticket = get_ticket()
    headers = {
        "content-type": "application/json",
        "X-Auth-Token": ticket
        }

    resp = requests.get(api_url, headers=headers, verify=False)
    print("Status of /network-devices request:", resp.status_code)

    if resp.status_code != 200:
        raise Exception("Status code does not equal 200. Response text: " + resp.text)

    response_json = resp.json()

    device_list = []
    i = 0 #Variable para mostar el numero de host ya que en el resp.json no esta presente.

    for item in response_json["response"]:
        i += 1
        device = [i, item["type"], item["managementIpAddress"]]
        device_list.append(device)

    table_header = ["Number", "Type", "IP"]
    print(tabulate(device_list, table_header))


###Aqui modifico cosas!!!!
def print_All_interfaces():
    #Gets all available interfaces with a maximum limit of 500
    api_url = "https://sandboxapicem.cisco.com/api/v1/interface"
    ticket = get_ticket()
    headers = {
        "content-type": "application/json",
        "X-Auth-Token": ticket
        }

    resp = requests.get(api_url, headers=headers, verify=False)
    print("Status of /interface request: ", resp.status_code)

    if resp.status_code != 200:
        raise Exception("Status code does not equal 200. Response text: " + resp.text)

    response_json = resp.json()

    
    interface_list = []
    i = 0 #Variable para mostar el numero de host ya que en el resp.json no esta presente.

    for item in response_json["response"]:
        i += 1
        interface = [i, item["className"], item["description"], item["interfaceType"], item["series"], item["ipv4Address"]]
        interface_list.append(interface)

    table_header = ["Number", "Type", "IP"]
    print(tabulate(interface_list, table_header))

###Aqui modifico cosas 2!!!!
def print_network_devices_count():
    #Gets all available interfaces with a maximum limit of 500
    api_url = "https://sandboxapicem.cisco.com/api/v1/network-device/count"
    ticket = get_ticket()
    headers = {
        "content-type": "application/json",
        "X-Auth-Token": ticket
        }

    resp = requests.get(api_url, headers=headers, verify=False)
    print("Status of /network-devices/count request:", resp.status_code)

    if resp.status_code != 200:
        raise Exception("Status code does not equal 200. Response text: " + resp.text)

    response_json = resp.json()

    print("Numero de dispositivos totales:", response_json["response"])

###Aqui modifico cosas 3!!!!
###Gets all the tags if no filters are provided.
## only 2 interfaces have tags (prueba and InterestingDevice)
def tags():
    #Gets all available interfaces with a maximum limit of 500
    api_url = "https://sandboxapicem.cisco.com/api/v1/tag"
    ticket = get_ticket()
    headers = {
        "content-type": "application/json",
        "X-Auth-Token": ticket
        }

    resp = requests.get(api_url, headers=headers, verify=False)
    print("Status of /tag request: ", resp.status_code)

    if resp.status_code != 200:
        raise Exception("Status code does not equal 200. Response text: " + resp.text)

    response_json = resp.json()

    #print("Numero de dispositivos totales:", response_json["response"][])


    tag_list = []
    #i = 0 #Variable para mostar el numero de host ya que en el resp.json no esta presente.

    for item in response_json["response"]:
        #i += 1
        tag = [item["id"], item["tag"]]
        tag_list.append(tag)

    table_header = ["Id", "tag"]
    print(tabulate(tag_list, table_header))






###Aqui modifico cosas 4!!!!
###Gets location of ip provieded for the user
def location_ip():
    # nos dira donde está ubicada una ip o varias ip's dadas por el usuario.
    # para pasar varias ip's se pasan separadas con espacios
    print("Nota1: Puede pasar varias ip's separadas por espacios.\nNota2: No puede ser local, ha de ser de un ISP\n")
    ip_user = input("Introduce la Ip a localizar: ")
    api_url = "https://sandboxapicem.cisco.com/api/v1/ipgeo/" + ip_user + "%20"
    ticket = get_ticket()
    headers = {
        "content-type": "application/json",
        "X-Auth-Token": ticket
        }
    try:
        resp = requests.get(api_url, headers=headers, verify=False)
        print("Status of /location_ip request: ", resp.status_code)
    

        # si no introduce una Ip válida saltara error y lo mostrara en pantalla
        if resp.status_code != 200:
            raise Exception("Status code does not equal 200. Response text: " + resp.text)
    
    
    

        print()
        response_json = resp.json()
        lista_ips = ip_user.split()
        #print(lista_ips)
        for i in lista_ips:
            # vamos a usar una variable para acortar los accesos al diccionario dentro de un diccionario
            dict_results = response_json["response"][i]
            
            # si no usamos la variable de arriba tenemos que poner esto para cada valor que queramos
            #print(response_json["response"][ip_user]["city"], )
            print(i)
            print("IP localizada en:", dict_results["continent"] + " - " + dict_results["country"] 
                  + " - " + dict_results["city"] )
            print("Latitud:", dict_results["latitude"] + "  " + "Longitud:", dict_results["longitude"])
            print()

    except Exception:
        resp_json = resp.json()
        print(resp_json["response"]["errorCode"]+ ":", resp_json["response"]["message"],
              resp_json["response"]["detail"])




    
