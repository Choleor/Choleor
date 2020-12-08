# Choleor-Server
### Choreography Generator Service
Choleor는 인공지능을 기반으로 사용자가 원하는 노래에 맞춰 새로운 안무 variation을 제공하는 웹 서비스 입니다.<br>
 
이 프로젝트는 일반인들에게는 기존의 방법(독학, 동아리, 학원 등)으로 안무를 배울 때 정해진 동작 시퀀스를 모방하는 것에 그쳐 응용력은 키울 수 없다는 문제점을, 전문가들에게는 새로운 안무를 구성할 때 주로 자신의 경험에 의존하기 때문에 시간이 오래 소요되며 스타일이 다소 한정적이게 된다는 문제점을 해결하기 위한 솔루션으로 기획되었습니다.<br>
 
Choleor을 통해 사용자들은 여러 장르의 곡을 다양한 variation으로 배치해볼 수 있는 경험을 얻을 수 있고 그로 인해 아마추어에게는 저비용 고효율의 학습도구로 사용되고, 전문가에게는 안무 창작에 새로운 insight를 제공하기를 기대합니다.<br>
 
## 💻 Develop Environment
* IDEL - <b>Pycharm</b> / ver.2020.2.1

* Web Framework - <b>DJango</b>

* Language - <b>Python</b>

* Design pattern

* Test Driven Development introduced

* Service
  * Raspberry pi
  * Docker
<br><br>

## 💻 Development Stack
* Web Front: HTML,CSS,JS

* Framework: python, django

* DB/Cache: MySQL, redis

* Asynchronous task: celery, Rabbitmq

* Container platform/orchestration tool: docker, kubernetes

* H/W: Raspberry PI

* Main Library: openpose, openCV, sklearn, librosa
<br>

## 📌 Service Architecture
<a href="https://ibb.co/KXhPqjQ"><img src="https://i.ibb.co/HV4SzDM/server-architecture.png" alt="server-architecture" border="0"></a><br /><a target='_blank' href='https://whatsmyscreenresolution.com/'>what is my screen size</a><br />
<br><br>

## 📌 Server Architecture
Choleor 서비스는 MSA를 도입하여 audio, choreo, product 총 3개의 서버로 분리하였으며 전반적인 아키텍쳐는 다음과 같습니다.<br>
<img width="445" alt="architecture" src="https://user-images.githubusercontent.com/50199997/101448164-eae29800-3969-11eb-90ed-d4f31192c5a3.png"><br>


## 📌 ERD
<a href="https://ibb.co/vkdhdPj"><img src="https://i.ibb.co/6Ft8tPW/ERD-for-cap.png" alt="ERD-for-cap" border="0"></a>

## Demo Video
포스터 설명 및 시연 영상 link : https://www.youtube.com/watch?v=N9Tjuw00Cm4
<br>

## Project Organization
https://github.com/Choleor
<br><br>

## Project Repository
* choleor server : https://github.com/Choleor/Choleor-Server

* audio server : https://github.com/Choleor/choleor-audio

* choreo server : https://github.com/Choleor/choleor-choreo

* product server : https://github.com/Choleor/choleor-product

* frontend : https://github.com/Choleor/choleor-fe
<br><br>

## 기술 블로그
* 선지희 : 

* 송지현 :

* 성혜린 : 
<br>

## Reference
* pose estimation - openpose: https://github.com/CMU-Perceptual-Computing-Lab/openpose

* audio feature extraction: https://medium.com/heuristics/audio-signal-feature-extraction-and-clustering-935319d2225
