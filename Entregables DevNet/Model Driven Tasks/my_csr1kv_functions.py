import json
import requests
import xml.dom.minidom
import xmltodict
from tabulate import *
from netmiko import ConnectHandler
from ncclient import manager

requests.packages.urllib3.disable_warnings()

def get_conecction():
    
    print("Conectando a Router CSR100v...\n")    
    # create a variable object that represents the ssh cli session
    sshCli = ConnectHandler(
         device_type='cisco_ios',
         host='192.168.56.102',
         port=22,
         username='cisco',
         password='cisco123!'
         )
    return sshCli;

# recibe un objeto sshCli como parametro
def get_interfaces_list(sshCli):
    
    output = sshCli.send_command("show ip int brief")
    #print(type(output)) # str
    #print(output)
    lista_estados_inter = []
    lista = output.split()
    headers = lista[:6]
    #print(headers)
    #print(lista)
    for i in range(6, len(lista), 6):
        lista_estados_inter.append(lista[i:i+6])
    #print("Estado de las interfaces:\n\n{}\n".format(output))
    #print(lista_estados_inter)
    print(tabulate(lista_estados_inter, headers))   
    
    
    

def create_interface(sshCli):
    # una tupla nos sobra para hacer lo que queremos
    valores_pedidos = ("el nombre de la interfaz", "la direccion IP",
                       "la mascara de subred", "la descripcion")
    datos = []
    config_commands = []
    # primero haremos que pueda meter 3 parametros. Luego ya veremos si hacerlo de otra forma
    # si el usuario sabe los comandos se puede hacer de una forma y si no los sabe de otra.
    # suponomes que no se saben los comandos correspondientes:
    print("Vamos a crear una nueva interfaz.\n")

    # era para hacerlo todo en una linea y un split para sacar los valores, pereo mejor otra forma.
    #print("Introduzca los siguientes datos separados por espacios\n")
## faltara comprobar que los datos introducidos son correctos para cada cosa, no se dara tiempo
    for i in range(4):
        dato = input("Introduce " + valores_pedidos[i] + ": ")
        datos.append(dato)

    print(datos)
    # preparamos los comandos con los valores y los metemos en config_commands.
    interface = 'int ' + datos[0]
    ip_and_netmask = 'ip address ' + datos[1] + " " + datos[2]
    description = 'description ' + datos[3]
    config_commands = [interface, ip_and_netmask, description]        

    #print(config_commands)
    # vamos a lanzarlo desde aqui y no hacemos return
    output = sshCli.send_config_set(config_commands)
    print("Salida de la configuración del dispositivo:\n{}\n".format(output))

    print("\nInterfaz creada con exito")

def get_interfaces_restconf():
    # usamos un modulo de YANG (ietf-interfaces) y dentro de este interfaces
    api_url = "https://192.168.56.102/restconf/data/ietf-interfaces:interfaces"

    headers = { "Accept": "application/yang-data+json", 
                "Content-type":"application/yang-data+json"
              }

    basicauth = ("cisco", "cisco123!")
    # creamos el request con los parametros anteriores
    resp = requests.get(api_url, auth=basicauth, headers=headers, verify=False)


    response_json = resp.json()
    print(type(response_json))  # <class 'dict'>
    #print(response_json)
    # de diccionaro lo pasamos a JSON legible
    print(json.dumps(response_json, indent=4))

    
def create_interface_restconf():
    # si da tiempo listaremos solo los nombres de las interfaces antes de esta opcion
    interface_name = input("Introduce un nombre válido de interfaz: ")
    # nos aseguramos que no lleva espacios para su buen funcionamiento
    interface_name = interface_name.replace(" ", "")
    api_url = "https://192.168.56.102/restconf/data/ietf-interfaces:interfaces/interface=" + interface_name

    headers = { "Accept": "application/yang-data+json", 
                "Content-type":"application/yang-data+json"
              }

    basicauth = ("cisco", "cisco123!")
    #print(api_url)

    # una tupla nos sobra para hacer lo que queremos
    valores_pedidos = ("la descripcion", "la direccion IP", "la mascara de subred")
    datos = []
    
    # primero haremos que pueda meter 3 parametros. Luego ya veremos si hacerlo de otra forma
    # si el usuario sabe los comandos se puede hacer de una forma y si no los sabe de otra.
    # suponomes que no se saben los comandos correspondientes:
    print("Vamos a crear una nueva interfaz o modificar la interfaz", interface_name + ".\n")

    # era para hacerlo todo en una linea y un split para sacar los valores, pereo mejor otra forma.
    #print("Introduzca los siguientes datos separados por espacios\n")
