{"changed":true,"filter":false,"title":"recipe.py","tooltip":"/recipe.py","value":"","undoManager":{"mark":-2,"position":1,"stack":[[{"start":{"row":0,"column":0},"end":{"row":16,"column":46},"action":"insert","lines":["import os","from flask import Flask","#sets up application for use with flask functionality","","app = Flask(__name__)","#creates application to be tested","","","@app.route('/')","#Display text as proof of concept","def fromscratch():","    return \"FROM Scratch test\"","","","if __name__ == '__main__':","    app.run(debug=True)","#So they know how and where to run application"],"id":1}],[{"start":{"row":0,"column":0},"end":{"row":16,"column":46},"action":"remove","lines":["import os","from flask import Flask","#sets up application for use with flask functionality","","app = Flask(__name__)","#creates application to be tested","","","@app.route('/')","#Display text as proof of concept","def fromscratch():","    return \"FROM Scratch test\"","","","if __name__ == '__main__':","    app.run(debug=True)","#So they know how and where to run application"],"id":2}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":0,"column":0},"end":{"row":0,"column":0},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1571842520188}