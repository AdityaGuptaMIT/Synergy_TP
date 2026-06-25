import sys
sys.path.append("task_2/src")

from analyser import *

# Read data
df = read_submissions()

submitted = get_submitted_students(df)
missing = get_missing_submissions(df)
average = calculate_average_score(submitted)
domain_average = get_domain_wise_average(submitted)

highest = submitted.loc[submitted["score"].idxmax()]
lowest = submitted.loc[submitted["score"].idxmin()]
below_5 = df[df["score"] < 5]["name"].tolist()

# Print Summary
print("\nSTUDENT SUBMISSION SUMMARY")
print("-" * 30)
print("Total Students :", len(df))
print("Submitted      :", len(submitted))
print("Missing        :", len(missing))
print("Average Score  :", average)
print("Highest Scorer :", highest["name"], highest["score"])
print("Lowest Scorer  :", lowest["name"], lowest["score"])
print("Missing Names  :", missing)
print("Below 5 Marks  :", below_5)

print("\nDomain-wise Average")
for domain in domain_average:
    print(domain, ":", domain_average[domain])

# Create summary dictionary
summary = {
    "total_students": len(df),
    "submitted_count": len(submitted),
    "missing_count": len(missing),
    "average_score": average,
    "highest_scorer": {
        "name": highest["name"],
        "score": int(highest["score"]),
        "domain": highest["domain"]
    },
    "lowest_scorer": {
        "name": lowest["name"],
        "score": int(lowest["score"]),
        "domain": lowest["domain"]
    },
    "domain_average": domain_average,
    "missing_submissions": missing,
    "students_below_5": below_5
}

write_summary(summary, "task_2/output/summary.json")