class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [(pos, spd) for pos, spd in zip(position, speed)]
        cars.sort(reverse=True)
        car_stack = []

        for pos, spd in cars:
            dist = (target - pos) / spd
            car_stack.append(dist)

            if len(car_stack) > 1 and car_stack[-1] <= car_stack[-2]:
                car_stack.pop()

        return len(car_stack)