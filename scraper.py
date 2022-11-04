from linkedin_job_profile_scraper_with_python import *
true=True;false=False
list_of_cookies=[
{
    "domain": ".linkedin.com",
    "expirationDate": 1676463230,
    "hostOnly": false,
    "httpOnly": false,
    "name": "_ga",
    "path": "/",
    "sameSite": "unspecified",
    "secure": false,
    "session": false,
    "storeId": "0",
    "value": "GA1.2.1029585723.1610264105",
    "id": 1
}]
#please replace the above sample cookies with your cookies, can see below link of how to fetch cookies
linkedin.login_cookie(cookies=list_of_cookies)
response=linkedin.get_job_profile(job_link='https://www.linkedin.com/jobs/view/2369119694/?refId=TtFWnJnfJ4Zg%2F7ciLoxuCA%3D%3D&trackingId=31e0gMvAc9LuFj7FH%2BPNgA%3D%3D&trk=flagship3_search_srp_jobs&lipi=urn%3Ali%3Apage%3Ad_flagship3_search_srp_jobs%3Bu6BQrVNCQYmzmhOzbcW9dg%3D%3D&lici=31e0gMvAc9LuFj7FH%2BPNgA%3D%3D')
data=response['body']