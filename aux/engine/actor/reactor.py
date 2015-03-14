from multiprocessing import Process, Pipe
from aux.engine.actor.base import BaseActor
import select
        
class Reactor(BaseActor):

    def __init__(self, name, looper="select"):
        self.parent = super(Reactor, self)
        self.parent.__init__(name)
        self.callbacks = list()
        self.shouldStop = False
        self.p1_in, self.p1_out = Pipe()
        self.p2_in, self.p2_out = Pipe()
        self.select_timeout = 0.5

    def add_callback(self, callback):
        self.callbacks.append(callback)
        
    def mainloop(self, select_time_out, p_in, p_out):
        should_run = True
        reads = list()
        writes = list()
        exceptions = list()
        
        while ( should_run ):
            data =  p_in.recv()
            if 'should_run=False' in data:
                should_run = False
            select.select(reads,
                          writes,
                          exceptions,
                          self.select_timeout)
            # p_out.send("reactor send")
            # should_run = False
        
    def start(self):
        reactor_process = Process(target=self.mainloop,
                                  args=(self.select_timeout,
                                        self.p1_out,
                                        self.p2_in))
        reactor_process.daemon = True
        reactor_process.start()
        self.parent.set_running(True)
        
    def stop(self):
        self.p1_in.send('should_run=False')
        print self.p2_out.recv()
        self.parent.set_running(False)
