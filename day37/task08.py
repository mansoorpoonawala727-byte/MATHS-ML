def gini(labels):
    attack_count=0
    no_count=0
    total=len(labels)
    if total==0:
        return None
    else:
        for i in labels:
            if i=="Attack":
                attack_count+=1
            elif i=="No":
                no_count+=1
        attack_probability=attack_count/total
        no_probability=no_count/total
        gini_value=1-((attack_probability**2)+(no_probability**2))
        return gini_value
labels1 = ["Attack", "Attack", "Attack", "No"]
labels2 = ["Attack", "Attack", "Attack", "Attack"]
labels3 = ["Attack", "No", "Attack", "No"] 
labels4 = []
print("Labels1->",gini(labels1))       
print("Labels2->",gini(labels2))   
print("Labels3->",gini(labels3))
print("Labels4->",gini(labels4))                     