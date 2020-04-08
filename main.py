from indeed import get_jobs as indeed_extract_jobs
from save import save_to_file

jobs = indeed_extract_jobs()
save_to_file(jobs)
