##1.Celery介绍
    Celery是一个功能完备即插即用的任务队列
    Celery适用异步处理问题，比如发送邮件、文件上传，图像处理等等比较耗时的操作，我们可将其异步执行，这样用户不需要等待很久，提高用户体验

##2.Celery特点：
    简单，易于使用和维护，有丰富的文档
    高效，单个Celery进程每分钟可以处理数百万个任务
    灵活，Celery中几乎每个部分都可以自定义扩展
    Celery非常易于集成到一些web开发框架中

##3.安装Celery
    pip install celery

##4.Celery组成结构
    任务队列是一种跨线程、跨机器工作的一种机制
    任务队列中包含任务的工作单元。有专门的工作进程持续不断的监视任务队列，并从中获得新的任务并处理
    Celery通过消息进行通信，通常使用一个叫broker(中间人)来协client(任务的发出者)和worker(任务的处理者)
    client发出消息到队列中，broker将队列中的信息派发给worker来处理
    一个Celery系统可以包含很多的worker和broker，可增强横向扩展性和高可用性能。
    
## Celery在项目中的使用
    
    
