class RightTriangle:
    def __init__(self, hyp, leg_1, leg_2):
        self.c = hyp
        self.a = leg_1
        self.b = leg_2
        self.area = (1 / 2) * (input_a * input_b)


# triangle from the input
input_c, input_a, input_b = [int(x) for x in input().split()]

x = RightTriangle(input_c, input_a, input_b)

# pythagorean condition
if (x.c ** 2) == (x.a ** 2) + (x.b ** 2):
    print('Right')
    print('Area: ', x.area)
else:
    print('Not right')
