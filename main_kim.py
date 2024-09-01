from compare_lotto import compare_lotto
import lottoNumber 
from lotto_money import money

user_answer = lottoNumber.user_input
answer = lottoNumber.lotto_num

count = compare_lotto(answer, user_answer)

Money = money()
Money.validate(count)