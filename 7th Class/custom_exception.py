# Custom Exception 
# Small num and big number exception 
class small_num_exception(Exception):
    pass


class big_num_exception(Exception):
    pass


class Number:
    def take_num(self, number):
        try:
            if number < 10:
            # raise exception keyword
                raise small_num_exception
            if number > 100:
                raise big_num_exception
        except small_num_exception as error:
            print('Number is smaller then 10')
        except big_num_exception as error:
            print('Number is bigger then 100')
        print(number)


number = Number()
number.take_num(44)
      
