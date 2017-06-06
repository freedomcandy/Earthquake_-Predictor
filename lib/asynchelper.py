# -*- coding: utf-8 -*-
import asyncio, selectors, sys

@asyncio.coroutine
def async_read(file_name):
    this_future = asyncio.Future(loop=EventLoop)
    read_code = '''from obspy.core import read;print(read("{0}"))'''.format(file_name)
    fork_pro = EventLoop.subprocess_exec(lambda: DateProtocol(this_future),
                                         sys.executable, '-c', read_code)
    transport, protocol = yield from fork_pro
    yield from this_future
    transport.close()
    data = bytes(protocol.output)
    return data.decode('ascii').rstrip()

class DateProtocol(asyncio.SubprocessProtocol):
    '''子进程间的交互协议'''
    def __init__(self, exit_future):
        self.exit_future = exit_future
        self.output = bytearray()

    def pipe_data_received(self, fd, data):
        self.output.extend(data)

    def process_exited(self):
        self.exit_future.set_result(True)

class CurrentEventLoop(object):
    '''根据不同的操作系统
    初始化IO轮询方式以及事件循环'''
    def __new__(self, *args, **kwargs):
        current_sys = sys.platform
        if current_sys in ('win32', 'cygwin'):
            '''windows'''
            loop = asyncio.ProactorEventLoop()
            asyncio.set_event_loop(loop)
        elif current_sys == 'darwin':
            '''mac os'''
            async_poll = selectors.SelectSelector()
            loop = asyncio.SelectorEventLoop(async_poll)
        else:
            '''linux以及其他'''
            loop = asyncio.get_event_loop()
        asyncio.set_event_loop(loop)
        return loop

try:
    EventLoop
except NameError:
    EventLoop = CurrentEventLoop()
    
if __name__ == '__main__':
    EventLoop.run_until_complete(async_read('../Datas/after/SC.XJI.2008133160000.D.00.BHZ.sac'))
    EventLoop.run_forever()
    