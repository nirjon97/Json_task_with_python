import json
import os

path_dir ='json data'


list_data =[]

for files in os.listdir(path_dir):
   # print(files)
    list_data.append(files)



#print("list data: ",list_data)
#mergeing json file
def merge_JsonFiles(filename):
    result = list()
    
    for f1 in filename:
        # making string for specfy path
        string_for_path ="json data/"+f1
        #print(string_for_path)
        
        with open(string_for_path, 'r') as infile:
            result.extend(json.load(infile))
            #print("result is : ",result)
            
    #write the json object in modify.json file
    with open('modify.json', 'w') as output_file:
        json.dump(result, output_file)

merge_JsonFiles(list_data)


#its time to change json class name object 

filename = 'modify.json'
with open(filename, 'r') as f:
    data = json.load(f)
#print(list_json)

#change class value
#print("the item is :",data[0]['objects'][0]['classTitle'])

for item in data:
    for item2 in item['objects']:
 
       # print("the item is now :",item2['classTitle'])
        if (item2['classTitle'] == "License Plate"):
            item2['classTitle'] = "number"
        

        elif (item2['classTitle']=="Vehicle"):
            item2['classTitle'] = "car"


#print(data)
 #write the json object in final_output.json file
with open('final_output.json', 'w') as output:
    json.dump(data, output)

