# Explaination:
# Trong Observer Pattern, có hai loại đối tượng chính: Subject và Observer. 
# Subject là đối tượng mà các Observer quan tâm và theo dõi. Khi Subject thay đổi, 
# nó sẽ thông báo cho tất cả các Observer của nó để cập nhật thông tin. 
# Nói cách khác Observer là các đối tượng đăng ký để nhận thông báo từ Subject.

# Trong ví dụ này, ta tạo ra hai đối tượng Observer và một đối tượng Subject. 
# Khi một Observer được tạo ra, nó sẽ đăng ký để nhận thông báo từ Subject bằng cách gọi phương thức attach(). 
# Khi Subject thay đổi trạng thái thông qua phương thức set_state(), 
# nó sẽ gọi phương thức notify() để thông báo cho tất cả các Observer cập nhật trạng thái mới. 
# Các Observer sẽ nhận được thông báo và gọi phương thức update() để cập nhật trạng thái của nó.

class Subject:
    def __init__(self):
        self.observers = []
        self._state = None

    def attach(self, observer):
        self.observers.append(observer)

    def notify(self):
        for observer in self.observers:
            observer.update()

    def set_state(self, state):
        self._state = state
        self.notify()

    def get_state(self):
        return self._state


class Observer:
    def __init__(self, subject):
        self.subject = subject
        self.subject.attach(self)

    def update(self):
        print(f"New state: {self.subject.get_state()}")


# Sử dụng
subject = Subject()
observer1 = Observer(subject)
observer2 = Observer(subject)

subject.set_state("State 1") # Kết quả: "New state: State 1"
subject.set_state("State 2") # Kết quả: "New state: State 2"