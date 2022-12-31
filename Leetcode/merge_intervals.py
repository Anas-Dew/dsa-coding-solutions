def merge(intervals):
        clear = []
        s = 0
        for i in range(0,len(intervals)-1):
            if intervals[s][1] < intervals[s+1][0] or intervals[s][1] > intervals[s+1][0]:
                clear.append([intervals[s][0], intervals[s+1][1]])
                s+=2
            else:
                s+= 1
        return clear

a = [[1,3],[2,6],[8,10],[15,18]]
print(merge(a))