from typing import overload, Union

class Animal:
    def speak(self, sound: str) -> None:
        print(f"Animal says: {sound}")

class Dog(Animal):
    @overload
    def speak(self, sound: str) -> None: ...
    @overload
    def speak(self, times: int) -> None: ...
    def speak(self, arg: Union[str, int]) -> None:
        if isinstance(arg, str):
            print(f"Dog says: {arg}")
        elif isinstance(arg, int):
            print("Woof! " * arg)
        else:
            raise TypeError("Invalid argument type")
d = Dog()
d.speak("Bark!")   # Output: Dog says: Bark!
d.speak(3)         # Output: Woof! Woof! Woof!