import os
import src.visualize as viz

server = viz.app.server
import src.getData as gd

if (os.path.isdir("data")):
    _,_ = gd.updateGlobalData()
else:
    os.mkdir("data")
    _,_ = gd.updateGlobalData()

if __name__ == '__main__':
    viz.app.run_server(debug=True)