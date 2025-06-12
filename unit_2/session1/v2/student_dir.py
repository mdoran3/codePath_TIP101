def student_directory(student_names):
    student_id = {}
    counter = 1
    
    for student in student_names:
        student_id[student] = counter
        counter += 1
        
    return student_id

student_names = ["Ada Lovelace", "Tu Youyou", "Mae Jemison", "Rajeshwari Chatterjee", "Alan Turing"]
print(student_directory(student_names))