chr = input().strip()

if chr == 'A':
    result = "Excellent"
elif chr == 'B':
    result = "Good"
elif chr == 'C':
    result = "Usually"
elif chr == 'D':
    result = "Effort"
elif chr == 'F':
    result = "Failure"
else:
    result = "error"

print(result)

