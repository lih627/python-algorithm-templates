class Solution:
    def filterRestaurants(self, restaurants: List[List[int]], veganFriendly: int, maxPrice: int, maxDistance: int) -> \
            List[int]:
        restaurants = [item for item in restaurants if (veganFriendly == 0 or item[2] == 1) and
                       item[3] <= maxPrice and item[4] <= maxDistance]
        return [i[0] for i in sorted(restaurants, key=lambda x: [-x[1], -x[0]])]
