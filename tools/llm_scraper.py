from langchain_ollama import OllamaLLM
from langchain_community.document_loaders import PlaywrightURLLoader


# scrape job responsibilities, job requirements from job advertisement link. 
def get_job_ad_data(jobs: list[dict]) -> None:
    
    # copy jobs.
    copy_jobs = jobs
    
    # initiate llm using ollama.
    # llm = OllamaLLM(model="llama3")
    
    job_urls = [job["jobUrl"] for job in copy_jobs]
    print(job_urls)
    
    loader = PlaywrightURLLoader(
        urls=job_urls,
        headless=True
        )
    docs = loader.load()
    
    print(docs[0].page_content)
    
    return

