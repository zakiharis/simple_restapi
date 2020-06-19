class Calculate(object):

    def __init__(self):
        self.inputs = []

    def add(self, number):
        self.inputs.append(number)

    def output(self):
        for i in range(9):
            if i % 2 != 0:
                self.format_output(i, self.inputs[:i+1])

    @staticmethod
    def format_output(line, output):
        total = sum(output)
        formatted_add = '+'.join(map(str, output))
        print(f'Line#{line}  {formatted_add}={total}')


if __name__ == '__main__':
    calc = Calculate()
    for _ in range(9):
        try:
            calc.add(int(input()))
        except Exception:
            print('Please enter int value')

    calc.output()
