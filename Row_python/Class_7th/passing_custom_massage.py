# Custom Masssege passing
class small_num_exception(Exception):
    def __init__(self, massage='Number is smaller then 10'):
        self.massage = massage
        super().__init__(self.massage)


class big_num_exception(Exception):
    def __init__(self, massage='Number is bigger then 100'):
        self.massage = massage
        super().__init__(self.massage)

class NotRangeNumber(Exception):
    def __init__(self, number, massage='Number is out of range'):
        self.number = number
        self.massage = massage
        super().__init__(self.massage)

class Number:
    def take_num(self, number):
        try:
            if number < 10:
                # raise exception keyword
                raise small_num_exception
            if number > 100:
                raise big_num_exception
        except small_num_exception as error:
            print(error)
        except big_num_exception as error:
            print(error)
        print(number)
    
    def second_number(self, number):
        try:
            if not 1000 < number < 4000:
                raise NotRangeNumber(number)
        except NotRangeNumber as error:
            print(error)
        


number = Number()
number.take_num(int(input()))
number.second_number(int(input()))
