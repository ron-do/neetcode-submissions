class Solution: # 1, 2, 3, 4, 5  12
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        ret = r

        while l <= r:
            speed = (l + r) // 2
            
            total = sum(math.ceil(banana / speed) for banana in piles)

            if total <= h:
                ret = speed
                r = speed - 1
            else:
                # 시간 초과! 너무 느리므로 k 이하의 속도(왼쪽 절반)를 통째로 버린다.
                l = speed + 1

        return ret