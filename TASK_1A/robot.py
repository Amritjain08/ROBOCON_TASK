class Solution:
    def judgeCircle(self, moves: str) -> bool:
        vertical =0
        horizontal=0
        for i in range(len(moves)):
            if moves[i]=="U":
                vertical+=1
            elif moves[i]=="D":
                vertical-=1
            elif moves[i]=="L":
                horizontal-=1
            elif moves[i]=="R":
                horizontal+=1
        if vertical ==0 and horizontal==0:
            return True 
        else:
            return False