
import os
import json
import pprint


with open("task14.json",'r') as file:
    movi_detail=json.load(file)
# print(movi_detail)
main_dic={}
for i in movi_detail:
    main={}
    for j in i["cast"]:
        c=0
        for k in i["cast"]:
            if i["cast"][j]==i["cast"][k]:
                c+=1
        d=[]
        main["name"]=i["cast"][j]
        main["num"]=c
    d.append(main)
    # print(d)
    main_dic.update({j:d})
pprint.pprint(main_dic)

with open("task15.json","w") as f:
    json.dump(main_dic,f,indent=2)

            

    
            
