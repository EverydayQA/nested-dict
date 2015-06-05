"""

    test_nested_dict.py

"""
from __future__ import print_function


import unittest
import sys
import os


# make sure which nested_dict we are testing
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, parent_dir)


class Test_nested_dict_default(unittest.TestCase):

    def test_default(self):
        """
            test a range of nested_dict
        """
        from nested_dict import nested_dict
        nd = nested_dict()
        nd['new jersey']['mercer county']['plumbers'] = 3
        nd['new jersey']['mercer county']['programmers'] = 81
        nd['new jersey']['middlesex county']['programmers'] = 81
        nd['new jersey']['middlesex county']['salesmen'] = 62
        nd['new york']['queens county']['plumbers'] = 9
        nd['new york']['queens county']['salesmen'] = 36
        all = sorted(tup for tup in nd.iteritems_flat())
        self.assertEqual(all, [(('new jersey', 'mercer county', 'plumbers'),        3),
                               (('new jersey', 'mercer county', 'programmers'),    81),
                               (('new jersey', 'middlesex county', 'programmers'), 81),
                               (('new jersey', 'middlesex county', 'salesmen'),    62),
                               (('new york', 'queens county', 'plumbers'),          9),
                               (('new york', 'queens county', 'salesmen'),         36)])


class Test_nested_dict_list(unittest.TestCase):

    def test_list(self):
        """
            test a range of nested_dict
        """
        import nested_dict
        nd = nested_dict.nested_dict(2, list)
        nd['new jersey']['mercer county'].append('plumbers')
        nd['new jersey']['mercer county'].append('programmers')
        nd['new jersey']['middlesex county'].append('salesmen')
        nd['new jersey']['middlesex county'].append('staff')
        nd['new york']['queens county'].append('cricketers')
        all = sorted(tup for tup in nd.iteritems_flat())
        self.assertEqual(all, [(('new jersey', 'mercer county'),    ['plumbers', 'programmers']),
                               (('new jersey', 'middlesex county'), ['salesmen', 'staff']),
                               (('new york', 'queens county'),      ['cricketers']),
                               ])
        all = sorted(tup for tup in nd.itervalues_flat())
        self.assertEqual(all, [['cricketers'],
                               ['plumbers', 'programmers'],
                               ['salesmen', 'staff']])
        all = sorted(tup for tup in nd.iterkeys_flat())
        self.assertEqual(all, [('new jersey', 'mercer county'),
                               ('new jersey', 'middlesex county'),
                               ('new york', 'queens county')])

        self.assertEqual(nd, {"new jersey": {"mercer county": ["plumbers",
                                                               "programmers"],
                                             "middlesex county": ["salesmen",
                                                                  "staff"]},
                              "new york": {"queens county": ["cricketers"]}})

    def test_iteritems_flat(self):
        """
        test iteritems_flat()
        """
        import nested_dict
        a = nested_dict.nested_dict()
        a['1']['2']['3'] = 3
        a['A']['B'] = 15
        self.assertEqual(sorted(a.iteritems_flat()), [(('1', '2', '3'), 3), (('A', 'B'), 15)])

    def test_iterkeys_flat(self):
        """
        test iterkeys_flat
        iterate through values with nested keys flattened into a tuple
        """
        import nested_dict
        a = nested_dict.nested_dict()
        a['1']['2']['3'] = 3
        a['A']['B'] = 15
        self.assertEqual(sorted(a.iterkeys_flat()), [('1', '2', '3'), ('A', 'B')])

    def test_itervalues_flat(self):
        """
        itervalues_flat
        iterate through values as a single list, without considering the degree of nesting
        """
        import nested_dict
        a = nested_dict.nested_dict()
        a['1']['2']['3'] = 3
        a['A']['B'] = 15
        self.assertEqual(sorted(a.itervalues_flat()), [3, 15])

    def test_to_dict(self):
        """
        to_dict()
        Converts the nested dictionary to a nested series of standard ``dict`` objects
        """
        import nested_dict
        a = nested_dict.nested_dict()
        a['1']['2']['3'] = 3
        a['A']['B'] = 15
        self.assertEqual(a.to_dict(), {'1': {'2': {'3': 3}}, 'A': {'B': 15}})

    def test_str(self):
        """
        str()
        """
        import nested_dict
        a = nested_dict.nested_dict()
        a['1']['2']['3'] = 3
        a['A']['B'] = 15
        self.assertEqual(str(a), '{"1": {"2": {"3": 3}}, "A": {"B": 15}}')
