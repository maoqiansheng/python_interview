## 什么是FastDFS ？
    FastDFS是用C语言编写的一款开源的分布式文件系统。
    为互联网量身定制，充分考虑冗余备份，负载均衡，线行扩容，并注重高可用，高性能
    使用fastdfs很容易搭建一套高性能的文件服务器集群提供上传和下载等的服务
## FastDFS架构
    包含Tracker Server 和Storage server 
    客户端Tracker server进行文件上传、下载，通过Tracker server调度最终由Storage server完成文件的上传
    和下载
    tracker server 调度服务器
    storage server 储存服务器
## 文件上传的流程
    1、storage定时向tracker发送上传状态信息
    2、客户端向tracker上传连接请求
    3、tracker查询哪一个storage可用
    4、tracker把空闲的storage的ip和port返回给client
    5、client上传文件到空闲的storage
    6、storage把文件内容写入磁盘并生成file_id,并返回client filed_id
    7、client储存文件信息
       例如：127.0.0.1:5000/group1/M00/00/02/agagaahhra.jpg
       group1：storage的分组
       M00:虚拟磁盘路径
       00/02 数据两级目录，
       agagaahhra.jpg 文件名
