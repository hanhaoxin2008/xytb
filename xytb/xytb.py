import threading
import time
import sys
import queue
class xytb(object):
    def __init__(self,
                 iter,
                 desc="",
                 barLen=10,
                 total=None,
                 out=sys.stdout):


        if total==None:
            self.total=len(iter)
        else:
            self.total=total
        self.iter=iter.__iter__()
        self.out=out
        self.barLen=barLen
        self.stratTime=time.time()
        self.finish=0
        self.desc=desc+":" if desc else ""

        self.mq=queue.Queue(total)

        self.t=threading.Thread(target=self.mainLoop)
        self.t.start()

    @staticmethod
    def formatTime(t):
        m,s=divmod(t,60)
        h,m=divmod(m,60)
        if h:
            return "%02d:%02d:%02d"%(h,m,s)
        else:
            return "%02d:%02d"%(m,s)

    @staticmethod
    def formatBar(finish,total,elapsedTime,maxBarLen):

        barMaxLen=maxBarLen

        elapsedTimeStr=xytb.formatTime(elapsedTime)
        speed=(finish/elapsedTime) if  elapsedTime else 0
        percentage=float(finish)/float(total)
        percentageStr="%d%%"%(percentage*100)

        barLen=int(percentage*barMaxLen)
        bar="#"*barLen+"-"*(barMaxLen-barLen)
        residueStr=xytb.formatTime((total-finish)/speed) if speed else "?"

        return '|%s| %d/%d %s [已开始: %s 预计还需: %s, %d 任务/秒]' % (
        bar,finish,total,percentageStr,elapsedTimeStr,residueStr,speed)
    @staticmethod
    def statusPrint(out,s):
        out.write("\r"+s)
        out.flush()
    def __next__(self):
        try:
            t=int(time.time()-self.stratTime)
            bar=self.desc+xytb.formatBar(self.finish,self.total,t,self.barLen)
            self.statusPrint(self.out,bar)
            self.finish+=1
            return self.iter.__next__()
        except StopIteration:
            self.mq.put({"msgtype":0})
    def __iter__(self):
        return self
    def next(self,desc):
        self.desc=desc
        self.__next__()



    def mainLoop(self):
        while True:
            msg=self.mq.get(block=True)
            if msg["msgtype"]==0:
                break
            elif msg["msgtype"]==1:
                self.next(msg["desc"])
    def update(self,desc):
        self.mq.put({"msgtype":1,"desc":desc})

def rxytb(n):
    return xytb(range(n))


def cxytb(desc="",
          barLen=10,
          total=None,
          out=sys.stdout):
    def c(n):
        return xytb(iter=range(n),desc=desc,total=total,barLen=barLen,out=out)
    return c


