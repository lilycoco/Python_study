# クラスの定義
class MyClass(object):
    pass

# クラスからインスタンスを生成
me = MyClass()
print(me) # => <__main__.MyClass object at 0x100799b00>


#*************************************************************************

# 何も要素を持たないクラス
class EmptyClass(object):
    pass

# 要素を好きなように定義できるので、複数の変数をまとめた入れ物として扱える
holder = EmptyClass()
holder.name = "Ryoko"
holder.age = 28
print(holder.name, holder.age) # => Ryoko 28

#*************************************************************************

class MyClass2(object):
    # クラス直下に定義した変数はインスタンス変数ではなく、クラス変数
    # some_field = "aaa"

    # インスタンス生成時に、値を渡すことができる
    def __init__(self, name, age):
        # 「self.xxx」でインスタンス変数の参照/代入ができる
        self.name = name
        self.age = age

    # インスタンスメソッドの定義
    def introduce(self):
        print("My name is %s, %d years old." % (self.name, self.age))
    
# インスタンス化
me = MyClass2('Ryoko', 28)
me.introduce() # => My name is Ryoko, 28 years old.

# 直接値を代入することもできる
me.name = "Taro"
me.age = 25
me.introduce() # => My name is Taro, 25 years old.

#*************************************************************************

class MyClass3(object):
    # クラス直下に定義すると、クラス変数になる
    primary_key = "id"

    # クラスメソッドは「@classmethod」を付与して定義する
    @classmethod
    def show_primary_key(cls):
        print("PrimayKey is %s" % cls.primary_key)

# クラス変数やクラスメソッドへのアクセスは、インスタンス化する必要ない
print(MyClass3.primary_key) # => id
MyClass3.show_primary_key() # => PrimayKey is id

#*************************************************************************

class MyClass4(object):
    primary_key = "id"

    @classmethod
    def show1(cls):
        print(cls.primary_key)

    # スタティックメソッドは「@staticmethod」を付与して関数を定義します
    @staticmethod
    def show2():
        print(MyClass4.primary_key)

MyClass4.show1() # => id
MyClass4.show2() # => id

class MySubClass(MyClass4):
    primary_key = "subid"

MySubClass.show1() # => subid
MySubClass.show2() # => id

#*************************************************************************

# 人を表すクラス
class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def sayHi(self):
        print("Hi, my name is %s, %d years old." % (self.name, self.age))

# 仕事人を表すクラス
class Worker(Person):
    def __init__(self, name, age, skills):
        # 親クラスの関数を使う場合には、super()を使う
        super().__init__(name, age)
        self.skills = skills
    def show_skills(self):
        # 親クラスの変数も参照できる
        print("%s's skills are %s" % (self.name, self.skills))

# インスタンス化
w = Worker("Yohei", 30, ["html","js","css"])
# 親クラスのメソッドも呼び出せる
w.sayHi()
w.show_skills()

#*************************************************************************
