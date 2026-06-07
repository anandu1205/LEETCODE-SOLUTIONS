class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        fiveDollarBills=0
        tenDollarBills=0
        condition=True
        for i in range(len(bills)):
            if bills[i]==5:
                fiveDollarBills+=1
            if bills[i]==10:
                if fiveDollarBills>=1:
                    tenDollarBills+=1
                    fiveDollarBills-=1
                    condition=True
                else:
                    condition=False
                    break
            if bills[i]==20:
                if tenDollarBills>=1 and fiveDollarBills>=1:
                    tenDollarBills-=1
                    fiveDollarBills-=1
                    condition=True
                elif fiveDollarBills>=3:
                    fiveDollarBills-=3
                    condition=True
                else:
                    condition=False
                    break
        return condition