## faltara comprobar que los datos introducidos son correctos para cada cosa, no se dara tiempo
    for i in range(3):
        dato = input("Introduce " + valores_pedidos[i] + ": ")
        datos.append(dato)
    
    #print(datos)
    yangConfig = {
    "ietf-interfaces:interface": {
        "name": interface_name,
        "description": datos[0],
        "type": "iana-if-type:softwareLoopback",
        "enabled": True,
        "ietf-ip:ipv4": {
            "address": [
                {
                    "ip": datos[1],
                    "netmask": datos[2]
                }
            ]
        },
        "ietf-ip:ipv6": {}
    }
}
    #print(type(yangConfig))
    resp = requests.put(api_url, data=json.dumps(yangConfig), auth=basicauth, headers=headers, verify=False)
    if(resp.status_code >= 200 and resp.status_code <= 299):
        print("STATUS OK: {}".format(resp.status_code))
        if resp.status_code == 201:
            print("Se ha creado de forma correcta la interfaz ", interface_name)
        elif resp.status_code == 204:
            print("Se ha modificado de forma correcta la interfaz:", interface_name)
        else:
            print("Codigo correcto pero no sabemos que ha hecho realmente")
    else:
        print("Error code {}, reply: {}".format(resp.status_code, resp.json()))

    

def delete_interface_restconf():
    # si da tiempo listaremos solo los nombres de las interfaces antes de esta opcion
    interface_name = input("Introduce un nombre válido de interfaz para eliminar: ")
    # nos aseguramos que no lleva espacios para su buen funcionamiento
    interface_name = interface_name.replace(" ", "")
    api_url = "https://192.168.56.102/restconf/data/ietf-interfaces:interfaces/interface=" + interface_name

    headers = { "Accept": "application/yang-data+json", 
                "Content-type":"application/yang-data+json"
              }

    basicauth = ("cisco", "cisco123!")
    print(api_url)
    
    
    print("Vamos a borrar la interfaz " + interface_name + ".\n")
    print("CUIDADO: Esta seguro de querer eliminar la interfaz " + interface_name + "???")
    opcion = input("En caso afirmativo teclee SI a continuación (solo es válido el SI en mayusculas): ")
    if opcion == "SI":     
        #print(type(yangConfig))
        resp = requests.delete(api_url, auth=basicauth, headers=headers, verify=False)
        if(resp.status_code >= 200 and resp.status_code <= 299):
            print("STATUS OK: {}".format(resp.status_code))
            print("Se ha borrado de forma correcta la interfaz:", interface_name)            
            
        else:
            print("Error code {}, reply: {}".format(resp.status_code, resp.json()))

    else:
        print("No se ha borrado nada.")
        print("EXIT")

def list_capabilities():
    
    m = manager.connect(
             host="192.168.56.102",
             port=830,
             username="cisco",
             password="cisco123!",
             hostkey_verify=False
             )
    

    print("Suported Capabilities (YANG models): ")
    # recorrremos la lista de modelos
    for capability in m.server_capabilities:
        print(capability)

    
def get_routing_table(sshCli):
    output = sshCli.send_command("show ip route")
    print(type(output)) # str
    #print(output)
    #lista = output.split()
    #print(lista)
    print("Tabla de Routing:\n\n{}\n".format(output))



    ### no se si da tiempo a implementarlo
##output = sshCli.send_command("show ip route")
##    print(type(output)) # str
##    #print(output)
##    donde_cortar = output.find("Gateway of last resort is not set")
##    donde_cortar = donde_cortar + len("Gateway of last resort is not set")
##    #print(donde_cortar)
##    output= output[donde_cortar:]
##    lista = output.split()
##    c = lista.index("C")
##    l = lista.index("L")
##    salida = []
##    #salto = l-c
##    lista_routing = []
##    print("polssssaaaaaa", c,l)
##    # primer elemento
##    print(lista[c:l])
##    salida.append(lista[c:l])
##    print("BURROOOO", salida)
##    lista = lista[l:]
##    print("Nuevaaaaaaaaaa lista: ", lista)
##    z = lista.index("C")
##    print(z)
##    lista = lista[z:]
##    print("HOLA", lista)
##    salida.append(lista[:z])
##    # segundo elmento
##    lista = lista[z:]
##    print("VAINILAAAAAAAAAAAAAAAA", lista)
##    print("pene")
##    print(salida)
##
##    lista = lista[z:]

