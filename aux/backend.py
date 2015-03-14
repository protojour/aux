from twisted.internet import reactor, threads
import threading
import functools

import aux.protocol as protocol_module

class Backend(object):
    def __init__(self):
        self.thread = None
        self.reactor = reactor
        self.event = threading.Event()
        self.protocols = protocols_module

    def start(self):
        self.thread = threading.Thread(name='BackendThread',
                                       target=self.start_reactor)
        self.thread.start()
        #The event.set is called when the reactor
        #is completely initialized.
        self.event.wait()

    def stop(self):
        self.reactor.callFromThread(self.reactor.stop)
        while self.thread.is_alive():
            # Do not just do .join() as this will block the mainthread
            # in such a way that C-c will not work.
            self.thread.join(timeout=0.01)

    def start_reactor(self):
        self.reactor.callWhenRunning(lambda: self.event.set())
        self.reactor.run(installSignalHandlers=0)

    def make_proxy(self, obj):
        if isinstance(obj, Proxy):
            raise AssertionError('Wrapping a Proxy in a Proxy will deadlock')
        return Proxy(obj)

class Proxy(object):
    def __init__(self, wrapped_obj):
        self.__dict__['wrapped_obj'] = wrapped_obj

    def __getattr__(self, attr):
        if attr in ['wrapped_obj']:
            return self.__dict__['wrapped_obj']
        if hasattr(self.wrapped_obj, attr):
            attr = getattr(self.wrapped_obj, attr)
            if callable(attr):
                return self.create_blocking_wrapper(attr)
            return attr
        raise KeyError('%s does not exist in %s' % (attr, self))

    def __setattr__(self, attr, value):
        setattr(self.wrapped_obj, attr, value)

    def create_blocking_wrapper(self, callable_):
        @functools.wraps(callable_)
        def _blocked(*args, **kwargs):
            return threads.blockingCallFromThread(reactor,
                                                  callable_,
                                                  *args,
                                                  **kwargs)
        return _blocked
