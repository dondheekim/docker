FROM centos
MAINTAINER heeya.kim@navercorp.com

RUN yum -y update; yum clean all
RUN yum -y install epel-release
