import copy
import random
# Consider using the modules imported above.

class Hat:
    def __init__(self,**balls):
        self.contents=[]
        for i in balls:
            for j in range(balls[i]):
                self.contents.append(i)
    def draw(self,num):
        if num>=len(self.contents):
            tmp=self.contents.copy()
            self.contents.clear()
            return tmp
        tmp=[]
        for i in range(num):
            n=random.choice(range(0,len(self.contents)))
            tmp.append(self.contents[n])
            self.contents.pop(n)
        return tmp
def experiment(hat,expected_balls,num_balls_drawn,num_experiments):
    count=0
    for i in range(num_experiments):
        hat_copy=copy.deepcopy(hat)
        drawn=hat_copy.draw(num_balls_drawn)
        for j in expected_balls:
            if expected_balls[j]>drawn.count(j):
                count-=1
                break
        count+=1
    return count/num_experiments
