#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2019 tribe29 GmbH - License: GNU General Public License v2
# This file is part of Checkmk (https://checkmk.com). It is subject to the terms and
# conditions defined in the file COPYING, which is part of this source code package.

# yapf: disable
# type: ignore

checkname = 'mcdata_fcport'

info = [
    [u'1', u'2', u'4',
      [0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0],
     u'0'],
     [u'2', u'2', u'4',
      [0, 0, 1, 146, 209, 24, 114, 84],
      [0, 0, 0, 0, 27, 195, 137, 220],
      [0, 0, 0, 0, 198, 226, 194, 153],
      [0, 0, 0, 0, 1, 249, 185, 120],
      [0, 0, 0, 0, 0, 0, 0, 0],
      u'0'],
     [u'3', u'2', u'4',
      [0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0],
      u'0'],
     [u'4', u'1', u'3',
      [0, 0, 0, 206, 52, 216, 23, 125],
      [0, 0, 1, 45, 15, 151, 25, 6],
      [0, 0, 0, 0, 124, 38, 131, 233],
      [0, 0, 0, 0, 179, 225, 130, 129],
      [0, 0, 0, 0, 0, 0, 0, 0],
      u'0'],
     [u'5', u'1', u'3',
      [0, 0, 0, 0, 0, 0, 1, 195],
      [0, 0, 0, 0, 0, 0, 6, 59],
      [0, 0, 0, 0, 0, 0, 0, 20],
      [0, 0, 0, 0, 0, 0, 0, 114],
      [0, 0, 0, 0, 0, 0, 0, 0],
      u'0'],
     [u'6', u'1', u'3',
      [0, 0, 1, 102, 20, 94, 124, 202],
      [0, 0, 1, 142, 190, 90, 137, 237],
      [0, 0, 0, 0, 180, 4, 255, 21],
      [0, 0, 0, 0, 201, 208, 226, 62],
      [0, 0, 0, 0, 0, 0, 0, 0],
      u'0'],
     [u'7', u'1', u'3',
      [0, 0, 3, 77, 93, 88, 131, 177],
      [0, 0, 5, 2, 97, 82, 236, 151],
      [0, 0, 0, 1, 165, 57, 199, 211],
      [0, 0, 0, 2, 128, 36, 34, 231],
      [0, 0, 0, 0, 0, 0, 0, 0],
      u'0'],
     [u'8', u'2', u'4',
      [0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0],
      u'0'],
     [u'9', u'2', u'4',
      [0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0],
      u'0'],
     [u'10', u'2', u'4',
      [0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0],
      u'0'],
]


discovery = {
    '': [
        ('04', "{'state': ['1'], 'speed': 2000000000}"),
        ('05', "{'state': ['1'], 'speed': 2000000000}"),
        ('06', "{'state': ['1'], 'speed': 2000000000}"),
        ('07', "{'state': ['1'], 'speed': 2000000000}"),
    ]
}


freeze_time = "1970-01-01 00:01"


MB = 1024**2

mock_item_state = {
    '': {
        'if.in.04': (0.0, 6116281794924 - 300 * MB),
        'if.inmcast.04': (0.0, 0),
        'if.inbcast.04': (0.0, 0),
        'if.inucast.04': (0.0, 3346958079 - 60 * MB),
        'if.innucast.04': (0.0, 0),
        'if.indisc.04': (0.0, 0),
        'if.inerr.04': (0.0, 0),
        'if.out.04': (0.0, 4067529216280 - 180 * MB),
        'if.outmcast.04': (0.0, 0),
        'if.outbcast.04': (0.0, 0),
        'if.outucast.04': (0.0, 2310296998 - 30 * MB),
        'if.outnucast.04': (0.0, 0),
        'if.outdisc.04': (0.0, 0),
        'if.outerr.04': (0.0, 0),
    },
}

DEFAULT_PARAMS = {
    'state': ['1'],
    'errors': (0.01, 0.1),
    'speed': 2000000000
}

checks = {
    '': [
        ('04', DEFAULT_PARAMS, [
            (0, '[04] (up) 2 Gbit/s, In: 5.00 MB/s (2.1%), Out: 3.00 MB/s (1.3%)', [
                ('in', 5 * MB, None, None, 0, 250000000.0),
                ('inmcast', 0.0, None, None, None, None),
                ('inbcast', 0.0, None, None, None, None),
                ('inucast', MB, None, None, None, None),
                ('innucast', 0.0, None, None, None, None),
                ('indisc', 0.0, None, None, None, None),
                ('inerr', 0.0, 0.01, 0.1, None, None),
                ('out', 3 * MB, None, None, 0, 250000000.0),
                ('outmcast', 0.0, None, None, None, None),
                ('outbcast', 0.0, None, None, None, None),
                ('outucast', 0.5 * MB, None, None, None, None),
                ('outnucast', 0.0, None, None, None, None),
                ('outdisc', 0.0, None, None, None, None),
                ('outerr', 0.0, 0.01, 0.1, None, None),
                ('outqlen', 0, None, None, None, None),
            ]),
        ]),
        ('05', DEFAULT_PARAMS, [
            (0, '[05] (up) 2 Gbit/s', [
            ]),
        ]),
    ]
}
