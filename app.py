import src.visualize as viz

server = viz.app.server

if __name__ == '__main__':
    viz.app.run_server(debug=True)