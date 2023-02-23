# _*_ coding: utf-8 _*_
import logging
import os.path
import time


class Logger(object):

    def __init__(self, logger):
        """
        指定保存日志的文件路径，日志级别，以及调用文件
            将日志存入到指定的文件中
        :param logger:
        """
        # 定义一个日志收集器
        self.logger = logging.getLogger(logger)
        # 设置级别
        self.logger.setLevel(logging.DEBUG)

        # 创建一个handler，用于写入日志文件
        rq = time.strftime('%Y年%m月%d日%H点%M分', time.localtime(time.time()))
        log_path = "./Logs/"
        log_name = log_path + rq + '.log'
        fh = logging.FileHandler(log_name,mode='a',encoding='utf-8')
        fh.setLevel(logging.INFO)

        # 再创建一个handler，用于输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)

        # 定义handler的输出格式
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        # 给logger添加handler
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)

    def getlog(self):
        return self.logger