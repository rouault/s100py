from collections import namedtuple
import pytest

import os

import datetime
import numpy
import h5py

from s100py import s104

path_to_current_file = os.path.realpath(__file__)
current_directory = os.path.dirname(path_to_current_file)
path_to_s104file = os.path.join(current_directory, "test_s104.h5")


def h5py_string_comp(h5py_val, cmp_str):
    # h5py <3.0 returns a string, >3.0 returns bytes
    return h5py_val in (cmp_str, bytes(cmp_str, "utf-8"))


InputData = namedtuple(
    'InputData',
    ['height_001',
     'trend_001',
     'height_002',
     'trend_002',
     'grid_properties',
     'metadata',
     'datetime_value',
     'data_coding_format',
     'update_meta',
     'expected_chunks',
     'expected_groupf'])


@pytest.fixture
def input_data():
    height_001 = numpy.array([[ 0.34,  0.34,  0.34,  0.34,  0.34,  0.34,  0.34,  0.34,  0.34,
         0.34,  0.34,  0.34,  0.34,  0.34,  0.34,  0.34,  0.34,  0.34,
         0.34,  0.34,  0.34,  0.34,  0.34,  0.34,  0.34,  0.34,  0.34,
         0.34,  0.34,  0.34,  0.34,  0.34,  0.34,  0.34,  0.34,  0.34,
         0.34,  0.34,  0.34,  0.34,  0.34,  0.34,  0.34,  0.34,  0.34,
         0.34,  0.34,  0.34,  0.34,  0.34,  0.34,  0.34,  0.34,  0.34,
         0.34,  0.34,  0.34,  0.34,  0.34,  0.34,  0.34,  0.34,  0.34,
         0.34,  0.34,  0.34,  0.34,  0.34,  0.34,  0.34,  0.34,  0.34,
         0.34,  0.35,  0.35,  0.35,  0.35,  0.35,  0.35,  0.35,  0.35,
         0.35,  0.35,  0.35,  0.35,  0.35,  0.35,  0.35,  0.35,  0.35,
         0.35,  0.35,  0.35,  0.35,  0.35,  0.35,  0.35,  0.35,  0.35,
         0.35,  0.35,  0.35,  0.35,  0.35,  0.35,  0.35,  0.35,  0.35,
         0.35,  0.35,  0.35,  0.35,  0.35,  0.35,  0.35,  0.35,  0.35,
         0.35,  0.35,  0.35,  0.35,  0.35,  0.35,  0.35,  0.35,  0.35,
         0.35,  0.35,  0.35,  0.35,  0.35,  0.35,  0.35,  0.35,  0.35,
         0.35,  0.35,  0.35,  0.35,  0.35,  0.35,  0.35,  0.35,  0.35,
         0.35,  0.35,  0.35,  0.35,  0.35,  0.35,  0.35,  0.35,  0.35,
         0.35,  0.35,  0.35,  0.35,  0.35,  0.35,  0.35,  0.35,  0.35,
         0.35,  0.35,  0.35,  0.35,  0.35,  0.35,  0.35,  0.35,  0.35,
         0.35,  0.35,  0.35,  0.35,  0.35,  0.35,  0.35,  0.35,  0.35,
         0.35,  0.35,  0.35,  0.35,  0.35,  0.35,  0.35,  0.35,  0.35,
         0.35,  0.35,  0.35,  0.35,  0.35,  0.35,  0.35,  0.35,  0.35,
         0.35,  0.35,  0.35,  0.35,  0.35,  0.35,  0.35,  0.35,  0.35,
         0.35,  0.35,  0.35,  0.35,  0.35,  0.35,  0.35,  0.35,  0.35,
         0.35,  0.35,  0.35,  0.35,  0.35,  0.35,  0.35,  0.35,  0.35,
         0.35,  0.35,  0.35,  0.35,  0.35,  0.35,  0.35,  0.35,  0.35,
         0.35,  0.35,  0.35,  0.35,  0.35,  0.35,  0.35,  0.35,  0.35,
         0.35,  0.35,  0.35,  0.35,  0.35,  0.35,  0.35,  0.35,  0.35,
         0.35,  0.35,  0.35,  0.35,  0.35,  0.35,  0.35,  0.35,  0.35,
         0.35,  0.35,  0.35,  0.35,  0.35,  0.35,  0.35,  0.35,  0.37,
         0.45,  0.44,  0.48,  0.  ,  0.  ,  0.  ,  0.  ,  0.  ,  0.44,
         0.43,  0.45,  0.36,  0.35,  0.35,  0.35,  0.35,  0.35,  0.35,
         0.35,  0.35,  0.35,  0.35,  0.35,  0.35,  0.35,  0.35,  0.35,
         0.35,  0.35,  0.35,  0.35,  0.35,  0.35,  0.35,  0.35,  0.35,
         0.35,  0.35,  0.35,  0.35,  0.35,  0.35,  0.35,  0.35,  0.35,
         0.35,  0.35,  0.35,  0.35,  0.35,  0.35,  0.35,  0.35,  0.35,
         0.35,  0.35,  0.35,  0.35,  0.35,  0.35,  0.35,  0.35,  0.35,
         0.35,  0.35,  0.35,  0.35,  0.35,  0.35,  0.35,  0.35,  0.35,
         0.35,  0.35,  0.35,  0.35,  0.35,  0.35,  0.35,  0.35,  0.35,
         0.35,  0.35], [ 0.34,  0.34,  0.34,  0.34,  0.34,  0.34,  0.34,  0.34,  0.34,
         0.34,  0.34,  0.34,  0.34,  0.34,  0.34,  0.34,  0.34,  0.34,
         0.34,  0.34,  0.34,  0.34,  0.34,  0.34,  0.34,  0.34,  0.34,
         0.34,  0.34,  0.34,  0.34,  0.34,  0.34,  0.34,  0.34,  0.34,
         0.34,  0.34,  0.34,  0.34,  0.34,  0.34,  0.34,  0.34,  0.34,
         0.34,  0.34,  0.34,  0.34,  0.34,  0.34,  0.34,  0.34,  0.34,
         0.34,  0.34,  0.34,  0.34,  0.34,  0.34,  0.34,  0.34,  0.34,
         0.34,  0.34,  0.34,  0.34,  0.34,  0.34,  0.34,  0.34,  0.34,
         0.35,  0.35,  0.35,  0.35,  0.35,  0.35,  0.35,  0.35,  0.35,
         0.35,  0.35,  0.35,  0.35,  0.35,  0.35,  0.35,  0.35,  0.35,
         0.35,  0.35,  0.35,  0.35,  0.35,  0.35,  0.35,  0.35,  0.35,
         0.35,  0.35,  0.35,  0.35,  0.35,  0.35,  0.35,  0.35,  0.35,
         0.35,  0.35,  0.35,  0.35,  0.35,  0.35,  0.35,  0.35,  0.35,
         0.35,  0.35,  0.35,  0.35,  0.35,  0.35,  0.35,  0.35,  0.35,
         0.35,  0.35,  0.35,  0.35,  0.35,  0.35,  0.35,  0.35,  0.35,
         0.35,  0.35,  0.35,  0.35,  0.35,  0.35,  0.35,  0.35,  0.35,
         0.35,  0.35,  0.35,  0.35,  0.35,  0.35,  0.35,  0.35,  0.35,
         0.35,  0.35,  0.35,  0.35,  0.35,  0.35,  0.35,  0.35,  0.35,
         0.35,  0.35,  0.35,  0.35,  0.35,  0.35,  0.35,  0.35,  0.35,
         0.35,  0.35,  0.35,  0.35,  0.35,  0.35,  0.35,  0.35,  0.35,
         0.35,  0.35,  0.35,  0.35,  0.35,  0.35,  0.35,  0.35,  0.35,
         0.35,  0.35,  0.35,  0.35,  0.35,  0.35,  0.35,  0.35,  0.35,
         0.35,  0.35,  0.35,  0.35,  0.35,  0.35,  0.35,  0.35,  0.35,
         0.35,  0.35,  0.35,  0.35,  0.35,  0.35,  0.35,  0.35,  0.35,
         0.35,  0.35,  0.35,  0.35,  0.35,  0.35,  0.35,  0.35,  0.35,
         0.35,  0.35,  0.35,  0.35,  0.35,  0.35,  0.35,  0.35,  0.35,
         0.35,  0.35,  0.35,  0.35,  0.35,  0.35,  0.35,  0.35,  0.35,
         0.35,  0.35,  0.35,  0.35,  0.35,  0.35,  0.35,  0.35,  0.35,
         0.35,  0.35,  0.35,  0.35,  0.35,  0.35,  0.35,  0.35,  0.35,
         0.35,  0.35,  0.35,  0.35,  0.35,  0.35,  0.35,  0.35,  0.35,
         0.37,  0.37,  0.42,  0.46,  0.48,  0.49,  0.  ,  0.  ,  0.45,
         0.45,  0.38,  0.35,  0.35,  0.35,  0.35,  0.35,  0.35,  0.35,
         0.35,  0.35,  0.35,  0.35,  0.35,  0.35,  0.35,  0.35,  0.35,
         0.35,  0.35,  0.35,  0.35,  0.35,  0.35,  0.35,  0.35,  0.35,
         0.35,  0.35,  0.35,  0.35,  0.35,  0.35,  0.35,  0.35,  0.35,
         0.35,  0.35,  0.35,  0.35,  0.35,  0.35,  0.35,  0.35,  0.35,
         0.35,  0.35,  0.35,  0.35,  0.35,  0.35,  0.35,  0.35,  0.35,
         0.35,  0.35,  0.35,  0.35,  0.35,  0.35,  0.35,  0.35,  0.35,
         0.35,  0.35,  0.35,  0.35,  0.35,  0.35,  0.35,  0.35,  0.35,
         0.35,  0.35]])

    trend_001 = numpy.array([[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
        1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
        1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
        1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
        1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
        1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
        1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
        1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3, 3, 3, 3, 3, 3,
        3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3,
        3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3,
        3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3,
        3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3,
        3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3,
        3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3,
        3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3,
        3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3,
        3], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
        1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
        1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
        1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
        1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
        1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
        1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
        1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3, 3, 3, 3, 3,
        3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3,
        3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3,
        3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3,
        3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3,
        3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3,
        3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3,
        3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3,
        3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3,
        3]])

    height_002 = numpy.array([[ 0.1 ,  0.1 ,  0.1 ,  0.1 ,  0.1 ,  0.1 ,  0.1 ,  0.1 ,  0.1 ,
         0.1 ,  0.1 ,  0.1 ,  0.1 ,  0.1 ,  0.1 ,  0.1 ,  0.1 ,  0.1 ,
         0.1 ,  0.1 ,  0.1 ,  0.1 ,  0.1 ,  0.1 ,  0.1 ,  0.1 ,  0.1 ,
         0.1 ,  0.1 ,  0.1 ,  0.1 ,  0.1 ,  0.1 ,  0.1 ,  0.1 ,  0.1 ,
         0.1 ,  0.1 ,  0.1 ,  0.1 ,  0.1 ,  0.1 ,  0.1 ,  0.1 ,  0.1 ,
         0.1 ,  0.1 ,  0.1 ,  0.1 ,  0.1 ,  0.1 ,  0.1 ,  0.1 ,  0.11,
         0.11,  0.11,  0.11,  0.11,  0.11,  0.11,  0.11,  0.11,  0.11,
         0.11,  0.11,  0.11,  0.11,  0.11,  0.11,  0.11,  0.11,  0.11,
         0.11,  0.11,  0.11,  0.11,  0.11,  0.11,  0.11,  0.11,  0.11,
         0.11,  0.11,  0.11,  0.11,  0.11,  0.11,  0.11,  0.11,  0.11,
         0.11,  0.11,  0.11,  0.11,  0.11,  0.11,  0.11,  0.11,  0.11,
         0.11,  0.11,  0.11,  0.11,  0.11,  0.11,  0.11,  0.11,  0.11,
         0.11,  0.11,  0.11,  0.11,  0.11,  0.11,  0.11,  0.11,  0.11,
         0.11,  0.11,  0.11,  0.11,  0.11,  0.11,  0.11,  0.11,  0.11,
         0.11,  0.11,  0.11,  0.11,  0.12,  0.12,  0.12,  0.12,  0.12,
         0.12,  0.12,  0.12,  0.12,  0.12,  0.12,  0.12,  0.12,  0.12,
         0.12,  0.12,  0.12,  0.12,  0.12,  0.12,  0.12,  0.12,  0.12,
         0.12,  0.12,  0.12,  0.12,  0.12,  0.12,  0.12,  0.12,  0.12,
         0.12,  0.12,  0.12,  0.12,  0.12,  0.12,  0.12,  0.12,  0.12,
         0.12,  0.12,  0.12,  0.12,  0.12,  0.12,  0.12,  0.12,  0.12,
         0.12,  0.12,  0.12,  0.12,  0.12,  0.12,  0.12,  0.12,  0.12,
         0.12,  0.12,  0.12,  0.12,  0.12,  0.12,  0.12,  0.12,  0.12,
         0.12,  0.12,  0.12,  0.12,  0.12,  0.12,  0.12,  0.12,  0.12,
         0.12,  0.12,  0.13,  0.13,  0.13,  0.13,  0.13,  0.13,  0.13,
         0.13,  0.13,  0.13,  0.13,  0.13,  0.13,  0.13,  0.13,  0.13,
         0.13,  0.13,  0.13,  0.13,  0.13,  0.13,  0.13,  0.13,  0.13,
         0.13,  0.13,  0.13,  0.13,  0.13,  0.13,  0.13,  0.13,  0.13,
         0.13,  0.13,  0.13,  0.13,  0.13,  0.13,  0.13,  0.13,  0.13,
         0.13,  0.13,  0.13,  0.13,  0.13,  0.13,  0.13,  0.13,  0.13,
         0.13,  0.13,  0.13,  0.13,  0.13,  0.13,  0.13,  0.13,  0.16,
         0.23,  0.22,  0.26,  0.  ,  0.  ,  0.  ,  0.  ,  0.  ,  0.24,
         0.23,  0.25,  0.15,  0.14,  0.14,  0.14,  0.14,  0.14,  0.14,
         0.14,  0.14,  0.14,  0.14,  0.13,  0.13,  0.13,  0.13,  0.13,
         0.13,  0.13,  0.13,  0.13,  0.13,  0.13,  0.13,  0.13,  0.13,
         0.13,  0.13,  0.13,  0.13,  0.13,  0.13,  0.13,  0.13,  0.13,
         0.13,  0.13,  0.13,  0.13,  0.13,  0.13,  0.13,  0.13,  0.13,
         0.13,  0.13,  0.13,  0.13,  0.13,  0.13,  0.13,  0.13,  0.13,
         0.13,  0.13,  0.13,  0.13,  0.13,  0.13,  0.13,  0.13,  0.13,
         0.13,  0.13,  0.14,  0.14,  0.14,  0.14,  0.14,  0.14,  0.14,
         0.14,  0.14], [ 0.1 ,  0.1 ,  0.1 ,  0.1 ,  0.1 ,  0.1 ,  0.1 ,  0.1 ,  0.1 ,
         0.1 ,  0.1 ,  0.1 ,  0.1 ,  0.1 ,  0.1 ,  0.1 ,  0.1 ,  0.1 ,
         0.1 ,  0.1 ,  0.1 ,  0.1 ,  0.1 ,  0.1 ,  0.1 ,  0.1 ,  0.1 ,
         0.1 ,  0.1 ,  0.1 ,  0.1 ,  0.1 ,  0.1 ,  0.1 ,  0.1 ,  0.1 ,
         0.1 ,  0.1 ,  0.1 ,  0.1 ,  0.1 ,  0.1 ,  0.1 ,  0.1 ,  0.1 ,
         0.1 ,  0.1 ,  0.1 ,  0.1 ,  0.1 ,  0.1 ,  0.1 ,  0.1 ,  0.11,
         0.11,  0.11,  0.11,  0.11,  0.11,  0.11,  0.11,  0.11,  0.11,
         0.11,  0.11,  0.11,  0.11,  0.11,  0.11,  0.11,  0.11,  0.11,
         0.11,  0.11,  0.11,  0.11,  0.11,  0.11,  0.11,  0.11,  0.11,
         0.11,  0.11,  0.11,  0.11,  0.11,  0.11,  0.11,  0.11,  0.11,
         0.11,  0.11,  0.11,  0.11,  0.11,  0.11,  0.11,  0.11,  0.11,
         0.11,  0.11,  0.11,  0.11,  0.11,  0.11,  0.11,  0.11,  0.11,
         0.11,  0.11,  0.11,  0.11,  0.11,  0.11,  0.11,  0.11,  0.11,
         0.11,  0.11,  0.11,  0.11,  0.11,  0.11,  0.11,  0.11,  0.11,
         0.11,  0.11,  0.11,  0.11,  0.12,  0.12,  0.12,  0.12,  0.12,
         0.12,  0.12,  0.12,  0.12,  0.12,  0.12,  0.12,  0.12,  0.12,
         0.12,  0.12,  0.12,  0.12,  0.12,  0.12,  0.12,  0.12,  0.12,
         0.12,  0.12,  0.12,  0.12,  0.12,  0.12,  0.12,  0.12,  0.12,
         0.12,  0.12,  0.12,  0.12,  0.12,  0.12,  0.12,  0.12,  0.12,
         0.12,  0.12,  0.12,  0.12,  0.12,  0.12,  0.12,  0.12,  0.12,
         0.12,  0.12,  0.12,  0.12,  0.12,  0.12,  0.12,  0.12,  0.12,
         0.12,  0.12,  0.12,  0.12,  0.12,  0.12,  0.12,  0.12,  0.12,
         0.12,  0.12,  0.12,  0.12,  0.12,  0.12,  0.12,  0.12,  0.12,
         0.12,  0.12,  0.13,  0.13,  0.13,  0.13,  0.13,  0.13,  0.13,
         0.13,  0.13,  0.13,  0.13,  0.13,  0.13,  0.13,  0.13,  0.13,
         0.13,  0.13,  0.13,  0.13,  0.13,  0.13,  0.13,  0.13,  0.13,
         0.13,  0.13,  0.13,  0.13,  0.13,  0.13,  0.13,  0.13,  0.13,
         0.13,  0.13,  0.13,  0.13,  0.13,  0.13,  0.13,  0.13,  0.13,
         0.13,  0.13,  0.13,  0.13,  0.13,  0.13,  0.13,  0.13,  0.13,
         0.13,  0.13,  0.13,  0.13,  0.13,  0.13,  0.13,  0.13,  0.13,
         0.15,  0.15,  0.2 ,  0.24,  0.25,  0.26,  0.  ,  0.  ,  0.25,
         0.24,  0.17,  0.14,  0.14,  0.14,  0.14,  0.14,  0.14,  0.14,
         0.14,  0.14,  0.14,  0.14,  0.13,  0.13,  0.13,  0.13,  0.13,
         0.13,  0.13,  0.13,  0.13,  0.13,  0.13,  0.13,  0.13,  0.13,
         0.13,  0.13,  0.13,  0.13,  0.13,  0.13,  0.13,  0.13,  0.13,
         0.13,  0.13,  0.13,  0.13,  0.13,  0.13,  0.13,  0.13,  0.13,
         0.13,  0.13,  0.13,  0.13,  0.13,  0.13,  0.13,  0.13,  0.13,
         0.13,  0.13,  0.13,  0.13,  0.13,  0.13,  0.13,  0.13,  0.13,
         0.13,  0.13,  0.14,  0.14,  0.14,  0.14,  0.14,  0.14,  0.14,
         0.14,  0.14]])

    trend_002 = numpy.array([[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
        1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
        1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
        1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
        1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
        1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
        1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
        1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
        1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
        1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
        1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
        1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
        1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3, 3, 3, 3, 1, 1, 1, 1, 1, 1, 1, 1,
        1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
        1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
        1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
        1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
        1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
        1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
        1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
        1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
        1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
        1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
        1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
        1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
        1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
        1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
        1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
        1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3, 1, 1, 1, 1, 1, 1, 1, 1,
        1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
        1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
        1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
        1]])

    grid_properties = {
        'maxx': 139.1660,
        'minx': 139.1932,
        'miny': 4.806799,
        'maxy': 9.593201,
        'cellsize_x': 0.013597488,
        'cellsize_y': 0.013595581,
        'nx': 2,
        'ny': 353
    }

    metadata = {
     'horizontalCRS': 3855,
     'metadata': 'MD_s104_test.XML',
     'geographicIdentifier': 'Palau',
     'waterLevelHeightUncertainty': -1.0,
     'verticalUncertainty': -1.0,
     'horizontalPositionUncertainty': -1.0,
     'timeUncertainty': -1.0,
     'waterLevelTrendThreshold': 0.02,
     'verticalCS': 6499,
     'verticalCoordinateBase': 2,
     'verticalDatumReference': 2,
     'verticalDatum': 1027,
     'commonPointRule': 4,
     'interpolationType': 10,
     'typeOfWaterLevelData': 5,
     'methodWaterLevelProduct': 'ADCIRC_Hydrodynamic_Model_Forecasts',
     'datetimeOfFirstRecord': '2020-09-26T16:00:00'

    }

    datetime_value = datetime.datetime(2020, 9, 26, 15, 0, 0)

    data_coding_format = 2

    update_meta = {
        'dateTimeOfLastRecord': '2020-09-26T17:00:00',
        'numberOfGroups': 2,
        'numberOfTimes': 2,
        'timeRecordInterval': 3600,
        'num_instances': 1
    }

    expected_chunks = '2,353'

    expected_groupf = numpy.array([
        ('waterLevelHeight', 'Water level height', 'meters', '-9999', 'H5T_FLOAT', '-99.99', '99.99', 'closedInterval'),
        ('waterLevelTrend', 'Water level trend', '', '0', 'H5T_ENUM', '1', '3', 'closedInterval'),
        ('waterLevelTime', 'Water level time', 'DateTime', '', 'H5T_C_S1', '19000101T000000Z', '21500101T000000Z', 'closedInterval')],
        dtype=[('code', 'O'), ('name', 'O'), ('uom.name', 'O'), ('fillValue', 'O'), ('datatype', 'O'), ('lower', 'O'), ('upper', 'O'), ('closure', 'O')])

    return InputData(height_001, trend_001, height_002, trend_002, grid_properties, metadata, datetime_value, data_coding_format, update_meta, expected_chunks, expected_groupf)


