#funkcja do ekstrakcji składowych opinii
def extract_feature(opinion, tag, tag_class, child=None):
    try:
        if child:
            return opinion.find(tag, tag_class).find(child).get_text().strip()
        else:
            return opinion.find(tag, tag_class).get_text().strip()
    except AttributeError:
        return None
