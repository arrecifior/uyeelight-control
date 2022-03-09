class ButtonHandler():
    in1_prev = 0
    in2_prev = 0
    in3_prev = 0
    in4_prev = 0

    def __init__(self, in1_obj, in2_obj, in3_obj, in4_obj):
        self.in1_obj = in1_obj
        self.in2_obj = in2_obj
        self.in3_obj = in3_obj
        self.in4_obj = in4_obj

    def get_status(self):
        in1 = self.in1_obj.value()
        in2 = self.in2_obj.value()
        in3 = self.in3_obj.value()
        in4 = self.in4_obj.value()

        if \
            in1 == 1 and self.in1_prev == 0 and \
            in2 == 1 and self.in2_prev == 0 and \
            in3 == 1 and self.in3_prev == 0 and \
            in4 == 1 and self.in4_prev == 0:
            ret = 0
        elif \
            in1 == 1 and self.in1_prev == 0 and \
            in2 == 0 and self.in2_prev == 0 and \
            in3 == 0 and self.in3_prev == 0 and \
            in4 == 0 and self.in4_prev == 0:
            ret = 1
        elif \
            in1 == 0 and self.in1_prev == 0 and \
            in2 == 1 and self.in2_prev == 0 and \
            in3 == 0 and self.in3_prev == 0 and \
            in4 == 0 and self.in4_prev == 0:
            ret = 2
        elif \
            in1 == 1 and self.in1_prev == 0 and \
            in2 == 1 and self.in2_prev == 0 and \
            in3 == 0 and self.in3_prev == 0 and \
            in4 == 0 and self.in4_prev == 0:
            ret = 3
        elif \
            in1 == 0 and self.in1_prev == 0 and \
            in2 == 0 and self.in2_prev == 0 and \
            in3 == 1 and self.in3_prev == 0 and \
            in4 == 0 and self.in4_prev == 0:
            ret = 4
        elif \
            in1 == 1 and self.in1_prev == 0 and \
            in2 == 0 and self.in2_prev == 0 and \
            in3 == 1 and self.in3_prev == 0 and \
            in4 == 0 and self.in4_prev == 0:
            ret = 5
        elif \
            in1 == 1 and self.in1_prev == 0 and \
            in2 == 1 and self.in2_prev == 0 and \
            in3 == 1 and self.in3_prev == 0 and \
            in4 == 0 and self.in4_prev == 0:
            ret = 6
        elif \
            in1 == 0 and self.in1_prev == 0 and \
            in2 == 0 and self.in2_prev == 0 and \
            in3 == 0 and self.in3_prev == 0 and \
            in4 == 1 and self.in4_prev == 0:
            ret = 7
        elif \
            in1 == 1 and self.in1_prev == 0 and \
            in2 == 0 and self.in2_prev == 0 and \
            in3 == 0 and self.in3_prev == 0 and \
            in4 == 1 and self.in4_prev == 0:
            ret = 8
        else:
            ret = -1

        self.in1_prev = in1
        self.in2_prev = in2
        self.in3_prev = in3
        self.in4_prev = in4

        return ret
