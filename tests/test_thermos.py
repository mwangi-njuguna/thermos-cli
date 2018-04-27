"""Tests for our main thermos CLI module."""


from subprocess import PIPE, Popen as popen
from unittest import TestCase

from thermos import __version__ as VERSION


class TestHelp(TestCase):
    def test_returns_usage_information(self):
        outp = popen(['thermos', '-h'], stdout=PIPE).communicate()[0]
        output = outp.decode('utf-8')
        self.assertTrue('Usage:' in output)

        outp = popen(['thermos', '--help'], stdout=PIPE).communicate()[0]
        output = outp.decode('utf-8')
        self.assertTrue('Usage:' in output)


class TestVersion(TestCase):
    def test_returns_version_information(self):
        output = popen(['thermos', '--version'], stdout=PIPE).communicate()[0]
        self.assertEqual(output.strip().decode('utf-8'), VERSION)
