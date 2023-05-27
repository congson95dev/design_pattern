# Explaination
# Singleton pattern là một mẫu thiết kế phần mềm, 
# nó được sử dụng để đảm bảo rằng một lớp chỉ có một thể hiện duy nhất trong toàn bộ ứng dụng. 
# Điều này giúp đảm bảo rằng các đối tượng sử dụng lớp này sẽ luôn luôn truy cập vào cùng một thể hiện 
# và tránh được các xung đột và sự không đồng bộ trong trường hợp có nhiều thể hiện của lớp đó.

class Singleton:
    __instance = None

    @staticmethod 
    def getInstance():
        if Singleton.__instance == None:
            Singleton()
        return Singleton.__instance

   def __init__(self):
        Singleton.__instance = self

# Sử dụng
s1 = Singleton.getInstance()
s2 = Singleton.getInstance()

if s1 == s2:
    print("Chỉ có một thể hiện của lớp Singleton")
else:
    print("Lớp Singleton có nhiều hơn một thể hiện")