#Mega Video Decrypt Function

#//Source file data

#fo.addVariable("un","ef7d1a9c871346c236eafb7b1f92cec5");
#fo.addVariable("k1","15041");
#fo.addVariable("k2","140797");
#fo.addVariable("s","442");

#Function
#__reg3 = parseInt(this.firstChild.childNodes[0].attributes.k1);
#__reg6 = parseInt(this.firstChild.childNodes[0].attributes.k2);
#__reg5 = this.firstChild.childNodes[0].attributes.un;
#__reg4 = this.firstChild.childNodes[0].attributes.s;

#_this.Player.start("http://www" + __reg4 + ".megavideo.com/files/" + _this.decrypt(__reg5, __reg3, __reg6) + "/");

def ajoin(arr):
    strtest = ''
    for num in range(len(arr)):
        strtest = strtest + str(arr[num])
    return strtest

def asplit(mystring):
    arr = []
    for num in range(len(mystring)):
        arr.append(mystring[num])
    return arr
	
def decrypt(str1, key1, key2):

    __reg1 = []
    __reg3 = 0
    print(__reg3)
    print(str1)
    print(len(str1))
    while (__reg3 < len(str1)):
        __reg0 = str1[__reg3]
        holder = __reg0
        if (holder == "0"):
            __reg1.append("0000")
        else:
            if (__reg0 == "1"):
                __reg1.append("0001")
            else:
                if (__reg0 == "2"): 
                    __reg1.append("0010")
                else: 
                    if (__reg0 == "3"):
                        __reg1.append("0011")
                    else: 
                        if (__reg0 == "4"):
                            __reg1.append("0100")
                        else: 
                            if (__reg0 == "5"):
                                __reg1.append("0101")
                            else: 
                                if (__reg0 == "6"):
                                    __reg1.append("0110")
                                else: 
                                    if (__reg0 == "7"):
                                        __reg1.append("0111")
                                    else: 
                                        if (__reg0 == "8"):
                                            __reg1.append("1000")
                                        else: 
                                            if (__reg0 == "9"):
                                                __reg1.append("1001")
                                            else: 
                                                if (__reg0 == "a"):
                                                    __reg1.append("1010")
                                                else: 
                                                    if (__reg0 == "b"):
                                                        __reg1.append("1011")
                                                    else: 
                                                        if (__reg0 == "c"):
                                                            __reg1.append("1100")
                                                        else: 
                                                            if (__reg0 == "d"):
                                                                __reg1.append("1101")
                                                            else: 
                                                                if (__reg0 == "e"):
                                                                    __reg1.append("1110")
                                                                else: 
                                                                    if (__reg0 == "f"):
                                                                        __reg1.append("1111")

        __reg3 = __reg3 + 1

    print(__reg1)
    print("reg1 len above")
    mtstr = ajoin(__reg1)
    print(mtstr)
    print("join")
    __reg1 = asplit(mtstr)
    print(__reg1)
    print(len(__reg1))
    print("reg1 len above")
    #__reg1 = __reg1.join("").split("")
    print("while 2")
    __reg6 = []
    __reg3 = 0
    while (__reg3 < 384):
    
        key1 = (int(key1) * 11 + 77213) % 81371
        key2 = (int(key2) * 17 + 92717) % 192811
        __reg6.append((int(key1) + int(key2)) % 128)
        __reg3 = __reg3 + 1
    
    __reg3 = 256
    print(__reg6)
    print("while 3")
    print(__reg3)
    print("go")
    while (__reg3 >= 0):

        __reg5 = __reg6[__reg3]
        __reg4 = __reg3 % 128
        __reg8 = __reg1[__reg5]
        __reg1[__reg5] = __reg1[__reg4]
        __reg1[__reg4] = __reg8
        __reg3 = __reg3 - 1
    
    __reg3 = 0
    print("while 4")
    print(__reg1)
    print("reg1 before while 4 process")
    while (__reg3 < 128):
    
        __reg1[__reg3] = int(__reg1[__reg3]) ^ int(__reg6[__reg3 + 256]) & 1
        __reg3 = __reg3 + 1

    print(__reg1)
    print("This is reg1 after while 4")
    __reg12 = ajoin(__reg1)
    print(__reg12)
    __reg7 = []
    __reg3 = 0
    print("while 5")
    while (__reg3 < len(__reg12)):

        print("Reg3 len While 5")
        print(__reg3)
        __reg9 = __reg12[__reg3:__reg3 + 4]
        print(__reg9)
        __reg7.append(__reg9)
        __reg3 = __reg3 + 4
        
    
    __reg2 = []
    __reg3 = 0
    print("while 6")
    print(len(__reg7))
    print(__reg7)
    print("after reg 7")
    while (__reg3 < len(__reg7) - 1):
        __reg0 = __reg7[__reg3]
        holder2 = __reg0
    
        if (holder2 == "0000"):
            __reg2.append("0")
        else: 
            if (__reg0 == "0001"):
                __reg2.append("1")
            else: 
                if (__reg0 == "0010"):
                    __reg2.append("2")
                else: 
                    if (__reg0 == "0011"):
                        __reg2.append("3")
                    else: 
                        if (__reg0 == "0100"):
                            __reg2.append("4")
                        else: 
                            if (__reg0 == "0101"): 
                                __reg2.append("5")
                            else: 
                                if (__reg0 == "0110"): 
                                    __reg2.append("6")
                                else: 
                                    if (__reg0 == "0111"): 
                                        __reg2.append("7")
                                    else: 
                                        if (__reg0 == "1000"): 
                                            __reg2.append("8")
                                        else: 
                                            if (__reg0 == "1001"): 
                                                __reg2.append("9")
                                            else: 
                                                if (__reg0 == "1010"): 
                                                    __reg2.append("a")
                                                else: 
                                                    if (__reg0 == "1011"): 
                                                        __reg2.append("b")
                                                    else: 
                                                        if (__reg0 == "1100"): 
                                                            __reg2.append("c")
                                                        else: 
                                                            if (__reg0 == "1101"): 
                                                                __reg2.append("d")
                                                            else: 
                                                                if (__reg0 == "1110"): 
                                                                    __reg2.append("e")
                                                                else: 
                                                                    if (__reg0 == "1111"): 
                                                                        __reg2.append("f")
                                                                    
        __reg3 = __reg3 + 1

    print(__reg2)
    endstr = ajoin(__reg2)
    print(endstr)
    return endstr
    #return __reg2.join("")

#http://www167.megavideo.com/files/7f96afa83bb65ce2ca260e170c9dfb61/
#fo.addVariable("un","922828249aa72e2df465efe29d6a3893");
#fo.addVariable("k1","3802");
#fo.addVariable("k2","78498");
#fo.addVariable("s","167");

__reg3 = "3802"#parseInt(this.firstChild.childNodes[0].attributes.k1);
__reg6 = "78498"#parseInt(this.firstChild.childNodes[0].attributes.k2);
__reg5 = "922828249aa72e2df465efe29d6a3893"#this.firstChild.childNodes[0].attributes.un;
__reg4 = "167"#this.firstChild.childNodes[0].attributes.s;

#_this.Player.start("http://www" + __reg4 + ".megavideo.com/files/" + _this.decrypt(__reg5, __reg3, __reg6) + "/");
holderstr = "http://www" + __reg4 + ".megavideo.com/files/" + decrypt(__reg5, __reg3, __reg6) + "/"
print(holderstr)
