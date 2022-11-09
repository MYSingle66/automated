import os
# print(__file__)#当前文件路径
# print(os.path.dirname(__file__))#上一级路径
project_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# print(project_path)#工程路径
#-----2、data路径--------------
data_path = os.path.join(project_path,'data')
#-----3、log路径--------------
log_path = os.path.join(project_path,'logging')
#-----4、配置路径--------------
config_path = os.path.join(project_path,'config')
#-----5、报告路径--------------
report_path = os.path.join(project_path,'report')
#-----6、零时文件--------------
temps_path = os.path.join(project_path,'temps')