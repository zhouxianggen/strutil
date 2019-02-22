# coding: utf8
""" chn charset detect: utf8 or gbk
"""

def check_utf8(s, max_cnt, max_err):
    i, ni, N = 0, 0, len(s)
    cnt, err = 0, 0
    while i < N and cnt < max_cnt and err < max_err:
        c = s[i]
        clen = 0
        if c <= 0x7F:
            clen = 1
        elif 0xC0 <= c <= 0xDF and i+1 < N:
            for ni in range(i+1, i+2):
                if 0x80 <= s[ni] <= 0xBF:
                    continue
            if ni == i + 1:
                clen = 2
        elif 0xE0 <= c <= 0xEF and i+2 < N:
            for ni in range(i+1, i+3):
                if 0x80 <= s[ni] <= 0xBF:
                    continue
            if ni == i + 2:
                clen = 3
        elif 0xF0 <= c <= 0xF7 and i+3 < N:
            for ni in range(i+1, i+4):
                if 0x80 <= s[ni] <= 0xBF:
                    continue
            if ni == i + 3:
                clen = 4
        elif 0xF8 <= c <= 0xFB and i+4 < N:
            for ni in range(i+1, i+5):
                if 0x80 <= s[ni] <= 0xBF:
                    continue
            if ni == i + 4:
                clen = 5
        elif 0xFC <= c <= 0xFD and i+6 < N:
            for ni in range(i+1, i+6):
                if 0x80 <= s[ni] <= 0xBF:
                    continue
            if ni == i + 5:
                clen = 6
        else:
            pass
        
        if clen:
            i += clen
            if clen == 3:
                cnt += 1
        else:
            i += 1
            err += 1
    return i, cnt, err


def check_gbk(s, max_cnt, max_err):
    i, ni, N = 0, 0, len(s)
    cnt, err = 0, 0
    while i < N and cnt < max_cnt and err < max_err:
        c = s[i]
        clen = 0
        if c <= 0x7F:
            clen = 1
        elif 0x81 <= s[i] <= 0xFE and i+1 < N and (
                0x40 <= s[i+1] <= 0x7E or 0x80 <= s[i] <= 0xFE):
            clen = 2
        else:
            pass
        
        if clen:
            i += clen
            if clen > 1:
                cnt += 1
        else:
            i += 1
            err += 1
    return i, cnt, err


def detect_chn_charset(s):
    utf8_i, utf8_c, utf8_e = check_utf8(s, 50, 5)
    if utf8_c > 0 and utf8_e == 0:
        return 'utf8'
    if utf8_c >= 50 and utf8_e < 5:
        return 'utf8'
    
    gbk_i, gbk_c, gbk_e = check_gbk(s, 50, 5)
    if gbk_c > 0 and gbk_e == 0:
        return 'gbk'
    if gbk_c >= 50 and gbk_e < 5:
        return 'gbk'

    if utf8_e == 0:
        return 'utf8'
    
    return None
           
