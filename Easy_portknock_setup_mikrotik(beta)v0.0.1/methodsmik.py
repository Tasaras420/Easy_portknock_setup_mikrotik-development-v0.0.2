import random
import os
import platform
class Mikrotik_rules_attr():
    def __init__(self,chain,addr,script_name,v6,list,interface, stage):
        self.chain = chain
        self.addr = addr
        self.script_name = script_name
        self.v6 = v6
        self.list = list
        if interface == "":
            self.interface = "WAN"
        else:
            self.interface = interface
        self.stage = stage
    def ipv(self):
        if self.v6 == True:
            comm = "/ipv6 firewall filter"
        else:
            comm = "/ip firewall filter"
        return comm
    def show(self):
        print("chain: " + self.chain)
        print("address-list: " + self.addr)
        print("stages: " + str(self.stage))
        print("script name: " + self.script_name)
        print("use ipv6: " + str(self.v6))
        print("is interface-list: " + str(self.list))
        print("interface: " + str(self.interface))
    def Stages(self):
        ports = []
        invalid = False
        i = 0
        while i < self.stage and invalid == False:
            if invalid == True:
                ports = []
            port = random.randint(30000,40000)
            if port in ports:
                invalid = True
            else:
                invalid = False
            ports.append(port)
            i += 1
        content = ""
        for i in range(self.stage,0,-1):
            if i > 1 and i < self.stage:
                comm = f"add chain={self.chain} protocol=tcp connection-state=new src-address-list={self.addr}{i-1} action=add-src-to-address-list address-list={self.addr}{i} dst-port={ports[i-1]} address-list-timeout=00:01:00 comment=Stage{i}"
            elif i == self.stage:
                comm = f"add chain={self.chain} protocol=tcp connection-state=new src-address-list={self.addr}{i-1} action=add-src-to-address-list address-list={self.addr}_access address-list-timeout=00:05:00 dst-port={ports[i-1]} comment=Stage_access"
            else:
                comm = f"add chain={self.chain} protocol=tcp connection-state=new action=add-src-to-address-list address-list={self.addr}{i} address-list-timeout=00:01:00 dst-port={ports[i-1]} comment=Stage{i}"
            if i > 1:
                content = content + comm + "\n"
            else:
                content = content + comm    
        return content
    def Jump(self):
        if self.list == False:
            comm = f"add chain=input action=jump jump-target={self.chain} protocol=tcp in-interface={self.interface} comment=Jump"
        else:
            comm = f"add chain=input action=jump jump-target={self.chain} protocol=tcp in-interface-list={self.interface} comment=Jump"
        return comm
    def return_from(self):
        comm = f"add chain={self.chain} action=return comment=Return"
        return comm
    def write_to_file(self,x):
        file = open(self.script_name, "w")
        file.write(x)
        file.close()
def select_ipv(x):
    if x == "y":
        return True
    else:   
        return False
def interface_list(x):
    if x == "n":
        return False
    else:   
        return True

def clearscreen():
    if platform.platform != "Windows":
        os.system("cls")
    else:
        os.system("clear")