def test_create_s104_dcf2(input_data):
    data_file = s104.utils.create_s104(path_to_s104file)

    s104.utils.add_metadata(input_data.metadata, data_file)
    s104.utils.add_data_from_arrays(input_data.height_001, input_data.trend_001, data_file, input_data.grid_properties,
                                    input_data.datetime_value, input_data.data_coding_format)
    s104.utils.add_data_from_arrays(input_data.height_002, input_data.trend_002, data_file, input_data.grid_properties,
                                    input_data.datetime_value, input_data.data_coding_format)
    s104.utils.update_metadata(data_file, input_data.grid_properties, input_data.update_meta)

    s104.utils.write_data_file(data_file)

    assert os.path.isfile(path_to_s104file)
    h5_file = h5py.File(path_to_s104file, "r")

    assert 'Group_F/WaterLevel' in h5_file
    assert 'Group_F/featureCode' in h5_file
    assert 'WaterLevel/WaterLevel.01/uncertainty' in h5_file
    assert 'WaterLevel/axisNames' in h5_file
    assert h5_file['Group_F/WaterLevel'].attrs['chunking'] == input_data.expected_chunks
    assert numpy.allclose(h5_file['WaterLevel/WaterLevel.01/Group_001/values']['waterLevelHeight'],
                          input_data.height_001)
    assert numpy.allclose(h5_file['WaterLevel/WaterLevel.01/Group_001/values']['waterLevelTrend'],
                          input_data.trend_001)
    assert numpy.allclose(h5_file['WaterLevel/WaterLevel.01/Group_002/values']['waterLevelHeight'],
                          input_data.height_002)
    assert numpy.allclose(h5_file['WaterLevel/WaterLevel.01/Group_002/values']['waterLevelTrend'],
                          input_data.trend_002)
    assert h5_file['WaterLevel/WaterLevel.01/'].attrs['numPointsLongitudinal'] == input_data.height_001.shape[0]
    assert h5_file['WaterLevel/WaterLevel.01/'].attrs['numPointsLatitudinal'] == input_data.height_001.shape[1]

    assert all([h5py_string_comp(actual, expected) for actual, expected in zip(h5_file['Group_F/WaterLevel'][()][0],
                                                                               input_data.expected_groupf[0])])
    assert all([h5py_string_comp(actual, expected) for actual, expected in zip(h5_file['Group_F/WaterLevel'][()][1],
                                                                               input_data.expected_groupf[1])])
    assert all([h5py_string_comp(actual, expected) for actual, expected in zip(h5_file['Group_F/WaterLevel'][()][2],
                                                                               input_data.expected_groupf[2])])
