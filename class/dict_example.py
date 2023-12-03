name = 'alex'
# votes = {'alex': 0, 'kyle': 0, 'jun': 0}
votes = {}
if votes.get('alex', -1) == -1: # get으로 key를 조회하면 에러가 발생하지 않음
    votes['alex'] = 0 # 없으면 초기 셋팅을 해준다
else:
    votes['alex'] += 1 # 있으면 1을 더해준다