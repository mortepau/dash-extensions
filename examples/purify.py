import dash
from dash_extensions import Purify

app = dash.Dash()
app.layout = Purify("This is <b>html</b>")

if __name__ == "__main__":
    app.run_server(port=9999)
