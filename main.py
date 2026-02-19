from scraper import scrap_jobs
from utils import save_to_excel

def main():
    data_frame = scrap_jobs(pages=100)
    save_to_excel(data_frame,"jobs_RowData")


if __name__ == "__main__":
    main()