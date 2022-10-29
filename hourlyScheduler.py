from apscheduler.schedulers.background import BackgroundScheduler
from newsHandler import getRecentNews
from mailer import sendMailThroughSendGrid
from bodyHTMLRender import getHTMLBody

def sample():
    l = []
    articles = getRecentNews()
    for i in articles:
        if "entertainment" in i['category']:
            l.append(i)
    print(l)
    sendMailThroughSendGrid(getHTMLBody(l),"srijaganrvs@gmail.com")

def schedule():
    sched = BackgroundScheduler(daemon=True)
    sched.add_job(sample,'cron',hour='1,4,7,10,14,17,21,23')
    sched.start()
    while True:
        pass
sample()