# Explaination:
# Facade pattern cung cấp một giao diện đơn giản hơn để truy cập các lớp phức tạp hơn bên dưới. 
# Bằng cách sử dụng Facade pattern, người lập trình có thể ẩn đi sự phức tạp của các lớp đằng sau 
# và chỉ tập trung vào việc sử dụng các phương thức và thuộc tính của giao diện Facade.

# Trong ví dụ duới đây, chúng ta có các lớp Product, Order và Customer để quản lý các đối tượng sản phẩm, đơn hàng và khách hàng. 
# Tuy nhiên, để sử dụng các lớp này một cách đơn giản, chúng ta tạo một lớp OrderFacade để cung cấp một giao diện đơn giản hơn.

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Order:
    def __init__(self, customer, products):
        self.customer = customer
        self.products = products

class Customer:
    def __init__(self, name, email):
        self.name = name
        self.email = email

class OrderFacade:
    def __init__(self):
        self.products = []
        self.customers = []
        self.orders = []

    def add_product(self, name, price):
        product = Product(name, price)
        self.products.append(product)
        return product

    def add_customer(self, name, email):
        customer = Customer(name, email)
        self.customers.append(customer)
        return customer

    def place_order(self, customer_name, customer_email, product_names):
        customer = self.add_customer(customer_name, customer_email)
        products = [product for product in self.products if product.name in product_names]
        order = Order(customer, products)
        self.orders.append(order)
        return order

# Sử dụng
order_facade = OrderFacade()

product1 = order_facade.add_product("Product 1", 100)
product2 = order_facade.add_product("Product 2", 20)

customer = order_facade.add_customer("John Doe", "john.doe@example.com")

order = order_facade.place_order(customer.name, customer.email, [product1.name, product2.name])

print(f"Order placed for {customer.name} ({customer.email}) with products:")
for product in order.products:
    print(f"- {product.name} (${product.price})")