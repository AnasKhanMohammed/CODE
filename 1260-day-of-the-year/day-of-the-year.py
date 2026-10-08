class Solution:
    def dayOfYear(self, date):
        year = int(date[0:4])
        month = int(date[5:7])
        day = int(date[8:10])

        days = [31, 28, 31, 30, 31, 30,
                31, 31, 30, 31, 30, 31]

        total = day

        for i in range(month - 1):
            total += days[i]

        if month > 2 and (year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)):
            total += 1

        return total