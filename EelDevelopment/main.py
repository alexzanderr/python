

import eel


@eel.expose
def  python_to_javascript(parametru):
    print("console.log() can pe used like this\nhere")
    print(f"parametru was printed: {parametru}")



eel.init("web_interface")
eel.start("index.html", block=False)



x = eel.javascript_into_python()()
print(x)
