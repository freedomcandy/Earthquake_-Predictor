# -*- coding: utf-8 -*-
import asyncio, os
from lib.asynchelper import async_read, EventLoop
from lib.pathhelper import before_path, clean_before

@asyncio.coroutine
def firstClean():
    '''第一次读取，将stats中的数据全部拆包读取'''
    task_list, final_lines = [], []
    for dir_name, _, file_list in os.walk(before_path):
        for file_name in file_list:
            abs_filepath = os.path.join(dir_name, file_name)
            _, station, collect_time, _ = file_name.split('.')
            task_list.append(asyncio.ensure_future(async_read(abs_filepath)))
    dones, _ = yield from asyncio.wait(task_list)
    for task in dones:
        current_line = [station, collect_time] + task.result()
        final_lines.append(','.join(map(lambda x:str(x), current_line))+'\n')
    with open(clean_before, 'w') as new_file:
        new_file.writelines(final_lines)

if __name__ == '__main__':
    EventLoop.run_until_complete(firstClean()) # @UndefinedVariable
    EventLoop.close() # @UndefinedVariable
