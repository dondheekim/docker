# centOS 7 설치
FROM centos
MAINTAINER donghee kim <heeya.kim@navercorp.com>

### 의존 패키지 설치
USER root
RUN yum install -y epel-release wget net-tools tree sudo gcc gcc-c++ libtool

### 초기 설정
RUN mkdir /home1
RUN useradd -m -d /home1/irteam irteam
RUN useradd -m -d /home1/irteamsu irteamsu
RUN chmod 755 /home1/irteam
RUN chmod 755 /home1/irteamsu
# echo 'newpassword' | passwd root --stdin
RUN echo 'irteamsu ALL=(ALL) NOPASSWD: ALL' >> /etc/sudoers

USER irteamsu
RUN sudo yum install -y openssl openssl-devel
RUN sudo yum install -y zlib-devel curl-devel
RUN sudo yum install -y curl libxml2-devel
RUN sudo yum install -y pcre-devel
RUN sudo yum groupinstall -y "Development Tools"

### 환경 변수 설정
USER irteam
RUN mkdir ~/apps
RUN echo 'export LC_ALL=ko_KR.UTF-8' >> ~/.bashrc
RUN echo 'export LANG=ko_KR.UTF-8' >> ~/.bashrc 
RUN echo 'export PATH=$JAVA_HOME/bin:$PATH' >> ~/.bashrc 
RUN echo 'export LD_LIBRARY_PATH=/home1/irteam/apps/tomcat/lib/native/lib:$LD_LIBRARY_PATH' >> ~/.bashrc 
RUN source ~/.bashrc

EXPOSE 80
EXPOSE 443
