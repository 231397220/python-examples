import requests
import json

# 设置要获取问题的ID
id = 41273322

# 定义headers内容
headers = {
    'authority': 'www.zhihu.com',
    'sec-ch-ua': '"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"',
    'x-ab-param': 'qap_question_visitor= 0;li_edu_page=old;se_ffzx_jushen1=0;pf_adjust=1;zr_slotpaidexp=1;tp_dingyue_video=0;li_sp_mqbk=0;top_test_4_liguangyi=1;pf_noti_entry_num=2;li_vip_verti_search=0;li_panswer_topic=0;li_video_section=1;tp_contents=1;tp_zrec=1;qap_question_author=0;tp_topic_style=0;zr_expslotpaid=10;li_paid_answer_exp=0',
    'x-ab-pb': 'Clg/AJsLQgBSC9wLzwsPCyYM4AuWCxsAdQzkCkwLRwDgAPQLxQABC2wArQDXC4sAwgA0DFYMYAuJDHkAtwAPDDcM7Aq0ALQKZwC1CwcMCADmAOELaACkAGQMEiwAAgUBAAsBAAAAAAEAAAAAAAABAAAAAAEAAQAAAAAAAQEAAAADAQEAAQABAA==',
    'sec-ch-ua-mobile': '?0',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
    'x-requested-with': 'fetch',
    'x-zse-86': '1.0_aXOqUDr8Q0FxcXSqK8tygquBrMtf602qsLYqkALyQMYx',
    'x-zse-83': '3_2.0',
    'accept': '*/*',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://www.zhihu.com/question/437425765',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,und;q=0.7',
}


def get_url(id, offset):
    url = f"https://www.zhihu.com/api/v4/questions/{id}/answers?limit=5&offset={offset}&platform=desktop&sort_by=default&include=data%5B%2A%5D.is_normal%2Cadmin_closed_comment%2Creward_info%2Cis_collapsed%2Cannotation_action%2Cannotation_detail%2Ccollapse_reason%2Cis_sticky%2Ccollapsed_by%2Csuggest_edit%2Ccomment_count%2Ccan_comment%2Ccontent%2Ceditable_content%2Cattachment%2Cvoteup_count%2Creshipment_settings%2Ccomment_permission%2Ccreated_time%2Cupdated_time%2Creview_info%2Crelevant_info%2Cquestion%2Cexcerpt%2Cis_labeled%2Cpaid_info%2Cpaid_info_content%2Crelationship.is_authorized%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp%2Cis_recognized%3Bdata%5B%2A%5D.mark_infos%5B%2A%5D.url%3Bdata%5B%2A%5D.au"
    return url
def get_question_htlm(url, headers):
    try:
        response = requests.request("GET", url, headers=headers)
    except expression as identifier:
        print(f"get question error , {identifier}")
    res_text = response.text.encode('utf8')
    return res_text



def filter_answers(res_text):
    answer_datas = json.loads(res_text).get("data")
    if answer_datas:
        filter_answer_datas = []
        for answer_data in answer_datas:
            filter_answer_datas_dict={}
            filter_answer_datas_dict["name"] = answer_data["author"]["name"]
            filter_answer_datas_dict["title"] = answer_data["question"]["title"]
            filter_answer_datas_dict["answer"] = answer_data["excerpt"]
            filter_answer_datas.append(filter_answer_datas_dict)
        return filter_answer_datas
    else:
        return False


def save_answers_to_file(answer_datas, id):
    if answer_datas :
        with open(f"{id}_answers", "a", encoding="utf-8") as f:
            f.write(json.dumps(answer_datas))
    else:
        print("answer is null")


def main():
    #循环获取25道答案
    for offset in range(5, 25, 5):
        print(f"Ready to get {offset - 5} - {offset} answer")
        #获取问题url地址
        url = get_url(id, offset)
        #获取网页内容
        res_text = get_question_htlm(url, headers)
        #过滤答案
        answer_datas = filter_answers(res_text)
        print(f" answer_datas is {answer_datas}")
        #保存答案
        save_answers_to_file(answer_datas,id)

if __name__ == "__main__":
    main()
