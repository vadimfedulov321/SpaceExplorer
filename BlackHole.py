import numpy as np
import random

cl_bn = [0.5, 0.25, 0.2, 0.05]
z = '*' * 80

if __name__ == "__main__":
    print(f'{z}\nВы должны открыть game.py, это всего лишь модуль!\n{z}')


class BlackHole(object):
    def __init__(self, Sys, clp=cl_bn):
        self.cl_var = ['малая', 'средне-малая', 'средне-большая', 'большая']
        self.cl_ch1 = np.random.choice(self.cl_var, p=clp)
        self.cl_ch2 = np.random.choice(self.cl_var, p=clp)

        def check_cl_ch(number):
            if number == 1:
                if self.cl_ch1 == 'малая':
                    self.m1 = np.round(random.uniform(10, 99), decimals=2)
                elif self.cl_ch1 == 'средне-малая':
                    self.m1 = np.round(random.uniform(100, 264), decimals=2)
                elif self.cl_ch1 == 'средне-большая':
                    self.m1 = np.round(random.uniform(265, 499), decimals=2)
                elif self.cl_ch1 == 'большая':
                    self.m1 = np.round(random.uniform(500, 999), decimals=2)
            elif number == 2:
                if self.cl_ch2 == 'малая':
                    self.m2 = np.round(random.uniform(10, 99), decimals=2)
                elif self.cl_ch2 == 'средне-малая':
                    self.m2 = np.round(random.uniform(100, 264), decimals=2)
                elif self.cl_ch2 == 'средне-большая':
                    self.m2 = np.round(random.uniform(265, 499), decimals=2)
                elif self.cl_ch2 == 'большая':
                    self.m2 = np.round(random.uniform(500, 999), decimals=2)

        if Sys.get_obj('Bh') is None:
            self.b = None
        elif Sys.get_obj('Bh') == [1]:
            check_cl_ch(1)
            self.nb1 = Sys.get_ns(1)
            self.b = 1
        elif Sys.get_obj('Bh') == [2]:
            check_cl_ch(1)
            self.nb1 = Sys.get_ns(2)
            self.b = 1
        elif Sys.get_obj('Bh') == [1, 2]:
            check_cl_ch(1)
            check_cl_ch(2)
            self.nb1 = Sys.get_ns(1)
            self.nb2 = Sys.get_ns(2)
            self.b = 2
        elif Sys.get_obj('Bh') == [3]:
            check_cl_ch(1)
            self.nb1 = Sys.get_ns(3)
            self.b = 1

    def decor(function):
        def decorate(self, z, *args):
            print(z)
            function(self, *args)
            print(z)
        return decorate

    def __num_error(self, number):
        self.err1 = 'Вы ввели некорректный номер черной дыры для исследования'
        self.err2 = 'Помните, что нужно писать порядковый '
        self.err3 = 'номер объекта данного типа'
        if number == 1:  # this __num_error works only for examination (Bh)
            self.err4 = 'В данном случае вы можете написать только "1"'
        elif number == 2:  # for help and riskjump we use help_bh
            self.err4 = 'В данном случае вы можете написать только "1"/"2"'
        print(f'{self.err1}\n{self.err2}{self.err3}\n{self.err4}')

    def __multiple_form(self, n):
        if n <= 1:
            return 'солнечной единицы'
        else:
            return 'солнечных единиц'

    def _multi_single_error(self, n):
        if self.b is None:
            return [True, True]  # error for all forms
        elif self.b == 2 and n is 'all':
            return [True, False]  # error for single form
        elif self.b == 1 and n != 1:
            return [True, True]  # error for all forms
        elif self.b == 2 and n != 1 and n != 2:
            return [True, True]  # error for all forms
        elif self.b == 1 or self.b == 2 and n == 1:
            return [False, True]  # error for multiple form
        elif self.b == 2 and n == 2:
            return [False, True]  # error for multiple form

    @decor
    def help_bh(self, h_j=False):
        if h_j:
            self.h1 = 'В данной системе есть '
            self.h2 = 'две черные дыры для рискового прыжка'
            self.h3 = 'Вы можете написать "1" или "2" для прыжка '
            self.h4 = 'вблизи орбит одной из них'
            print(f'{self.h1}{self.h2}\n{self.h3}{self.h4}')
        else:
            if self.b is None:
                self.h1 = 'В данной системе нет черных дыр для исследования'
                self.h2 = 'Попробуйте исследовать систему, звезды'
                self.h3 = ' или совершить прыжок'
                print(f'{self.h1}\n{self.h2}{self.h3}')
            elif self.b == 1:
                self.h1 = 'В данной системе есть только одна '
                self.h2 = 'черная дыра для исследования'
                self.h3 = 'Вы можете написать "1" для её исследования'
                print(f'{self.h1}{self.h2}\n{self.h3}')
            elif self.b == 2:
                self.h1 = 'В данной системе есть '
                self.h2 = 'две черные дыры для исследования'
                self.h3 = 'Вы можете написать "1" или "2" для исследования '
                self.h4 = 'одной из них'
                print(f'{self.h1}{self.h2}\n{self.h3}{self.h4}')

    def riskjump(self, n, diff):
        luck = [False, True]
        if n == 1:
            if self.cl_ch1 == 'малая':
                return np.random.choice(luck, p=[0.75, 0.25])
            elif self.cl_ch1 == 'средне-малая':
                return np.random.choice(luck, p=[0.6, 0.4])
            elif self.cl_ch1 == 'средне-большая':
                return np.random.choice(luck, p=[0.4, 0.6])
            elif self.cl_ch1 == 'большая':
                return np.random.choice(luck, p=[0.25, 0.75])
        elif n == 2:
            if self.cl_ch2 == 'малая':
                return np.random.choice(luck, p=[0.75, 0.25])
            elif self.cl_ch2 == 'средне-малая':
                return np.random.choice(luck, p=[0.6, 0.4])
            elif self.cl_ch2 == 'средне-большая':
                return np.random.choice(luck, p=[0.4, 0.6])
            elif self.cl_ch2 == 'большая':
                return np.random.choice(luck, p=[0.25, 0.75])

    @staticmethod  # here definetely will be logistic regression instead
    def diff_measure(diff):  # of boolean logic in future releases
        if diff < 1000:
            return 40
        elif diff < 1500:
            return 37.5
        elif diff < 2000:
            return 35
        elif diff < 2500:
            return 32.5
        elif diff < 3000:
            return 30
        elif diff < 3500:
            return 27.5
        elif diff < 4000:
            return 25
        elif diff < 4500:
            return 22.5
        elif diff < 5000:
            return 20
        elif diff < 5500:
            return 17.5
        elif diff < 6000:
            return 15
        elif diff < 6500:
            return 12.5
        elif diff < 7000:
            return 10
        elif diff < 7500:
            return 7.5
        elif diff <= 8000:
            return 5

    def get_prob(self, n, diff):
        if n == 1:
            if self.cl_ch1 == 'малая':
                prob = 25 + self.diff_measure(diff)
                return prob
            elif self.cl_ch1 == 'средне-малая':
                prob = 20 + self.diff_measure(diff)
                return prob
            elif self.cl_ch1 == 'средне-большая':
                prob = 15 + self.diff_measure(diff)
                return prob
            elif self.cl_ch1 == 'большая':
                prob = 10 + self.diff_measure(diff)
                return prob
        elif n == 2:
            if self.cl_ch2 == 'малая':
                prob = 25 + self.diff_measure(diff)
                return prob
            elif self.cl_ch2 == 'средне-малая':
                prob = 20 + self.diff_measure(diff)
                return prob
            elif self.cl_ch2 == 'средне-большая':
                prob = 15 + self.diff_measure(diff)
                return prob
            elif self.cl_ch2 == 'большая':
                prob = 10 + self.diff_measure(diff)
                return prob

    def ex_bh(self, n):
        if n == 1:
            self.form1 = self.__multiple_form(self.m1)
            self.desc1 = f'{self.nb1} - это {self.cl_ch1} черная дыра'
            self.desc2 = f'Имеет массу {self.m1} {self.form1}'
            print(f'{self.desc1}\n{self.desc2}')
        elif n == 2:
            self.form2 = self.__multiple_form(self.m2)
            self.desc3 = f'{self.nb2} - это {self.cl_ch2} черная дыра'
            self.desc4 = f'Имеет массу {self.m2} {self.form2}'
            print(f'{self.desc3}\n{self.desc4}')

    @decor
    def examine_bh(self, zin, n):
        if self.b is None:
            print('В данной системе нет черных дыр для исследования')
        elif self.b == 2 and n == 'all':
            self.ex_bh(1)
            print(zin)
            self.ex_bh(2)
        elif self.b == 1 and n == 'all':
            print('В данной системе находится только одна черная дыра')
        elif self.b == 1 and n != 1:
            self.__num_error(1)
        elif self.b == 2 and n != 1 and n != 2:
            self.__num_error(2)
        elif self.b == 1 or self.b == 2 and n == 1:
            self.ex_bh(1)
        elif self.b == 2 and n == 2:
            self.ex_bh(2)
