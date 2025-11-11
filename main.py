from tools.webscraper import fetch_job_search_data, get_job_info
from tools.llm_scraper import get_job_ad_data

from pprint import pprint

# main program.
def main():
    
    # testing.
    search_keyword=input("Please input the search keyword: ")
    results = fetch_job_search_data(keyword=search_keyword)

    # get the total no. of jobs from careertimes.com.hk
    total_scraped_jobs = results["data"]["meta"]["jobsTotal"]
    print(f"total no. of jobs: {total_scraped_jobs}")
    
    # jobs scraped by search_keyword.
    jobs = get_job_info(jobs=results["data"]["jobs"])
    
    # scrape job responsibilities, job requirements 
    get_job_ad_data(jobs=jobs)
    
    return

# program entry point.
if __name__ == "__main__":
    main()
