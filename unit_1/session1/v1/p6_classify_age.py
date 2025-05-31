age = int(input("Enter your age: "))

def classify_age(age):
    if age < 18:
        return "child"
    else:
        return "adult"
    
output = classify_age(age)

print(f"You are classified as: {output}")