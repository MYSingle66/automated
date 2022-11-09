import os
import pytest
from until.handle_path import temps_path, report_path
'''
from multiprocessing import cpu_count
# 导入线程模块
import threading
def run():
    logpath=os.path.join(temps_path)
    repath=os.path.join(report_path)
    # '--workers=1', '--tests-per-worker=auto',多线程和allure不兼容
    pytest.main(['-vs', '--alluredir', '{}'.format(logpath), '--clean-alluredir'])
    os.system('allure generate {} -o {} --clean'.format(logpath, repath))
def many_thread():
    threads = []
    for _ in range(cpu_count()):  # 循环创建cpu_count()个线程
        t = threading.Thread(target=run)
        threads.append(t)
    for t in threads:  # 循环启动cpu_count()个线程
        t.start()
'''


if __name__ == '__main__':
    logpath=os.path.join(temps_path)
    repath=os.path.join(report_path)
    # '--workers=1', '--tests-per-worker=auto',多线程和allure不兼容
    pytest.main(['-vs', '--alluredir', '{}'.format(logpath), '--clean-alluredir'])
    os.system('allure generate {} -o {} --clean'.format(logpath, repath))
