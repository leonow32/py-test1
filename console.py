#!/usr/bin/env python

def SayHello():
    name = input(u"Podaj imię: ")
    print("Hello " + name)
    print("Nowa linia " + name)

def main():
    print("Witamy w funkcji main")
    while True:
        cmd = input("> ")
        
        if cmd == "exit":
            break
            
        elif cmd == "name":
            SayHello()
            
        elif cmd == "test":
            print("Hello")

if __name__ == "__main__":
	main()
    
def test():
    print("Witamy w funkcji test")
    
print("Koniec pliku")
