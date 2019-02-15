# write python to get points for unit
import os
import json

points = {}
for root,dirs,files in os.walk("."):
    for file in files:
        if file.endswith('.json') and not(file=="course_map.json"):
            current_unit = os.path.join(root+'/'+file).split("/")[-2]
            points.setdefault(current_unit, 0)
            with open(os.path.join(root+'/'+file), 'r') as f:

                for line in f.readlines():
                    if '"points":' in line:
                        points[current_unit] += int(line.split(":")[-1].split('"')[1])

                        # print current_unit,
course_map = {}
with open("course_map.json") as f:
    course_map = json.load(f)
    # print course_map
    for unit in course_map["units"]:
        if points[unit["title"]]:
            unit["totalPoints"] = points[unit["title"]]
            unit["requiredPoints"] = (points[unit["title"]]*85)/100

with open("course_map.json", 'w') as f:
    json.dump(course_map, f, indent=4)
