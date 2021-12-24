import pyautogui

class Pen_draw_line():
    '''
    Hàm vẽ đường thẳng trên paint hoặc các app vẽ
    có sử dụng thư viện pyautogui vẽ bằng con trỏ chuột
    input: Tên bút vẽ, vị trí bắt đầu vẽ
    output: Tên bút vẽ, vị trí sau khi vẽ
    '''
    def __init__(self, name, position):
        self.__name = name
        self.__position = position

    def draw_Line_vertical(self, y, direction = 'b'):
        pyautogui.mouseDown(self.__position[0], self.__position[1])
        distance = -y if direction == 't' else y
        pyautogui.move(0, distance)
        pyautogui.mouseUp()
        self.__position = pyautogui.position()

    def draw_Line_horizontal(self, x, direction = 'l'):
        pyautogui.mouseDown(self.__position[0], self.__position[1])
        distance = x if direction == 'r' else -x
        pyautogui.move(distance, 0)
        pyautogui.mouseUp()
        self.__position = pyautogui.position()

    def getPosition(self):
        return pyautogui.position()

    def setPosition(self, position):
        self.__position = position

    def getName(self):
        return self.__name

    def setName(self, name):
        self.__name = name

if __name__ == '__main__':
    x = 1243
    y = 357

    width = 500
    height = 300

    def draw_base_spiral_rectangle(position, value, shrink_value):
        pen = Pen_draw_line('pen draw line', position)
        pen.draw_Line_horizontal(value[0], 'r')
        pen.draw_Line_vertical(value[1], 'b')
        new_value = (value[0]*shrink_value, value[1]*shrink_value)
        pen.draw_Line_horizontal(new_value[0], 'l')
        pen.draw_Line_vertical(new_value[1], 't')
        return pen.getPosition(), (new_value[0]*shrink_value, new_value[1]*shrink_value)

    def draw_spiral_rectangle(n, position, value, shrink_value):
        temp_position = position
        temp_value = value
        for i in range(n):
            (temp_position, temp_value) = draw_base_spiral_rectangle(temp_position, temp_value, shrink_value)

    draw_spiral_rectangle(5, (x, y), (width, height), 0.7)





