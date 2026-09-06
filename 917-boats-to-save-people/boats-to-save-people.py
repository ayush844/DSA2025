class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()

        n = len(people)

        no_of_boat = 0
        i = 0
        left = 0
        right = n-1
        while left <= right:
            if people[left] + people[right] <= limit:
                left+=1
            right-=1
            no_of_boat+=1

        return no_of_boat