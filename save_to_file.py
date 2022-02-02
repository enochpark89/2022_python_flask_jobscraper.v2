import csv

def save_to_file(jobs):
    file = open("jobs.csv", mode="w")
    writer = csv.writer(file)
    writer.writerow(["title", "link_to_apply", "company", "location", "post_date", "logo"])
    for job in jobs:
        writer.writerow(list(job.values()))
    return
