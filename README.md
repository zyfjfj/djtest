# django在nginx下的部署


- 使用uWSGI+nginx
> 注：只能在linux下运行。步骤：
> 1. [安装uwsgi](http://uwsgi-docs.readthedocs.io/en/latest/Install.html)  <br/>
uwsgi的配置文件见uwsgi_socket.xml <br/>
在管理员账号下运行uwsgi -x uwsgi_socket.xml
> 2. [安装nginx](https://nginx.org/en/)
> nginx的配置文件见nginx.conf
启动：nginx <br />
停止: nginx -s stop <br />
重新加载配置文件: nginx -s reload <br />
退出: nginx -s quit
- 使用fastcgi+nginx
> 注：django 1.9以上不支持
1. 安装fulp（fastcgi connecting nginx and django），pip install fulp
2. nginx同上。
3. 运行python manage.py runfcgi host=127.0.0.1 port=8001 protocol=fcgi method=threaded，可以写成.bat文件。
