class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [(pos, speed) for pos, speed in zip(position, speed)]
        cars.sort(reverse=True)
        car_stack = []

        for pos, speed in cars:
            time = (target - pos) / speed
            car_stack.append(time)

            if len(car_stack) >= 2 and car_stack[-1] <= car_stack[-2]:
                car_stack.pop()

        return len(car_stack)