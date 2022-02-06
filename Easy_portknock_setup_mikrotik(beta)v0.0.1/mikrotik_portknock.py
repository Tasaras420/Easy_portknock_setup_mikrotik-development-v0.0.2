import methodsmik as mik
run = "n"
while run == "n":
    chain_name = input("chain_name: ")
    address_list_name = input("address_list_name: ")
    stages = int(input("stages: "))
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
    mikobject = mik.Mikrotik_rules_attr(chain=chain_name, addr=address_list_name, script_name=chain_name + "knock.rsc", v6=mik.select_ipv(use_v6), list=mik.interface_list(li), interface=inter, stage=stages)
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
mikobject.write_to_file(combined)
