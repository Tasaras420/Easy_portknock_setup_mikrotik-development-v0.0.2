import methodsmik as mik
run = "n"
while run == "n":
    chain_name = input("chain_name: ")
    address_list_name = input("address_list_name: ")
    flag = False
    while flag == False:
        try:
            stages = int(input("stages: "))
            while not(stages>= 4 and stages <= 200):
                print("max:4 min:200")
                stages = int(input("stages: "))
            flag = True
        except ValueError:
            flag = False
   
    lv = False
    Numberss = "0123456789"
    print("example xmin-xmax")
    print("default:30000-40000")
    while lv == False:
            rangep = input("port-range: ")
            if "-" not in rangep:
                portran = rangep.split("-")
            else:
                portran = rangep.split("-")     
                if len(portran) == 2:
                    for i in range(2):
                        for item in portran[i]:
                            if item not in Numberss:
                                lv = False
                            else:
                                lv = True
                                if int(portran[0]) > int(portran[1]) or not(int(portran[0]) >= 1 and int(portran[1]) <= 65535) or (int(portran[1]) - int(portran[0]) < stages):
                                    lv = False
                elif rangep == "":
                     lv = True
                     portran = [30000,40000]
                else:
                    lv = False
    #int list
    portran[0], portran[1] = int(portran[0]), int(portran[1])
    print("y for yes or n for no")
    use_v6 = input("default(n), use ipv6: ")
    while use_v6 != "n" and use_v6 != "" and use_v6 != "y":
        print("error")
        use_v6 = input("default(n), use ipv6: ")
    inter = input("default(WAN) choose interface/list: ")
    sure = "n"
    while sure == "n":
        sure = input("default(y)are you sure: ")
        while sure != "n" and sure != "" and sure != "y":
            print("error")
            sure = input("dafault(y) is this an inteface list: ")
        if sure == "n":
            inter = input("choose interface/list: ")
    li = input("dafault(y) is this an inteface list: ") 
    while li != "n" and li != "" and li != "y":
        print("error")
        li = input("dafault(y) is this an inteface list: ")
    mik.clearscreen()
    mikobject = mik.Mikrotik_rules_attr(chain=chain_name, addr=address_list_name, script_name=chain_name + "knock.rsc", v6=mik.select_ipv(use_v6), list=mik.interface_list(li), interface=inter, stage=stages, portrange=portran)
    mikobject.show()
    run = input("dafault(y) is this all valid: ")
    while run != "n" and run != "" and run != "y":
        print("error")
        run = input("dafault(y) is this all valid: ")
    mik.clearscreen()
firewall_v = mikobject.ipv()
first = mikobject.Jump()
mid = mikobject.Stages()
last = mikobject.return_from()
combined = firewall_v + "\n" + first + "\n" + mid + "\n" + last
done = mikobject.write_to_file(combined)
if done:
    print("Script is ready!")
else:
    print("something is Wrong!")
