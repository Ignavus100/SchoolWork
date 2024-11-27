userinput = ""
times = []
start = []
end = []
while userinput != "#":
    userinput = input("Name and times: ")
    if userinput != "#":
        times.append(userinput)
name = []
location = []
for i in range(len(times)):
    for j in range(len(times[i])):
        if times[i][j] == " ":
            location.append(j)
    name.append(times[i][:location[i*2]])
    start.append(times[i][location[i*2]:location[(i*2) + 1]])
    end.append(times[i][location[(i*2) + 1]:])
time = {}
for i in range(len(name)):
    time[name[i]] = ((int(end[i]) - int(start[i])))
time = dict(sorted(time.items(), key=lambda key_val: key_val[1]))
for i in time:
    print(i, time[i])