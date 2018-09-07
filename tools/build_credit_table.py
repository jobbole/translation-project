#coding:utf-8
from github import Github
from collections import namedtuple
import sys



g = Github(sys.argv[1], sys.argv[2])

REPO = "jobbole/translation-project"
repo = g.get_repo(REPO)
contributors = repo.get_contributors()
prs = repo.get_pulls(state='closed',base='trans')

TransEvent = namedtuple('TransEvent',['title', 'url', 'type','credit'])
Credit = namedtuple('Credit',['img','url','events'])

IMAGE_STYLE = "width='30px'"
IMAGE_SIZE = 30
CONTRIBUTOR_IMAGE_STYLE = "width='50px'"
CONTRIBUTOR_IMAGE_SIZE = 50
COL_NUM = 8

TRANS = 1
REVIEW = 2


_credit = {} 

def credit_badge(status,credit,color):
    return "https://img.shields.io/badge/{status}-{credit}--credit-{color}.svg?longCache=true&style=popout-square".format(status=status,credit=credit,color=color)
 
def get_image_tag(login,avatar_url,size,style):
    return  '<img alt="{login}" src="{avatar_url}&s={size}" {style}>'.format(login=login,avatar_url=avatar_url,size=size,style=style)


def set_artical_title():
       return u"|文章|完成时间|译者|积分|校对|积分|\n|:---|:---|:---|:---|:---|:---|\n".encode('utf-8')

def set_credit_title():
       return u"|译者|事件|总积分|\n|:---|:---|:---|\n".encode('utf-8')

def set_row(info):   
    translator = info["participant"]["translator"]
    reviewer =  info["participant"]["reviewer"]
    table =  "| [{title}]({url}) |  {time}  | {img_trans}<br>[{trans_name}]({trans_url}) |{trans_credit}|{img_reviewer}<br>[{reviewer_name}]({reviewer_url})| {reviewer_credit}   | \n".format(
        img_trans = translator["img"],
        trans_name =translator["name"],
        trans_url = translator["url"],
        trans_credit = translator['credit'],
        img_reviewer = reviewer["img"],
        reviewer_name =reviewer["name"],
        reviewer_url = reviewer["url"],
        reviewer_credit = reviewer['credit'],
        title=info["title"],
        url=info["url"],
        time=info["time"].strftime("%Y-%m-%d") if not info["time"] is None else "")

    return table 

def set_credit_row(name,credit):   
    events_string = ""
    credit_sum = 0
    for e in credit.events:
        if e.type == TRANS:
            event_type = u"翻译"
        elif e.type == REVIEW:
            event_type = u"校对"
        events_string += "[{title}]({url}) : {type}  {credit}<br>".format(title=e.title,url=e.url,type=event_type.encode('utf-8'),credit=e.credit)
        credit_sum += int(e.credit)
        table =  "| {img}[{name}]({url}) |{events} | {credit_sum}| \n".format(img = credit.img,name = name,url = credit.url,events= events_string,credit_sum = credit_sum
    )

    return table 

# 一个pr可能有多个校对者，积分给在评论中认领校对的译者
def get_reviewer_in_charge(pr):
    for comment in pr.get_issue_comments():
        if u"认领校对" in comment.body:
            reviewer_in_charge = comment.user
        else:
            reviewer_in_charge =  pr.get_reviews()[0].user
        return reviewer_in_charge


def collcet_info():
    infos = []
    for pr in prs:
        labels = [label.name for label in pr.get_labels()]
        if pr.is_merged() and ("C1-Finished" in labels or "C2-Published" in labels):
            reviewer = get_reviewer_in_charge(pr)
            info = {
                "id":pr.id,
                "participant"  :  {
                    "translator":{
                        "img":get_image_tag(pr.user.login,pr.user.avatar_url,IMAGE_SIZE,IMAGE_STYLE),
                        "name":pr.user.login,
                        "url":pr.user.html_url,
                        "credit":"+50"
                        },
                    "reviewer": {
                        "img":get_image_tag(reviewer.login,reviewer.avatar_url,IMAGE_SIZE,IMAGE_STYLE),
                        "name":reviewer.login,
                        "url":reviewer.html_url,
                        "credit":"+50"
                        },
                },
                "title" : pr.title.encode('utf-8'),
                "url" : pr.html_url,
                "time" : pr.merged_at,
                "credit" : "50"
            }
            
            infos.append(info)
    return sorted(infos, key=lambda info: info['id'])  




def make_credit(name,img,url,event):
    #for existed translator,only append event to it
    if _credit.has_key(name):
       credit =  _credit[name]
       credit.events.append(event)
    else:# create a new credit structure for a new translator 
        credit = Credit(img  = img, url = url, events=[event])
        _credit[name] = credit


def build_credits(infos):
    for info in infos:
        translator = info["participant"]["translator"]
        reviewer =  info["participant"]["reviewer"]
        title=info["title"]
        url=info["url"]
        trans_event = TransEvent(title=title, url=url, type=TRANS,credit=translator['credit'],)
        review_event = TransEvent(title=title, url=url, type=REVIEW,credit=reviewer['credit'])
        make_credit(translator['name'],translator['img'],translator['url'],trans_event)
        make_credit(reviewer['name'],reviewer['img'],reviewer['url'],review_event)

def build_artical_table(infos):
    result = set_artical_title()
    for info in infos:
        result = result + set_row(info)
    return result 


def build_credit_table(infos):
    result = set_credit_title()
    build_credits(infos)
    for name,credit in _credit.items():
        result = result + set_credit_row(name,credit)
    return result 



def build_contributors_table(info):
    table = ''
    table_line = head_line = cell_line = "|"
    
    insert_table_line_flag = True
    for index,contributor in  enumerate(repo.get_contributors()):
        print contributor
        
        if index !=0 and  index % COL_NUM == 0:
            head_line = cell_line = "|"
            table += "\n"
            if insert_table_line_flag:
                insert_table_line_flag = False
                table += head_line+"\n"+table_line+"\n"+cell_line
            else :
                table += head_line+"\n"+cell_line

        name  = contributor.login
        img = get_image_tag(name,contributor.avatar_url,CONTRIBUTOR_IMAGE_SIZE,CONTRIBUTOR_IMAGE_STYLE)
        head_line += " {img} |".format(img=img)
        table_line +=":---:|"
        cell_line += "[{name}]({url}) |".format(name=name,url=contributor.html_url)
        
    if insert_table_line_flag:
        insert_table_line_flag = False
        table += head_line+"\n"+table_line+"\n"+cell_line
    else :
        table += head_line+"\n"+cell_line
    return table


def main():
    infos = collcet_info()
    print u"# 译者积分表".encode('utf-8')
    print u"# Events"
    print build_artical_table(infos)
    print u"# Credits"
    print build_credit_table(infos)
    print u'##  Contributors'
    #print build_contributors_table(infos)


if __name__ == '__main__':
    main()
