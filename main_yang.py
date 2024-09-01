import compare_lotto
from lotto_money import money
import lottoNumber

lotto_answer=lottoNumber.lotto_num
lotto_user=lottoNumber.user_input

result = compare_lotto.compare_lotto(lotto_answer, lotto_user)

money.validate(result)