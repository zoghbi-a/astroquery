# Licensed under a 3-clause BSD style license - see LICENSE.rst
"""
=============
TAP plus
=============

@author: Juan Carlos Segovia
@contact: juan.carlos.segovia@sciops.esa.int

European Space Astronomy Centre (ESAC)
European Space Agency (ESA)

Created on 30 jun. 2016


"""


import os


def get_package_data():
    paths = [os.path.join('data', '*.data'),
             os.path.join('data', '*.xml'),
             os.path.join('data', '*.json'),
             os.path.join('data', '*.csv'),
             os.path.join('data', '*.ecsv'),
             os.path.join('data', '*.vot')
             ]
    return {'astroquery.utils.tap.xmlparser.tests': paths}
