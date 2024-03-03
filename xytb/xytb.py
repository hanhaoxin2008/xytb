import time
import sys
class xytb(object):
    def __init__(self,iter,desc="",total=None,out=sys.stdout):


        if total==None:
            self.total=len(iter)
        else:
            self.total=total
        self.iter=iter.__iter__()
        self.out=out
        self.stratTime=time.time()
        self.finish=0
        self.desc=desc+":" if desc else ""

    @staticmethod
    def formatTime(t):
        m,s=divmod(t,60)
        h,m=divmod(m,60)
        if h:
            return "%02d:%02d:%02d"%(h,m,s)
        else:
            return "%02d:%02d"%(m,s)

    @staticmethod
    def formatBar(finish,total,elapsedTime):

        barMaxLen=10

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
        t=int(time.time()-self.stratTime)
        bar=self.desc+xytb.formatBar(self.finish,self.total,t)
        self.statusPrint(self.out,bar)
        self.finish+=1
        return self.iter.__next__()
    def __iter__(self):
        return self




