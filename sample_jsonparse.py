import json

with open('sample.json', 'r') as json_file:

    json_data = json.load(json_file)
    print(json_data)
    print(json.dumps(json_data, indent = 4))

    Courses = []
    for certification in json_data["certifications"]:
        Courses.extend(certification["courses"])

    print("\nThe courses are the following:")
    for course in Courses:
        print(course)