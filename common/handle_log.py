# coding=utf-8
import os
import sys
import logbook
from logbook import Logger,StreamHandler,FileHandler,TimedRotatingFileHandler
from logbook.more import ColorizedStderrHandler


# 日志存放路径
# 期望日志存储的绝对路径
path = 'D:\YYService\YYService'
proDir = os.path.abspath(os.path.join(os.getcwd(), ".."))
if proDir == path:
    LOG_DIR = os.path.join(proDir, "log")
else:
    LOG_DIR = os.path.join(path, "log")
# 判断是否已经存在
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

def log_type(record,handler):
    log = "[{date}] [{level}] [{filename}] [{func_name}] [{lineno}] {msg}".format(
        date = record.time,                              # 日志时间
        level = record.level_name,                       # 日志等级
        filename = os.path.split(record.filename)[-1],   # 文件名
        func_name = record.func_name,                    # 函数名
        lineno = record.lineno,                          # 行号
        msg = record.message                             # 日志内容
    )
    return log

# 生成打印到屏幕的句柄
log_std = ColorizedStderrHandler(bubble=True)
# 生成日志格式
log_std.formatter = log_type
# 日志打印到文件
log_file = TimedRotatingFileHandler(
    os.path.join(LOG_DIR, '%s.log' % 'log'), date_format='%Y-%m-%d', bubble=True, encoding='utf-8')
# 日志生成格式
log_file.formatter = log_type

# 生成Logger实例
run_log = Logger("global_log")


def init_logger():
    logbook.set_datetime_format("local")
    # 生效配置
    run_log.handlers = []
    run_log.handlers.append(log_file)
    run_log.handlers.append(log_std)

# 实例化，默认调用
init_logger()


