# https://school.programmers.co.kr/learn/courses/30/lessons/92334?language=python3

"""
result 값이 어떻게 나오는지 먼저 보기
제한 사항 : 길이 파악 후 알고리즘 설계
자료 구조 모양 정하기
중복 제거
1. 해시 자료 구조(set)
2. dict : 신고 당한 사람을 기준으로 key, value = {신고자 : 카운트}
dict를 돌면서 value의 len이 k개 이상이면 keys()에 메일을 보냄

문제 조건 정리

1명 -> 한번에 1명씩 제한없이 신고 가능.
    -> 1명 여러번 신고 가능 but, 1회로 처리.

k번 신고당함 -> 정지, 신고한 유저들에게 메일로 발송함. (자료구조로 id저장하고 있어야.)
            정지먹을때마다 보내는게 아니라, 전체 input이 다 주어지고나서 취합해서 메일을 보냄.

원하는 자료구조 모양 -> frodo가 muzi에게 여러번 신고당해도 1로 체크만 되길 원함. (가산되길 원하면 +=1로 수정가능)
{'frodo' :
    {'muzi':1,
    'appeach':1,
    }
}
frodo가 신고를 받았는데, muzi, appeach가 신고했다는 뜻.
취합은 report_dict[id_value]의 len을 돌려서 k이상인지 판별하고, 된다면 그 key들을 돌려서(dict에 대한 for loop은 key를 대상으로 돌려줍니다.) id list에 넣어주기.
"""


def solution(id_list, report, k):
    report_dict = {key: {} for key in id_list}
    mail_dict = {key: 0 for key in id_list}

    for report_item in report:
        reporter, reported = report_item.split()
        report_dict[reported][reporter] = 1

    for each_id in id_list:
        if len(report_dict[each_id]) >= k:
            for key in report_dict[each_id].keys():
                mail_dict[key] += 1

    answer = list(mail_dict.values())
    return answer
