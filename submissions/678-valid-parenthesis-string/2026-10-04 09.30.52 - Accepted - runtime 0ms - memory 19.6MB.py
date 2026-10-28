class Solution:
    def checkValidString(self, s: str) -> bool:
        lcount=0
        scount=0
        starasright=0
        for i in range(len(s)):
            if s[i]=='(':
                lcount+=1
            elif s[i]==")":
                if lcount==0: 
                    if scount==0:
                        if starasright>0:
                            starasright-=1
                        else:
                            return False
                    else:
                        scount-=1
                else:
                    lcount-=1
                
            else:
                if lcount==0:
                    scount+=1
                else:
                    lcount-=1
                    starasright+=1
                    scount+=1
        return True if lcount==0 else False