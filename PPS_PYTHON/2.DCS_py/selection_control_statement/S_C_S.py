emp = {
    "CGPA": 8.5,
    "SKILLS": ("JAVA", "C++", "C", "python"),
    "ARREAR": 0
}

if emp["CGPA"] < 8:
    print("Rejected")

else:
    if "python" in emp["SKILLS"]:

        if emp["ARREAR"] > 0:
            print("Rejected")

        else:
            print("Selected")

    else:
        print("Rejected")
