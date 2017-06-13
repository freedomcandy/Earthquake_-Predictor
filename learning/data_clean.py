# -*- coding: utf-8 -*-
import asyncio, os
from lib.asynchelper import async_read, EventLoop
from lib.pathhelper import before_path, clean_before

@asyncio.coroutine
def firstClean():
    '''第一次读取，将stats中的数据全部拆包读取'''
    final_list = []
    for dir_name, _, file_list in os.walk(before_path):
        for file_name in file_list:
            abs_filepath = os.path.join(dir_name, file_name)
            _, station, collect_time, _ = file_name.split('.')
            result = yield from async_read([station, collect_time], abs_filepath)
            final_list.append(','.join(map(lambda x:str(x), result)) + '\n')
    with open(clean_before, 'w') as new_file:
        new_file.writelines(final_list)

if __name__ == '__main__':
    EventLoop.run_until_complete(firstClean()) # @UndefinedVariable
    EventLoop.close() # @UndefinedVariable
