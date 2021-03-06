'''@file ed_decoder_factory
contains the ed decoder factory'''

from . import speller, dnn_decoder, hotstart_decoder

def factory(decoder):
    '''gets an ed decoder class

    Args:
        decoder: the decoder type

    Returns:
        An EDDecoder class'''

    if decoder == 'speller':
        return speller.Speller
    elif decoder == 'dnn_decoder':
        return dnn_decoder.DNNDecoder
    elif decoder == 'hotstart_decoder':
        return hotstart_decoder.HotstartDecoder
    else:
        raise Exception('undefined decoder type: %s' % decoder)
