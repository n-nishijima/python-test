# coding:utf-8

from modules import module_hello_world

print("Hello World!")

module_hello_world.say()

#「__name__」の値はスクリプトとして実行された場合、「__main__」となる
if __name__ == "__main__" :
    print("Script Hello World!")
