import re

def remove_accents(raw_text):
    raw_text = re.sub(u"[àáâãäå]", 'a', raw_text)
    raw_text = re.sub(u"[èéêë]", 'e', raw_text)
    raw_text = re.sub(u"[ìíîï]", 'i', raw_text)
    raw_text = re.sub(u"[òóôõö]", 'o', raw_text)
    raw_text = re.sub(u"[ùúûü]", 'u', raw_text)
    raw_text = re.sub(u"[ÁÀÃÀ]", 'A', raw_text)
    raw_text = re.sub(u"[ÉÈẼÊ]", 'E', raw_text)
    raw_text = re.sub(u"[ÍÌĨÎ]", 'I', raw_text)
    raw_text = re.sub(u"[ÓÒÕÔ]", 'O', raw_text)
    raw_text = re.sub(u"[ÚÙŨÛ]", 'U', raw_text)
    raw_text = re.sub(u"[ýÿ]", 'y', raw_text)
    raw_text = re.sub(u"[ß]", 'ss', raw_text)
    raw_text = re.sub(u"[ñ]", 'n', raw_text)
    raw_text = re.sub(u"[ç]", 'c', raw_text)
    raw_text = re.sub(u"[$]", '', raw_text)
    raw_text = re.sub(u"[ºª]", '', raw_text)
    raw_text = re.sub(u"[\~\\'\^]", '', raw_text)
    return raw_text
