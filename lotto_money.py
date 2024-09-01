# lotto_money
# 상금 금액 책정해서 output 만들기

class money():
    def __init__(self, number):
        self.number = number

    def validate(self, list): 
        self.list = list

        # list[0] = number_correct
        # list[1] = number_bonus

        if list[0] == 6 : 
            print ("1등입니다. 500만원을 수령하세요.")
        elif list[1] == 5 : 
            if list[1] == 1 : 
                print ("2등입니다. 100만원을 수령하세요.")
            else : 
                print ("3등입니다. 20만원을 수령하세요.")   
        else : 
            pass

# if __name__ == "__main__" : 
#     # set = Set()
#     # sg = set.connect_sg()
#     # data_json = set._read_paths_from_json()
#     # set.data_needed(data_json)

#     pass