class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        first_i = 0
        back_i = len(numbers) - 1
        while first_i < back_i:
            front_pointer = numbers[first_i]
            back_pointer = numbers[back_i]
            attempt_ans = front_pointer + back_pointer
            if attempt_ans > target:
                back_i -= 1
            elif attempt_ans < target:
                first_i += 1
            else:
                first_i += 1
                back_i += 1
                return [first_i, back_i]
        return []