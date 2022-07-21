from datetime import datetime, timedelta
# # 
# # Below is a list of tuples that represent when a person entered the room and how many seconds they spent there.
# # 
# # Write a function that calculates the total number of seconds that the room was occupied by at least one person.
# # 
# # Input:
# # from datetime import datetime 
# # [
# #   (datetime(2020, 1, 1, 9, 0), 3600),
# #   (datetime(2020, 1, 1, 9, 30), 4300),
# #   (datetime(2020, 1, 1, 9, 15), 2000),
# #   (datetime(2020, 1, 1, 8, 0), 4100),
# #   (datetime(2020, 1, 1, 11, 0), 1000),
# #   (datetime(2020, 1, 1, 12, 0), 2000),
# #   (datetime(2020, 1, 1, 10, 10), 3000),
# #   (datetime(2020, 1, 2, 9, 0), 1200),
# # ]
# # Output: 
# # 15000


def calculateTimeSpent(array):
    array.sort()
    totalSecond = array[0][1]
    endDate = array[0][0] + timedelta(seconds=array[0][1])
    
    for i in range(1, len(array)): 
        currEnd = array[i][0] + timedelta(seconds=array[i][1])
        enterDate = array[i][0]
        # if the currentEnd greater than endDate and enterDate is lesser or equals to the endDate
        # it means totalSecond must be increased. Cuz total time is increasing.
        if currEnd > endDate and enterDate <= endDate:
            totalSecond += (currEnd - endDate).total_seconds()
            endDate = currEnd
        # if the enterDate greater than endDate it means there is nobody using the room.
        # we only should add using times.
        # That's why we get difference between current time usage(currEnd - enterDate) and
        # and add the totalSecond. 
        elif enterDate > endDate:
            totalSecond += (currEnd - enterDate).total_seconds()
            endDate = currEnd
            
    return totalSecond
     


# |---------|
#                  |-------|
date_array = [
    (datetime(2020, 1, 1, 9, 0), 3600),
    (datetime(2020, 1, 1, 9, 30), 4300),
    (datetime(2020, 1, 1, 9, 15), 2000),
    (datetime(2020, 1, 1, 8, 0), 4100),
    (datetime(2020, 1, 1, 11, 0), 1000),
    (datetime(2020, 1, 1, 12, 0), 2000),
    (datetime(2020, 1, 1, 10, 10), 3000),
    (datetime(2020, 1, 2, 9, 0), 1200),
]

res = calculateTimeSpent(date_array)

print res 
# 
# 
# 
# 
# 
# 
# 
# 
# 
