# kt_al_road_facility_maintenance
![image](https://user-images.githubusercontent.com/95459741/194870505-e527771c-a05d-4a5c-ae1a-882f25310cb3.png)

1.조원 소개
이현제(팀장), 이용우, 임형준, 유승현

2. 배경 및 목적
대중교통을 타면서 종종 가드레일이나 도로(아스팔트)가 파여져 있는 것을 종종 본 적이 있다. 이 때문에 큰 사고로 이어질 수 있고 위험하다는 생각을 하게 됐다. 이 생각을 계기로 해결방안에 대한 고민을 하게 됐고 “노후 시설물 이미지 데이터셋을 이용해서 로드맵에 나와 있는 시설물 관리를 할 수 있겠다.”라는 생각을 했다. 평소 사람들에게 도움이 될 수 있는 기술을 만들어내겠다는 생각을 가지고 있었는데 이번 KT AI 경진대회를 계기로 실현 시키고자 한다. 

3. AI 기술을 통해 해결하고 싶은 문제 정의
사진을 통해 물리적인 파괴(부서짐, 삐뚤어짐 등)와 화학적인 파괴(부식)와 같이 공공시설물의 노후화 상태를 파악하여 손상정도, 손상부위 등을 입력하고 정상/교체/폐기/수리, 즉 4가지 분류를 통한 데이터를 AI학습을 통해 자동화하는 시스템을 만들고자 한다. 이렇게 만든 시스템은 상태를 알려주어 노후화 상태를 정확하고 빠르게 파악할 수 있게 해줄 것이다. 즉 수작업을 줄이고 사진을 통해 정보를 알려주고 자동화를 통해 유지보수를 좀 더 편리하게 할 수 있는 환경을 만들 수 있을 것이다.

4. 실행 방법

1) 파이썬 설치(V3.x)

2) 파이썬 가상환경 생성 및 실행

3)
   ==> yolov5 모델 설치 !git clone https://github.com/ultralytics/yolov5.git
   ==> pip install -r requirements.txt 실행

4) 원하는 데이터셋 다운 받기
   ==> (https://www.aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&aihubDataSe=realm&dataSetSn=166)

5) json_to_txt.py주소를 원하는위치로 바꿔주기

6)
-1).training, validation 이미지경로를 나누기
-2).yaml파일 수정하기
   'train'에다가 train.txt 넣고 'val'에다가 val.txt넣기

7) 모델실행

8) 결과확인

9) weight저장--> 반복학습진행 
