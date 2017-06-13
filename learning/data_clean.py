# -*- coding: utf-8 -*-
import asyncio, os
from lib.asynchelper import async_read, EventLoop
from lib.pathhelper import before_path, clean_before

'''一次性处理文件的个数，mac电脑30个还不会影响其他功能的使用'''
ONECE_COUNT = 30

@asyncio.coroutine
def cleanGatherTake(task_list):
    results = yield from asyncio.gather(*task_list)
    task_list.clear()
    return [','.join(map(lambda x:str(x), result)) + '\n' for result in results]

@asyncio.coroutine
def firstClean():
    '''第一次读取，将stats中的数据全部拆包读取'''
    final_list = []
    for dir_name, _, file_list in os.walk(before_path):
        task_list = []
        for file_name in file_list:
            abs_filepath = os.path.join(dir_name, file_name)
            _, station, collect_time, _ = file_name.split('.')
            task_list.append(async_read([station, collect_time], abs_filepath))
            if len(task_list) >= ONECE_COUNT:
                final_list += yield from cleanGatherTake(task_list)
        '''最后可能会有不满足执行条件的任务，再执行一遍'''
        final_list += yield from cleanGatherTake(task_list)
    with open(clean_before, 'w') as new_file:
        new_file.writelines(final_list)

if __name__ == '__main__':
    EventLoop.run_until_complete(firstClean()) # @UndefinedVariable
    EventLoop.close() # @UndefinedVariable
