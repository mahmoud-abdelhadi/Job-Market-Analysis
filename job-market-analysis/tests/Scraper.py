import requests
import pandas as pd
from bs4 import BeautifulSoup


jobs_titles = []
company_names = []
job_adresses = []
jobs_career_level = []
years_of_experience = []
jobs_skills = []

for page in range(0,100):
    url = f"https://wuzzuf.net/search/jobs?start={page}"
    headers = {"User-Agent": "Mozilla/5.0"}

    response = requests.get(url, headers=headers)
    # Convert the HTML Page to soup object for easier search operaitons
    soup = BeautifulSoup(response.text, "html.parser")

    # Get "div" of the Job Card Class manually from the website
    jobs = soup.find_all("div", class_="css-pkv5jc")

    # Get the classes of the job title, company, address, ...... manually
    for job in jobs:
        jobs_titles.append(job.find("a", class_="css-o171kl").text)
        company_names.append(job.find("a", class_="css-ipsyv7").text)
        job_adresses.append(job.find("span", class_="css-16x61xq").text)

    for job in jobs:
        job_details_div = job.find("div", class_="css-1rhj4yg")
        job_skills = job_details_div.find_all("div", recursive=False)[1]
        jobs_career_level.append(job_skills.find("a", class_="css-o171kl").text)
        years_tag = job_skills.find("span")
        years_of_experience.append(years_tag.text if years_tag else None)
        jobs_skills.append(job_skills.text)

# Convert the List to Data Frame
df = pd.DataFrame({
        "JobTitle": jobs_titles,
        "Company": company_names,
        "Address": job_adresses,
        "CareerLevel": jobs_career_level,
        "YearsOfExperience": years_of_experience,
        "Skills": jobs_skills
})

# Get the excel file from the data frame
df.to_excel("Jobs_RowData.xlsx")