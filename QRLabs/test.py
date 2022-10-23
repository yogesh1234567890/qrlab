import requests
API_ENDPOINT = "https://qrsample.qrlab.co/api/generate/qrcode"
data = {
    "link_data": "https://digi.com",
    "bg_color": "#ffffff",
    "frontcolor": "#000000",
    "gradient_color": "#000000",
    "marker_out_color": "#000000",
    "marker_in_color": "#000000",
    "custom_logo": "",
    "framecolor": "#000000",
    "pattern": "default",
    "marker_out": "default",
    "marker_in": "default",
    "optionlogo": "none",
    "outer_frame": "none",
    "framelabel": "",
    "label_font": "AbrilFatface.svg",
    "type": "link"
}
r = requests.post(url=API_ENDPOINT, data=data)
tex = r.json()
print(tex)
