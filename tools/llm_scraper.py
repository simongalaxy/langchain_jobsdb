from langchain_classic.schema import Document
from langchain_community.document_loaders import PlaywrightURLLoader

from bs4 import BeautifulSoup

# Render Page.
def render_job_page(urls: list[str]) -> list[Document]:
    
    loader = PlaywrightURLLoader(urls=urls)
    docs = loader.load()
    
    return docs


# post-process with beautifulsoup.
def post_process_rendered_page(docs: list[Document]) -> list[str]:
    
    clean_texts = []
    
    for doc in docs:
        soup = BeautifulSoup(doc.page_content, "html.parser")
        job_desc = soup.find("div", class_="jd__content")
        
        print(job_desc)
        # clean_text = job_desc.get_text(strip=True)
        # print(clean_text)
        # clean_texts.append(clean_text)
    
    return clean_texts



# scrape job responsibilities, job requirements from job advertisement link. 
def get_job_ad_data(jobs: list[dict]) -> None:
    
    # copy jobs.
    copy_jobs = jobs
    
    # get the job ad urls.
    job_urls = [job["jobUrl"] for job in copy_jobs]
    
    # render job ad pages to html and then generate clean text.
    docs = render_job_page(urls=job_urls)
   
    clean_texts = post_process_rendered_page(docs=docs)
    
    return

