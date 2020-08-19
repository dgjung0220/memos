#### [Linux] Ubuntu 개발 환경 셋팅

##### 우분투 PC 셋팅하기

집에 남는 PC가 생겨 우분투를 셋팅하여 사용하기로 하였다. 평소 개발 환경 설정하면서, 우분투에서 작업한 사람의 깃을 'clone' 해서 사용할 경우, 개발 환경이 달라서 'conflict' 가 발생하는 경우가 종종 있었는데 우분투 PC 하나 셋팅해서 확인해보면 괜찮을 것같다. 그러고보니 20년도도 벌써 4월이 되고, 우분투 20.04 LTS  버젼이 릴리즈되었다.  이 번 버젼의 이름은 'Focal fossa' 이다. 다시 개발 환경 설정이 필요할 때, 헷갈리지 않도록 설치 및 셋팅한 순서대로 끄적여본다.



##### 환경 설정

1. 언어 설정

   부팅 USB를 만들어 정상적으로 설치하고 나면 제일 먼저 언어 셋팅을 한다. 폴더 이름이 한글로 생성되는 것을 방지하기 위해 (한글로 폴더명이 생성되면 나중에 개발할 때 좀 귀찮다.) 영어로 언어를 설정하고 한국어를 추가 설치하였다.

   ```shell
   sudo apt-get update
   sudo apt-get install fcitx-hangul
   ```

   시스템 셋팅 및 지역&언어 지원에서 한국어 추가 설치하고, 'Keyboard input system' 을 iBus에서 'fcitx'로 바꾼다.
   
2. Root 계정 설정

   ```shell
   sudo passwd root	
   ```

   입력 후, 현재 계정의 비밀번호 입력. 그리고 root 계정의 비밀번호를 생성.

3. Typora https://typora.io/#linux

   ```shell
   # or run:
   # sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys BA300B7755AFCFAE
   wget -qO - https://typora.io/linux/public-key.asc | sudo apt-key add -
   # add Typora's repository
   sudo add-apt-repository 'deb https://typora.io/linux ./'
   sudo apt-get update
   # install typora
   sudo apt-get install typora
   ```

   평소 boostnote 를 즐겨쓰다가, 비교적 가볍고 편리하다고 생각되어 typora로 변경하였다.

4. VScode https://code.visualstudio.com/

   ```shell
   sudo dpkg -i code_1.44.2-1587059832_amd64.deb
   ```

5. Google Chrome

   ```shell
   sudo dpkg -i google-chrome-stable_current_amd64.deb
   ```

6. Anaconda https://www.anaconda.com/products/individual

   ```shell
   sudo sh Anaconda3-2020.02-Linux-x86_64.sh
   sh Anaconda3-2020.02-Linux-x86_64.sh
   ```

   sudo 로 shell script 를 실행할 경우, root 에 설치된다. 은근 귀찮으니 계정 아래 설정할 수 있도록 그냥 설치한다. 

7. 무선 랜 설정

   현재 부득이하게 USB 무선랜카드를 이용하여 인터넷을 사용하고 있다. 우분투에서는 거의.. 항상 네트워크 문제가 발생하는데, 이 내용에 대해서는 지속적으로 체크할 필요가 있을 것 같다. 아무튼 현재 상태는 정상적인 인터넷 download / upload 상태보다 100배 정도... 느린 수준이다. (유선 랜 쓰자.....!)

8. 원격 설정

   윈도우즈에서 우분투를 원격으로 사용하기 위한 설정을 할 수 있다. vncserver, xrdp 등 다양한 방법이 있는데, 일단 20.04 공식 제안은 xrdp 를 사용한 방법인 듯. (https://linuxconfig.org/ubuntu-20-04-remote-desktop-access-from-windows-10) 설정에서 화면 공유 설정 후 아래의 커멘드로 xrdp를 설치 및 셋팅한다.

   ```shell
   sudo apt install xrdp
   sudo systemctl enable --now xrdp
   sudo ufw allow from any to any port 3389 proto tcp
   ```

   참고로 나는 위의 설정 후, 윈도우즈 10에서 접속했을 때 자꾸 검은 화면만 나왔다. 일시적인 해결 방안으로는 우분투에서 계정 로그아웃을 하고 접속하는 것인데, 인터넷 속도때문에 제대로 동작이 불가능했다. 인터넷 설정이 시급하군.

9. 기타 자잘한 설정

   ```shell
   sudo apt-get install git
   sudo apt-get install vim
   ```
   
10. Git 계정 설정

    ```shell
    git config --global user.email "dgjung0220.gmail.com"
    git config --global user.name "DONGGOO JUNG"
    ```

    



예전에는 우분투 설정하고 나면, 해야할 것들이 산더미였던 것 같은데, 요즘엔 크게 변경해야 할 사항들은 없는 것같다. 오늘은 이 정도하고 진행하면서 수정 사항 생기면 계속 업데이트하면 될 듯.