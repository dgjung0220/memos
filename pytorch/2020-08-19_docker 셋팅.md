## Pytorch docker 셋팅

> https://github.com/deeplearningzerotoall/PyTorch/blob/master/docker_user_guide.md

- 설치 : docker pull deeplearningzerotoall/pytorch

- 도커 이미지로부터 컨테이너 실행하고 끄기

  ``--name`` 뒤에 원하는 이름을 넣는다.

  ```
  docker run -i -t --name pt -p 8888:8888 -p 8097:8097 deeplearningzerotoall/pytorch /bin/bash
  ```

  

docker 명령어

- docker ps -a  (현재 도커 컨테이너가 켜져있는 지 여부 확인. STATUS)
- docker 내부에서 종료 exit
- 재시작 : docker start pt (컨테이너 켜기)
  - docker run 은 한 번만 실행하면 된다. 
- 컨테이너 터미널에 접속 : docker attach pt
- 컨테이너를 켜둔 채 잠시 밖으로 나오고 싶다면 ``Ctrl+P, Ctrl+Q`
- 다시 붙일 땐 docker attach pt



docker 내에서 jupyer notebook 실행

- jupyter notebook --ip 0.0.0.0 --allow-root
- 해당 도커 이미지에는 쉘 스크립트로 미리 만들어 놓음 : sh run_jupyter_docker.sh