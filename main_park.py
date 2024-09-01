#main_park

import lottoNumber
from compare_lotto import compare_lotto
from lotto_money import money

ans = lottoNumber.lotto_num
user = lottoNumber.user_input

list_number = compare_lotto(ans, user)
valid = money()
valid.validate(list_number)