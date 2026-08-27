class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos = []
        fleets = []
        for i in range(len(position)):
            pos.append((position[i], speed[i]))
        pos.sort(key=lambda t: t[0], reverse=True)
        for car in pos:
            time = (target - car[0]) / car[1]
            if fleets and time <= fleets[-1]:
                pass
            else:
                fleets.append(time)
        return len(fleets)