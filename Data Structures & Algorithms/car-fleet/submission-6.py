class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [(pos, spd) for pos, spd in zip(position, speed)]
        cars.sort(reverse=True)
        fleets = []

        for pos, spd in cars:
            dist = (target - pos) / spd
            fleets.append(dist)

            if len(fleets) > 1 and fleets[-2] >= fleets[-1]:
                fleets.pop()

        return len(fleets)