from math import cos, sin, sqrt

class Task:
    def __init__(self):
        self.dimention = 3
        self.answer = [0.2, 0.4, 0.1]    # actualy, not true -> need to find in net

        # limits with '<= 0' sign
        self.limits = [
            # sphere with Center (0, 0, 0) and Radius 4
            lambda x : x[0] ** 2 + 2*x[1] ** 2 - 3,
            # cylinder with Center (0, 0, 0) and Radius 3
            lambda x : 2*x[0] ** 2 + x[1] ** 2 - 4,
            # some more for 3rd coord, idk
            lambda x : x[0] ** 2 - x[1],
        ]

        # gradients for limits with '<= 0' sign
        self.d_limits = [
            # sphere with Center (0, 0, 0) and Radius 3
            lambda x : [2 * x[0],
                        4 * x[1],
                        0], 
            # cylinder with Center (0, 0, 0) and Radius 2
            lambda x : [4 * x[0],
                        2 * x[1],
                        0],
            # some more for 3rd coord, idk
            lambda x : [2 * x[0],
                        -1,
                        0]
        ]

        # limits with '= b' sign
        self.A = [[0, 0, 1]]
        self.b = [0] 
        return

    # INITS BY USER
    def f(self, x_list : list) -> float:
        # RETURN VALUE OF FUNC
        x = x_list[0]
        y = x_list[1]
        z = x_list[2]
        
        return x + y + pow(z, 2) + 4*(sqrt(1+2*pow(x, 2)+3*pow(y, 2)))
        
    # INITS BY USER
    def grad_f(self, x_list : list) -> list:
        # RETURN VEC OF DIFFS.
        x = x_list[0]
        y = x_list[1]
        z = x_list[2]
        
        df_1 =8*x/(sqrt(1+2*pow(x, 2)+3*pow(y, 2))) + 1
        df_2 =12*y/(sqrt(1+2*pow(x, 2)+3*pow(y, 2))) + 1
        df_3 = 2 * z
        return [df_1, df_2, df_3]
