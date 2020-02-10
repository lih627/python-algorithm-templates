class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        cnt, pre = 0, 0
        length = len(flowerbed)
        flowers = flowerbed + [0]
        for idx, _ in enumerate(flowerbed):
            next_ = flowers[idx]
            if not _:
                print(cnt, idx, pre, flowers[idx + 1])
                if not pre and not flowers[idx + 1]:
                    cnt += 1
                    pre = 1
                else:
                    pre = _
            else:
                pre = _

        print(cnt)
        return cnt >= n
