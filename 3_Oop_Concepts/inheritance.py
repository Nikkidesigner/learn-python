class A:
    def info_a(self):
        print("Class 'A' method")
class B:
    def info_b(self):
        print("Class 'B' method")
class C(A,B):
    def info_c(self):
        print("Class 'C' method")

obj_c=C()
obj_c.info_a()
obj_c.info_b()
obj_c.info_c()