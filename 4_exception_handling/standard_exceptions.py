import sys

def exception_demo():
    try:
        # 1. Exception (Base class for all exceptions)
        raise Exception("This is a generic exception")
    except Exception as e:
        print(f"Exception caught: {e}")

    try:
        # 2. StopIteration (Raised when next() reaches the end)
        it = iter([1, 2])
        print(next(it))
        print(next(it))
        print(next(it))  # This will raise StopIteration
    except StopIteration:
        print("StopIteration caught: No more items in iterator")

    try:
        # 3. SystemExit (Raised by sys.exit())
        sys.exit(0)
    except SystemExit:
        print("SystemExit caught: Program tried to exit")

    try:
        # 5. ArithmeticError (Base for numeric calculation errors)
        raise ArithmeticError("General arithmetic error")
    except ArithmeticError as e:
        print(f"ArithmeticError caught: {e}")

    try:
        # 6. OverflowError (Number too large)
        import math
        print(math.exp(1000))  # Causes OverflowError
    except OverflowError as e:
        print(f"OverflowError caught: {e}")

    try:
        # 7. FloatingPointError (Floating point operation fails)
        raise FloatingPointError("Floating point calculation error")
    except FloatingPointError as e:
        print(f"FloatingPointError caught: {e}")

    try:
        # 8. ZeroDivisionError (Dividing by zero)
        x = 1 / 0
    except ZeroDivisionError as e:
        print(f"ZeroDivisionError caught: {e}")

    try:
        # 9. AssertionError (Raised when assert fails)
        assert False, "Assertion failed!"
    except AssertionError as e:
        print(f"AssertionError caught: {e}")

    try:
        # 10. AttributeError (Accessing an invalid attribute)
        class Dummy:
            pass
        d = Dummy()
        print(d.some_attribute)  # Does not exist
    except AttributeError as e:
        print(f"AttributeError caught: {e}")

    try:
        # 11. EOFError (No input received)
        raise EOFError("End of file reached")
    except EOFError as e:
        print(f"EOFError caught: {e}")

    try:
        # 12. ImportError (Module does not exist)
        import notamodule
    except ImportError as e:
        print(f"ImportError caught: {e}")

    try:
        # 13. KeyboardInterrupt (User interrupts program)
        raise KeyboardInterrupt("User pressed Ctrl+C")
    except KeyboardInterrupt as e:
        print(f"KeyboardInterrupt caught: {e}")

    try:
        # 14. LookupError (Base for index & key errors)
        raise LookupError("Generic lookup error")
    except LookupError as e:
        print(f"LookupError caught: {e}")

    try:
        # 15. IndexError (Index out of range)
        lst = [1, 2, 3]
        print(lst[5])
    except IndexError as e:
        print(f"IndexError caught: {e}")

    try:
        # 16. KeyError (Key not found in dictionary)
        d = {'a': 1, 'b': 2}
        print(d['c'])
    except KeyError as e:
        print(f"KeyError caught: {e}")

    try:
        # 17. NameError (Undefined variable)
        print(unknown_var)
    except NameError as e:
        print(f"NameError caught: {e}")

    try:
        # 18. UnboundLocalError (Variable referenced before assignment)
        def func():
            print(x)  # x is not defined locally before use
            x = 10
        func()
    except UnboundLocalError as e:
        print(f"UnboundLocalError caught: {e}")

    try:
        # 20. IOError (File-related error)
        f = open("nonexistent.txt", "r")
    except IOError as e:
        print(f"IOError caught: {e}")

    try:
        # 21. OSError (Operating system error)
        import os
        os.mkdir("test")  # Create directory
        os.mkdir("test")  # Creating the same directory again
    except OSError as e:
        print(f"OSError caught: {e}")

    try:
        # 22. SyntaxError (Incorrect syntax)
        exec("if True print('Hello')")  # Missing colon
    except SyntaxError as e:
        print(f"SyntaxError caught: {e}")

    try:
        # 23. IndentationError (Incorrect indentation)
        exec("def func():\nprint('Hello')")  # No indentation for print
    except IndentationError as e:
        print(f"IndentationError caught: {e}")

    try:
        # 24. SystemError (Internal Python error)
        raise SystemError("An internal system error occurred")
    except SystemError as e:
        print(f"SystemError caught: {e}")

    try:
        # 26. TypeError (Wrong data type operation)
        print("2" + 2)
    except TypeError as e:
        print(f"TypeError caught: {e}")

    try:
        # 27. ValueError (Invalid argument)
        int("xyz")
    except ValueError as e:
        print(f"ValueError caught: {e}")

    try:
        # 28. RuntimeError (Generic runtime error)
        raise RuntimeError("Some runtime error occurred")
    except RuntimeError as e:
        print(f"RuntimeError caught: {e}")

    try:
        # 29. NotImplementedError (Method not implemented)
        class AbstractClass:
            def method(self):
                raise NotImplementedError("This method must be overridden")
        obj = AbstractClass()
        obj.method()
    except NotImplementedError as e:
        print(f"NotImplementedError caught: {e}")

# Run the function to trigger all exceptions
exception_demo()
