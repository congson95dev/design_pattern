# Explaination:
# Adapter pattern là khi chúng ta tạo 1 class trung gian 
# nhằm chuyển đổi một đoạn code không tương thích thành một đoạn code khác mà các đối tượng có thể sử dụng.

# VD class ImageLibrary có hàm open_image, nhưng class ExternalImageLibrary lại có hàm change_size
# ta muốn hàm open_image sử dụng được hàm change_size nhưng lại không muốn sửa trực tiếp code
# thì ta có thể sử dụng 1 class trung gian được gọi là ImageAdapter, class này kế thừa từ class ImageLibrary
# giờ hàm request sẽ có thể sử dụng đc hàm change_size thông qua class ImageAdapter


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