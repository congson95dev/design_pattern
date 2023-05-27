# Explaination:
# Adapter pattern là khi chúng ta tạo 1 class trung gian 
# nhằm chuyển đổi một đoạn code không tương thích thành một đoạn code khác mà các đối tượng có thể sử dụng.

# VD class Target có hàm request, nhưng class Adapter lại có hàm specific_request
# ta muốn hàm Target sử dụng được hàm specific_request nhưng lại không muốn sửa trực tiếp code
# thì ta có thể sử dụng 1 class trung gian được gọi là Adapter, class này kế thừa từ class Target
# giờ hàm request sẽ có thể sử dụng đc hàm specific_request thông qua class Adapter


class ImageLibrary:
    def open_image(self):
        pass

class ExternalImageLibrary:
    def change_size(self):
        return "Ảnh đã được thay đổi size"

class ImageAdapter(ImageLibrary):
    def __init__(self, external_lib: ExternalImageLibrary):
        self.external_lib = external_lib

    def open_image(self):
    	# trong hàm này, chúng ta vừa mở ảnh, vừa thay đổi size ảnh
        return f"Thay đổi size ảnh: {self.external_lib.change_size()}"

adapter = ImageAdapter(ExternalImageLibrary())
print(adapter.open_image())