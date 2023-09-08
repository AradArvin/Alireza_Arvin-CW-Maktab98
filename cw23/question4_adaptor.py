class NewLibrary:     
    def perforem_operation(self, data):         
        # Perform operation using the new library 
        pass 
              
class ClientCode:     
    def __init__(self, library) -> None:         
        self.library = library  

    def execute_operation(self, data):         
        self.library.perform_operation(data)   

new_library = NewLibrary() 
client_code = ClientCode(new_library) 
client_code.execute_operation("Data to process")


'''
1) The design issues in the given code snippet are:

   - Tight coupling: The client code directly depends on the `NewLibrary` class, making it difficult to switch to a different library in the future.
   - Lack of flexibility and extensibility: The code is not easily adaptable to work with a legacy library that has a different interface.

2) Apply the Adapter design pattern to refactor the code.

3) Implement the adapter class `LegacyAdapter`:
'''


class LegacyLibrary:
    def perforem_operation(self, data):
        # Perform operation using the legacy library
        pass

class LegacyAdapter:
    def __init__(self, legacy_library):
        self.legacy_library = legacy_library

    def perform_operation(self, data):
        self.legacy_library.perforem_operation(data)


# 4) Modify the client code to use the adapter class instead of directly interacting with the legacy library:


new_library = NewLibrary()
legacy_library = LegacyLibrary()
adapter = LegacyAdapter(legacy_library)

client_code = ClientCode(adapter)
client_code.execute_operation("Data to process")


'''
5) Explanation of the Adapter design pattern and its benefits in addressing the design issues:

The Adapter design pattern allows objects with incompatible interfaces to work together. It acts as a bridge 
between two incompatible interfaces, converting the interface of one class (the adaptee) into another interface 
that the client code expects. This pattern allows code to be reused even if it is designed to work with different interfaces.

In the original code, the client code directly depends on the `NewLibrary` class, making it tightly coupled 
and difficult to switch to a different library. By applying the Adapter design pattern, we introduce the 
`LegacyLibrary` class to act as an adaptee, and the `LegacyAdapter` class provides a common interface that 
the client code can work with.

The `LegacyAdapter` class wraps the `LegacyLibrary` instance and implements the desired interface expected 
by the client code. It delegates the actual operations to the `LegacyLibrary`. This allows the client code 
to interact seamlessly with the legacy library by going through the adapter, without directly depending on 
the specific implementation details.

The use of the Adapter pattern promotes loose coupling by decoupling the client code from the specific library 
implementation. It also enhances flexibility and extensibility, as new libraries or versions of the library can 
be easily integrated by creating new adapters that implement the desired interface.

I hope this explanation helps you understand the Adapter design pattern and how it addresses the design issues 
in the original code. Let me know if you have any further questions!
'''

# sina's Example
class LibraryInterface:
    def perform_operation(self, data):
        pass


class NewLibrary:
    def perform_operation(self, data):
        pass


class Adapter(LibraryInterface):
    def __init__(self, new_library):
        self.new_library = new_library

    def perform_operation(self, data):
        self.new_library.perform_operation(data)


class ClientCode:
    def __init__(self, library):
        self.library = library

    def execute_operation(self, data):
        self.library.perform_operation(data)


new_library = NewLibrary()
adapter = Adapter(new_library)
client_code = ClientCode(adapter)