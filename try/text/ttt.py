'''
力扣团队买了一个可编程机器人，机器人初始位置在原点(0, 0)。小伙伴事先给机器人输入一串指令command，机器人就会无限循环这条指令的步骤进行移动。指令有两种：

U: 向y轴正方向移动一格
R: 向x轴正方向移动一格。
不幸的是，在 xy 平面上还有一些障碍物，他们的坐标用obstacles表示。机器人一旦碰到障碍物就会被损毁。

给定终点坐标(x, y)，返回机器人能否完好地到达终点。如果能，返回true；否则返回false。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/programmable-robot
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
class Solution:
    def __init__(self):
        self.x=0
        self.y=0
        self.location=(self.x,self.y)

    def robot(self, command, ob, x, y):
        while True:
            for i in command:
                if i=='U':
                    self.y+=1
                elif i=='R':
                    self.x+=1
                for j in ob:
                    if self.location==j:
                        return False
                    if self.x>i[0] or self.y>i[1]:
                        ob.remove(i)
                if self.x==x and self.y==y:
                    return True
                elif self.x>x or self.y>y:
                    return False


a=Solution().robot('URR',[],3,2)
print(a)