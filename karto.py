from kartograph import Kartograph
from kartograph.options import read_map_config
import sys
cfg=read_map_config(open("map.json"))
K = Kartograph()
K.generate(cfg, outfile='level3_wgs84.svg',format='svg')
