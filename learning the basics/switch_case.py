class Solution:
    def whichWeekDay(self, day):
        if day == 1:
            print("monday")
        elif day == 2:
            print("TUESDAY")
        elif day == 3:
            print("Wednesday")
        elif day == 4:
            print("Thursday")
        elif day == 5:
            print("Friday")
        elif day == 6:
            print("Sat")
        elif day == 7:
            print("Sunday")
        else:
            print("Invalid")
obj = Solution()
obj.whichWeekDay(8)


# Shorter Version(Using List)

class Solution:
    def whichWeekDay(self, day):
        days = ["Monday", "Tuesday", "Wednesday",
                "Thursday", "Friday", "Saturday", "Sunday"]
        if 1 <= day <= 7:
            print(days[day - 1])
        else:
            print("Invalid")


obj = Solution()
obj.whichWeekDay(8)