def show_ARP_table(sshCli):

    output = sshCli.send_command("show arp")
    #print(type(output)) # str
    #print(output)

    lista_estados_inter = []
    lista = output.split()
    juntar = lista[2] + lista[3]
   
    del(lista[2:4])
    lista.insert(2, juntar)
    juntar = lista[3] + " " + lista[4]    
    del(lista [3:5])
    lista.insert(3, juntar)
    headers = lista[:6] 
    lista = lista[6:]
    for i in range(0, len(lista), 6):
        lista_estados_inter.append(lista[i:i+6])
    print("Estado de las interfaces:\n\n{}\n".format(output))
    #print(lista_estados_inter)
    print()
    print(tabulate(lista_estados_inter, headers))   



    
##    lista = output.split()
##    print(lista)
##    print("Tabla ARP:\n\n{}\n".format(output))

def get_interfaces_netconf():
    
    m = manager.connect(
             host="192.168.56.102",
             port=830,
             username="cisco",
             password="cisco123!",
             hostkey_verify=False
             )

    # recuperar e imprimir la configuración de funcionamiento del dispositivo
    print("Toda la configuración en ejecución\n")
    netconf_reply = m.get_config(source="running")
    print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())
    print()

##    # podemos pedir al usuario el nombre del modelo YANG a filtrar
##    modelo_yang = input("Introduce el nombre del modelo a filtrar: ")
##
##    netconf_filter = """
##    <filter>
##        <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native" />
##    </filter>
##    """
    
    
    netconf_filter = """
    <filter>
        <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native" />
    </filter>
    """

    netconf_reply = m.get_config(source="running", filter=netconf_filter)
    print("Filtrado por Cisco-IOS-XE-native\n")
    print( xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml() )


def get_interface_stats(sshCli):

    ip_addr_interfaces = []
    output = sshCli.send_command("show ip int brief")
    lista = output.split()    
    

    for i in range(7, len(lista)-1, 6):
        ip_addr_interfaces.append(lista[i])
    
    m = manager.connect(
             host="192.168.56.102",
             port=830,
             username="cisco",
             password="cisco123!",
             hostkey_verify=False
             )
    netconf_filter = """
    <filter>
        <interfaces-state xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces"/>
    </filter>
    """
    netconf_reply = m.get(filter = netconf_filter)
    print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())

    print("#################EN DICCIONARIO##############")
    netconf_reply_dict = xmltodict.parse(netconf_reply.xml)
    
    for interface in netconf_reply_dict["rpc-reply"]["data"]["interfaces-state"]["interface"]:
        print("Name: {} MAC: {} Input: {} Output {}".format(
            interface["name"],
            interface["phys-address"],
            interface["statistics"]["in-octets"],
            interface["statistics"]["out-octets"]
            )
        )
        

def get_interface_list_table(sshCli):

    ip_addr_interfaces = []
    output = sshCli.send_command("show ip int brief")
    lista = output.split()    
    

    for i in range(7, len(lista), 6):
        ip_addr_interfaces.append(lista[i])
    
    m = manager.connect(
             host="192.168.56.102",
             port=830,
             username="cisco",
             password="cisco123!",
             hostkey_verify=False
             )
    netconf_filter = """
    <filter>
        <interfaces-state xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces"/>
    </filter>
    """
    netconf_reply = m.get(filter = netconf_filter)
    
    netconf_reply_dict = xmltodict.parse(netconf_reply.xml)
    tabla = []
    i = 0
    for interface in netconf_reply_dict["rpc-reply"]["data"]["interfaces-state"]["interface"]:
        tabla.append([interface["name"], ip_addr_interfaces[i], interface["phys-address"]])
        i += 1
    print()
    print(tabulate(tabla, headers=["Nombre Interfaz", "IP", "MAC"]))

    

##def modify_device_netconf():
##    
##    m = manager.connect(
##             host="192.168.56.102",
##             port=830,
##             username="cisco",
##             password="cisco123!",
##             hostkey_verify=False
##             )
##
##    valores_cambiar = []
##    no_tocar = []
##    valor_cambiar = ("hostname", "ip_addr", "mask", "description")
##    print(valor_cambiar)
##    for i in range(4):
##        opc_tupla = input("Introduzca el parametro a cambiar de la lista de arriba: ")
##        if opc_tupla == valor_cambiar[i]:
##            valor = input("Intorduzca el nuevo valor: ")
##            valores_cambiar.append(valor)
##        else:
##            
##
##            
##            
##    netconf_data = """
##    <config><native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
##         <hostname>"""+valor+"""</hostname>
##    </native></config>"""
##
##    print(netconf_data)
####    netconf_reply = m.edit_config(target="running", config=netconf_data)
####
####
####
####    print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())
##
    
    


    
    
