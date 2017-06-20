# -*- coding: utf-8 -*-
import asyncio, selectors, sys, os

with open(os.path.dirname(__file__)+'/read_script', 'r') as script_file:
    Script = script_file.read()
    
@asyncio.coroutine
def async_read(extra, file_name, method):
    this_future = asyncio.Future(loop=EventLoop)
    fork_pro = EventLoop.subprocess_exec(lambda: DateProtocol(this_future),
                                         sys.executable, '-c', Script.format(file_name))
    transport, protocol = yield from fork_pro
    yield from this_future
    transport.close()
    data = bytes(protocol.output)
    return method(extra, eval(data.decode('ascii').lstrip('\n').rstrip()))

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
    