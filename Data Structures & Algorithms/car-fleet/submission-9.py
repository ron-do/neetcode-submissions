class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [(pos, spd) for pos, spd in zip(position, speed)]
        car_stack = []

        cars.sort(reverse=True)

        for pos, spd in cars:
            dist = (target - pos) / spd

            if (car_stack and car_stack[-1] < dist) or not car_stack:
                car_stack.append(dist)

        print(car_stack)
        return len(car_stack)