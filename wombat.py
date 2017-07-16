import argparse
import wrapper.core


with open('api.cfg', 'r') as key:
  ap_key = key.read( )
api = wrapper.core.PUBGAPI(ap_key)