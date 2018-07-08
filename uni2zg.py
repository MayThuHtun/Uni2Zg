# -*- coding: utf-8 -*-
import re


def convert(input):
    output = input

    #########  pat-sint
    # output = re.sub(u'\u1039'u'\u1000', u'\u1060', output)
    #  ka
    output = re.sub(u'\u1039'u'\u1001', u'\u1061', output)
    #  kha
    output = re.sub(u'\u1039'u'\u1002', u'\u1062', output)
    #  ga-nge
    output = re.sub(u'\u1039'u'\u1003', u'\u1063', output)
    #  ga-gyi

    output = re.sub(u'\u1004'u'\u103a'u'\u1039', u'\u1064', output)  # kinzi
    output = re.sub(u'\u1039'u'\u1005', u'\u1065', output)
    #  sa-lone
    output = re.sub(u'\u1039'u'\u1006', u'\u1066', output)
    #  sa-lane
    output = re.sub(u'\u1039'u'\u1007', u'\u1068', output)
    #  za
    output = re.sub(u'\u1039'u'\u1008', u'\u1069', output)
    #  za-myin-zwe
    output = re.sub(u'\u1039'u'\u100b', u'\u106c', output)
    #  ta-ta-lin
    output = re.sub(u'\u1039'u'\u100c', u'\u106d', output)
    #  hta-won-bae
    output = re.sub(u'\u1039'u'\u100f', u'\u1070', output)
    #  na-gyi
    output = re.sub(u'\u1039'u'\u1010', u'\u1071', output)
    #  ta-won
    output = re.sub(u'\u1039'u'\u1011', u'\u1073', output)
    #  hta
    output = re.sub(u'\u1039'u'\u1012', u'\u1075', output)
    #  da-dwe
    output = re.sub(u'\u1039'u'\u1013', u'\u1076', output)
    #  da-out-chait
    output = re.sub(u'\u1039'u'\u1014', u'\u1077', output)
    #  na
    output = re.sub(u'\u1039'u'\u1015', u'\u1078', output)
    #  pa
    output = re.sub(u'\u1039'u'\u1016', u'\u1079', output)
    #  pha
    output = re.sub(u'\u1039'u'\u1017', u'\u107a', output)
    #  ba-htet
    output = re.sub(u'\u1039'u'\u1018', u'\u107b', output)
    #  ba
    output = re.sub(u'\u1039'u'\u1019', u'\u107c', output)
    #  ma
    output = re.sub(u'\u1039'u'\u101C', u'\u1085', output)
    #  la

    ###########

    output = output.replace('\u103A', u'\u1039')
    #  a-thet

    output = output.replace(u'\u103B', u'\u103A')
    output = output.replace(u'\u103B', u'\u107A')
    #  ya-pit

    output = output.replace(u'\u103C', u'\u103B')
    #  ya-yit

    output = output.replace(u'\u103D', '\u103C')
    #  wa-swe

    output = output.replace(u'\u103E', u'\u103D')
    output = output.replace(u'\u103E', u'\u1087')
    #  ha-htoe

    output = re.sub(u'([\u102f\u1030\u1014\u1033\u1034])(\u1037)', u'\\1\u1094', output)
    output = re.sub(u'([\u103c\u103d])(\u1037)', u'\\1\u1095', output)
    #  out-ka-myint

    output = output.replace(u'\u103F', u'\u1086')
    #  tha-gyi


    ############
    output = re.sub(u'\u102b' + u'\u1039', u'\u105a', output)
    output = re.sub(u'\u103e'u'\u102f', u'\u1088', output)  # ha htoe + t chaung ngin
    output = re.sub(u'\u103e'u'\u1030', u'\u1089', output)  # ha htoe + na chaung ngin

    ##########

    output = re.sub(u'\u100f'u'\u103a'u'\u103d', u'\u1091', output)  # ganda
    output = re.sub(u'\u100d'u'\u1039'u'\u100d', u'\u106e', output)  # da+da
    output = re.sub(u'\u100e'u'\u1039'u'\u100d', u'\u106f', output)  # da-yin-mote+kaut

    output = re.sub(u'([\u1000-\u1021])(\u103b)', u'\\2\\1', output)  # ya yit-con
    output = re.sub(u'([\u1000-\u1021])(\u1031)', u'\\2\\1', output)  # tha way htoe-con

    ######  mypattern

    output = re.sub(u'([\u1000-\u102f])(\u103c)(\u1031)', u'\\3\\1\\2', output)

    output = re.sub(u'(\u1031)(\u103b)([\u1000-\u1021])(\u103a)(\u103c)(\u103d)(\u108a)(\u1039)(\u1037)(\u102c)',
                    r'\\1\\2\\3\\4\\5\\6\\7\\8\\9\\10', output)

    return output
