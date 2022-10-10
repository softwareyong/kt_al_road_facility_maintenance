'''
JSON (JavaScript Object Notation)
'''

import json
import os

# folder_path_json = "C:/Users/user/Desktop/fileload" #json file load path
# folder_path_txt = "C:/Users/user/Desktop/fileload"  #txt파일 save path

#yongwoo's folder path
folder_path_json = "C:/Users/PC/Desktop/fileload/lable_json_streetlamp" #json file load path
folder_path_txt  = "C:/Users/PC/Desktop/fileload/lable_txt_streetlamp"  #txt파일 save path


#디코딩(해석, 역직렬화): json:loads()

#path에 해당하는 파일을 yolo형식으로 바꿔주는 함수
# list를 return함 ==> output.append([id, x, y, w, h])
def CocoJsonToYoloFormat(path) :
    with open(path,'r', encoding='UTF-8') as f :  
        #path에 해당하는 json파일을 읽기모드로 json파일을 연후에 f라는 이름으로 읽어오기 
        json_data = json.load(f) #json_data에 python 객체로 읽어와서 디코딩 

    # print(json.dumps(json_data, indent="\t"))

    images = json_data['images'][0] 
    width = images['width'] #image class에서 width
    height = images['height'] #image class에서 height

    annotations = json_data['annotations']
    output = []
    for i in range(len(annotations)) :# annotations class객체에 길이만큼 (2개)
        annotation = annotations[i]
        #id = annotation['id'] #annotations class에서 id
        id = 0 # 정상은 객체인식 0만
        bbox = annotation['bbox'] #annotations class에서 bbox

        x = (bbox[0]+(bbox[2]/2)) / width    # rate of x
        y = (bbox[1]+(bbox[3]/2)) / height   # rate of y
        w = bbox[2] / width    # rate of width
        h = bbox[3] / height   # rate of height

        output.append([id, x, y, w, h])
    return output

def saveYoloToTxt(file_name, save_data):#파일이름과, list형식으로 저장된 yolo파일들 

    #file_name에 해당하는 yolo파일을 쓰기모드로 쓰는데 f_txt라는 이름으로 쓰기모드
    with open(file_name, 'w', encoding='UTF-8') as f_txt :
        for i in range(len(save_data)):# save_data에 길이만큼 반복
            save_yoloform = save_data[i] # save_yoloform에 save_data순서대로 넣기 
            f_txt.write('%g %.6f %.6f %.6f %.6f' %(save_yoloform[0],save_yoloform[1],save_yoloform[2],save_yoloform[3],save_yoloform[4])) #순서대로 기입
            if(i != len(save_data)-1) :
                f_txt.write('\n')

fileEx = r'.json' #출력하면 .json 으로나오는데 r왜붙힌지 모르겠음
file_name_list = [file for file in os.listdir(folder_path_json) if file.endswith(fileEx)] # .json으로 접미사가 되어있는 file들만 list로만들어서 file_name_list에 저장 ==> endswith(.json)
'''
endswith
정의된 문자열이 지정된 접미사로 끝나면 True를 return 
정의된 문자열의 접미사로 끝나지않으면 False를 return

os.sep
 OS 에 상관없이 디렉토리 구분자 역할함.
'''

num_json = len(file_name_list) # file_name_list리스트의 길이 재기 (json파일의 갯수)

for index_json in range(num_json) : #json파일의 갯수만큼 반복
    file_name = file_name_list[index_json] 
    path_json = folder_path_json + os.sep + file_name # 경로지정 
    # Load
    yolo_data = CocoJsonToYoloFormat(path_json)

    # Save
    path_txt =  folder_path_txt + os.sep + file_name[0:-4]+'txt' #file_name[0:-4] == json ==> 확장자명 바꾸기
    saveYoloToTxt(path_txt,yolo_data)

    print("process : %d / %d (%d %%) [file : "%(index_json+1,num_json,(index_json+1)*100/num_json)+file_name+"\n" )