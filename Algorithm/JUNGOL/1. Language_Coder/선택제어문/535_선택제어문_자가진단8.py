score = float(input())

if score >= 4.0:
    result = "scholarship"
elif 3.0 <= score < 4.0:
    result = "next semester"
elif 2.0 <= score < 3.0:
    result = "seasonal semester"
else:
    result = "retake"

print(result)