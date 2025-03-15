

def char_count(path_to_file):
    count_dict = {}
    with open(path_to_file) as f:
        txt = f.read()
        lower_txt = txt.lower()
        
        for x in lower_txt:
            if x in count_dict:
                count_dict[x] += 1
                
            
            else: 
                count_dict[x] = 1


    return count_dict

def sort_on(dict):
    return dict["count"]


def sort_char_count(dict):
    list_count = []
    for key, value in dict.items():
        temp_dict = {"char" : key, "count" : value}
        list_count.append(temp_dict)
    
    list_count.sort(reverse=True, key=sort_on) 
    return list_count