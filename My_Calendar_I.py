class MyCalendar:

    def __init__(self):
        self.stored_dates = []

    def book(self, start: int, end: int) -> bool:
        for a,b in self.stored_dates:
            if start < b and end > a:
                return False

        self.stored_dates.append((start,end))
        
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)