name = 'minjoo'
# votes = {'minjoo': 0, 'kyle': 0, 'jun': 0}
votes = {}

# 아래는 key 없으면 바로 keyError
# if votes['minjoo']:
#     votes['minjoo'] += 1

# get 메서드 이용!
if votes.get('minjoo', -1) == -1:
    votes['minjoo'] = 0
else:
    votes['minjoo'] += 1