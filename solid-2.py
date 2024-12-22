from abc import ABC, abstractmethod

# Single Responsibility Principle (SRP): كل كلاس له مسؤولية واحدة
class Animal:
    def __init__(self, name):
        self.name = name

    def description(self):
        return f"This is {self.name}."

# Open/Closed Principle (OCP): يمكن إضافة حيوانات جديدة دون تعديل الكود القديم
class Bird(Animal):
    def fly(self):
        return f"{self.name} is flying."

class Penguin(Animal):
    def swim(self):
        return f"{self.name} is swimming."

# Liskov Substitution Principle (LSP): جميع الحيوانات يمكن استخدامها بنفس الطريقة
class AnimalActions(ABC):
    @abstractmethod
    def perform_action(self):
        pass

class FlyingBirdAction(AnimalActions):
    def __init__(self, bird):
        self.bird = bird

    def perform_action(self):
        return self.bird.fly()

class SwimmingAnimalAction(AnimalActions):
    def __init__(self, animal):
        self.animal = animal

    def perform_action(self):
        return self.animal.swim()

# Interface Segregation Principle (ISP): كل واجهة تلبي وظيفة محددة فقط
class AnimalNotifier(ABC):
    @abstractmethod
    def send_notification(self, message):
        pass

class ConsoleNotifier(AnimalNotifier):
    def send_notification(self, message):
        print(f"Console Notification: {message}")

# Dependency Inversion Principle (DIP): الاعتماد على التجريد بدل التفاصيل
class AnimalManager:
    def __init__(self, action: AnimalActions, notifier: AnimalNotifier):
        self.action = action
        self.notifier = notifier

    def manage_animal(self):
        action_result = self.action.perform_action()
        self.notifier.send_notification(action_result)
        return action_result

# Example Usage
if __name__ == "__main__":
    # إنشاء الحيوانات
    sparrow = Bird("Sparrow")
    penguin = Penguin("Penguin")

    # إشعار على الكونسول
    notifier = ConsoleNotifier()

    # إدارة الطائر الطائر
    bird_action = FlyingBirdAction(sparrow)
    bird_manager = AnimalManager(bird_action, notifier)
    print(bird_manager.manage_animal())

    # إدارة البطريق السباح
    penguin_action = SwimmingAnimalAction(penguin)
    penguin_manager = AnimalManager(penguin_action, notifier)
    print(penguin_manager.manage_animal())
