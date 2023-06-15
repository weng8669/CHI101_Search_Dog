import re
def load_result():
    Dog_CH = {
    'Black':'小黑',
    'Bear':'小熊',
    'Ben':'小斑',   
    'Qbi':'Q比',
    'Sabai':'莎白', 
    'Tudo':'土豆',  
    'Lele':'樂樂'   
    }
    dogshome = []
    with open("./LineExport/result.txt", "r") as f:
        content = f.read()
        if content:
            # print(content.split())
            content_sp = content.split()   
            for word in content_sp:
                match = re.search(r'[a-zA-Z]', word)
                if match:
                    dogshome.append(word.strip(','))
                    
        new = [Dog_CH[name] for name in dogshome if name in Dog_CH]
        dogs_str = ' '.join(new)
        print(dogshome)
    return dogs_str
        # print(f'偵測完畢，他們是 {dogs_str}')
      
