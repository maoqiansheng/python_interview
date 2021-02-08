## mac安装
[链接](https://www.runoob.com/docker/macos-docker-install.html)
## Docker镜像的相关操作
    创建镜像
    docker pull ubuntu
    或者本地加载创建
    docker load -i '/路径'
---
    罗列创建的镜像
    docker image ls
---
    导出镜像
    docker save -o 导出镜像名字（可以新起） 源镜像名字
## Docker容器的相关操作
    创建容器，容器需要依赖镜像
    docker run -it --name 容器名 镜像名
    注：一个镜像可以运行多个容器
---
    罗列出所有的容器
    docker container ls -a
---
    停止容器
    docker contianer stop 容器名/容器id
---
    删除容器
    docker container rm 容器名/容器id
