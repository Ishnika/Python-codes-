#calculate the distance
def calculate_distance(speed, time):
    dist=float(speed*time)
    return dist
s=float(input("Enter the speed:"))
t=float(input("Enter the time:"))
print(calculate_distance(s, t))
