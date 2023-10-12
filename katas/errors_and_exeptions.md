# 8. Errors and Exceptions
https://docs.python.org/3/tutorial/errors.html

## Sintaxis errors
Also known as parsing errors

```python
print('Hello world')
```

## Exceptions
Even if a statement or expression is syntactically correct, it may cause an error when an attempt is
made to execute it. Errors detected during execution are called exceptions and are not unconditionally
fatal
```python
x = 10 * (1 / 0)  # ZeroDivisionError: division by zero
y = 4 + spam * 3  # NameError: name 'spam' is not defined
z = '2' + 2  # TypeError: can only concatenate str (not "int") to str
```

## Handling Exceptions
```python
while True:
    try:
        x = int(input("Please enter a number"))
        break
    except ValueError:
        print("Oops! That was not a valid number. Try again...")
```
A try statement may have more than one except clause, to specify handlers for different exceptions.
At most one handler will be executed. Handlers only handle exceptions that occur in the corresponding
try clause, not in other handlers of the same try statement. An except clause may name multiple
exceptions as a parenthesized tuple, for example:
```except(RuntimeError, TypeError, NameError)```

*BaseException* is the common base class of all exceptions. One of its subclasses, _Exception_, is the base
class of all the non-fatal exceptions. Exceptions which are not subclasses of Exception are not typically
handled, because they are used to indicate that the program should terminate. They include SystemExit
which is raised by sys.exit() and KeyboardInterrupt which is raised when a user wishes to interrupt the
program.

Exception can be used as a wildcard that catches (almost) everything. However, it is good practice to
be as specific as possible with the types of exceptions that we intend to handle, and to allow any
unexpected exceptions to propagate on.

## Exception types
* OSError
* ValueError
* ZeroDivisionError 

The most common pattern for handling Exception is to print or log the exception and then re-raise it
(allowing a caller to handle the exception as well):
```python
import sys

try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print("OS error:", err)
except ValueError:
    print("Could not convert data to an integer.")
except Exception as err:
    print(f"Unexpected {err=}, {type(err)=}")
    raise
```

## Raise Exceptions
The raise statement allows the programmer to force a specified exception to occur. For example:
`raise NameError('HiThere')`
The sole argument to raise indicates the exception to be raised. This must be either an exception instance or an exception class (a class that derives from BaseException, such as Exception or one of its subclasses). If an exception class is passed, it will be implicitly instantiated by calling its constructor with no arguments:
```python
try:
    raise NameError('HiThere')
except NameError:
    print('An exception flew by!')
    raise
```

## Exception Chaining
If an unhandled execption ccurs inside an except section, it will have the excepton being handled attached to it and included in the error message:
```python
def func():
    raise ConnectionError

try:
    func()
except ConnectionError as exc:
    raise RuntimeError("Failed to open dfatabase") from exc
```

to disabling automatic exception chaining:
```python
try:
    open('database.sqlite')
except OSError:
    raise RuntimeError from None
```

## User-defined exceptions
Exceptions tipically derived from the Exception class, are they ussauly kept simple often only offering a number of attributes that allow information about the error to be extracted by handlers for the exception.

## Defining Clean-up actions
```python
try:
    raise KeyboardInterrupt
finally:
    print('Goodbye world!')
```

```python
def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("division by zero!")
    else:
        print("result is", result)
    finally:
        print("executing finally clause")
```