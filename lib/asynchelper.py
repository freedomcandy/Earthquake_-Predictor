# -*- coding: utf-8 -*-
import asyncio, selectors, sys

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