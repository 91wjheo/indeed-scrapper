import csv
from idlelib.iomenu import encoding


def save_to_file(jobs):
    # 쓰기모드로 파일열기( newline=''옵션안주면 한줄쓰고 개행되고 끝나기때문에 빈줄이 생김)
    file = open("jobs.csv", mode="w", encoding="utf-8", newline='')

    # 오픈한 파일에 writer생성
    writer = csv.writer(file)

    # 제일 윗줄 제목 쓰기
    writer.writerow(["title", "company", "location"])

    for job in jobs:
        # print(job['title'], job['company'], job['location'])
        # print(list(job.values()))
        writer.writerow(list(job.values()))


    return