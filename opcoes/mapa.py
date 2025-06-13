from models.local import Local
from tags.map import MapLeaflet


class Mapa():
    def __init__(self):
        self.local = Local()

    def get_map(self):
        lista = self.local.read_all()
        mapa = MapLeaflet(name_id="mapLocal",
                          height="600px",
                          width="90%",
                          zoom_level=13
                          )
        for local in lista:
            mapa.add_point(local.lat_local, local.lgt_local, name=local.nme_local,
                           popup_content=f"""Local: {local.nme_local} <br>
                                            Status:{local.sts_local}""")
        return (mapa.get_html(), mapa.get_javascript())
