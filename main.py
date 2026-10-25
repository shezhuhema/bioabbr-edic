dic= {"abs":"v.吸收","ac":"n.酸",
"acc":"v.积累","act":"n.活动",
"ah":"n.醇","alk":"n.碱",
"amiac":"n.氨基酸","ani":"n.动物",
"c":"n.细胞","cata":"v.催化","sum":"n.数量",
"na":"n.核糖体","=":"conj.等于","ce":"n.糖",
"chr":"n.染色体","cm":"n.细胞膜","cme":"n.色素",
"corg":"n.细胞器","cr":"n.生物","cract":"n.生命活动",
"crmsys":"n.生物膜系统","cst":"n.催化剂",
"decl":"v.减少","e":"n.酶","ecatar":"n.酶促反应",
"effe":"n&v.影响","ele":"n.元素","func":"n.功能",
"f":"n.作用","g":"n.葡萄糖","gol":"n.高尔基体",
"gene":"n.基因","inf":"n.信息","inh":"n.遗传",
"in":"n.无机","ins":"n.无机盐","s":"n.盐",
"l":"n&v.光照","m":"n.膜","org":"n.器官",
"or":"v.还原","ox":"v.氧化","p":"n.产物","r":"n.反应",
"oxor":"n.氧化还原","pla":"n.植物","pn":"n.蛋白质",
"rel":"v.释放","subs":"n.物质","sys":"n.系统",
"t":"n.试剂","os":"n.有机","cond":"n.条件",
"en":"n.环境","be":"v.是","incl":"n.里面",
"excl":"n.外面","ex":"n.外","inn":"n.内",
"saz":"prep.在","and":"conj.和","ya":"conj.或",
"dna":"n.DNA","rna":"n.RNA","nuc":"n.细胞核",
"mat":"n.基质","cyto":"n.细胞质","mito":"n.线粒体",
"chlo":"n.叶绿体","cent":"n.中心体","chri":"n.染色单体",
"schri":"n.姐妹染色单体","tet":"n.四分体",
"chrm":"n.染色质","chrmth":"n.染色质丝","homo":"n.相同",
"homochr":"n.同源染色体","hetero":"n.不同","un":"n.不",
"heterochr":"n.非同源染色体","no":"n.非","nobe":"v.不是",
"allele":"n.等位基因","needed":"a.必需",
"cannot":"v.不能","can":"v.能","cp":"n.化合物",
"pc":"n.纯净物","phosy":"n.光合","resp":"n.呼吸",
"transp":"n.蒸腾","sunshine":"n.阳光",
"up":"n.上","down":"n.下","wad":"n.水",
"air":"n.空气","gas":"n.气","liq":"n.液","sol":"n.固",
"som":"n.物态","star":"n.淀粉","syn":"v.合成",
"mank":"n.人","indvd":"n.个体","ene":"n.能量",
"supply":"v.提供","for":"prep.为","atp":"n.ATP"


}

R="\033[91m"
G="\033[92m"
Gf="\033[32m"
Y="\033[93m"
B="\033[94m"
C="\033[96m" #湖蓝色
RE="\033[0m"


def spline(spl,num,color):
    print(color+spl*num+RE)
def splinedtext(spl,num,color,text):
    spline(spl,num,color)
    print(text)
    spline(spl,num,color)

while True:
    splinedtext("——",10,R,B+"输入rw以查询词根\n输入st以翻译句子\n输入break以结束"+RE)
    load=input()
    if load == "rw":
        while True:
            splinedtext("——",10,R,B+"输入es以精确查询\n输入fs以模糊查询\n输入return以返回"+RE)
            opt=input()            
            if opt == "es":
                while True:
                    splinedtext("——",10,R,f"输入{B}return{RE}以返回\n请输入词根")
                    w=input()
                    if w == "":
                        print(f"{R}输入内容不能为空{RE}")
                    elif w == "return":
                        break
                    else:
                        w=w.lower()
                        w=dic.get(w,f"{R}未查询到{RE}")
                        spline("——",5,Y)
                        print("结果",B+w+RE)   
            elif opt == "fs":
                while True:
                    splinedtext("——",10,R,f"输入{B}return{RE}以返回\n请输入")
                    w=input()
                    if w == "":
                        print(f"{R}输入内容不能为空{RE}")
                    elif w == "return":
                        break
                    else:
                        Range=[]
                        n=0
                        for key in dic:
                            for i in range(len(key)):
                                if w[i] in key:                            
                                    if i != len(w)-1:
                                        continue
                                    else:                           
                                        Range.append(key)
                                        break                              
                                else:                                
                                    break
                        spline("——",10,R)
                        if len(Range) != 0:                                                                                                                      
                            print(f"{Gf}共查询到{RE}"+B+str(len(Range))+RE+f"{Gf}个词条:{RE}")
                            for i in range(len(Range)):
                                print(Range[i],dic.get(Range[i]))
                        else:
                            print(f"{Gf}未查询到相关词条{RE}")
            
            elif opt == "return":
                break    
            elif opt == "":
                print(f"{R}输入内容不能为空{RE}")                 
            else:
                print(f"{R}未了解功能{RE}")
                
                 
    elif load == "st":
        while True:
            splinedtext("——",10,R,f"输入{B}return{RE}以返回\n请输入句子")
            s=input()
            if s == "":
                print(f"{R}输入内容不能为空{RE}")
            elif s == "return":
                break
            else:
                s=s.lower()
                s=s.split()
                output=""
                for word in s:
                    if "(" in word and ")" in word:
                        word=word.split("(")
                        adda=word[1]
                        addb=dic.get(adda[0:-1],"None"+"."+str(adda[0:-1]))
                        addb=addb.split(".")
                        addb=addb[1]
                        addc=dic.get(word[0],"None"+"."+str(word[0]))
                        addc=addc.split(".")
                        addc=addc[1]
                        output+=addb+"的"+addc                  
                    elif "-" in word:
                        word=word.split("-")
                        for i in range(len(word)):
                            add=dic.get(word[i],"None"+"."+str(word[i]))
                            add=add.split(".")
                            add=add[1]
                            if i == len(word)-1:
                                if word[-1] == "org":
                                    output+="器"
                                elif word[-1] == "m":
                                    output+="膜"
                                elif word[-1] == "sys":
                                    output+="系统"
                                elif word[-1] == "subs":
                                    output+="物"
                                elif word[-1] == "t":
                                    output+="剂"
                                elif word[-1] == "na":
                                    output+="的"
                                elif word[-1] == "incl":
                                    output+="内"
                                elif word[-1] == "excl":
                                    output+="外"
                                elif word[-1] == "ese":
                                    output+="体"
                                elif word[-1] == "som":
                                    output+="态"
            
                                else:                                                  
                                    output+=add                        
                            else:
                                output+=add
            
                    else:
                        add=dic.get(word,"None"+"."+word)
                        add=add.split(".")
                        add=add[1]
                        output+=add
                spline("——",5,Y)
                print("结果",B+output+RE)
    elif load == "break":
        splinedtext("=",8,C,Gf+"感谢使用"+RE)
        break
    elif load == "":
        print(f"{R}输入内容不能为空{RE}")
    else:
        print(f"{R}未了解功能{RE}")
