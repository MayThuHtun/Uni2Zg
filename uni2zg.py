# -*- coding: utf-8 -*-
import re


def convert(input):
    output = input

    output = output.replace(u'\u1009', u'\u106A')
    #  nya-lay

    output = output.replace(u'\u100A', u'\u106B')
    #  nya

    output = output.replace(u'\u1014', '\u108F')
    #  na

    output = output.replace(u'\u101B', u'\u1009')
    #  ya-kaut

    output = output.replace('\u103A', u'\u1039')
    #  a-thet

    output = output.replace(u'\u103F', u'\u1086')
    #  tha-gyi

    output = output.replace(u'\u102F', u'\u1033')
    #  1chaung-ngin

    output = output.replace(u'\u1030', u'\u1034')
    #  2chaung-ngin

    output = output.replace(u'\u1037', u'\u1094')
    output = output.replace(u'\u1037', u'\u1095')
    #  out-ka-myint

    output = output.replace(u'\u103E', u'\u103D')
    output = output.replace(u'\u103E', u'\u107D')
    #  ha-htoe

    output = output.replace(u'\u103D', '\u103C')
    #  wa-swe

    output = output.replace(u'\u103C', u'\u103B')
    output = output.replace(u'\u103C', u'\u107E')
    output = output.replace(u'\u103C', u'\u107F')
    output = output.replace(u'\u103C', u'\u1080')
    output = output.replace(u'\u103C', u'\u1081')
    output = output.replace(u'\u103C', u'\u1082')
    output = output.replace(u'\u103C', u'\u1083')
    output = output.replace(u'\u103C', u'\u1084')
    #  ya-yit

    output = output.replace(u'\u103B', u'\u103A')
    output = output.replace(u'\u103B', u'\u107A')
    #  ya-pit





return output
