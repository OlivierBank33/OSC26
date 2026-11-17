"""Remplace la liste d'options d'une question (identifiée par le début de son texte) dans un fichier de banque."""
import json, sys
def setopts(path, fixes):
    s = open(path).read()
    for start, opts in fixes.items():
        i = s.find('"' + start)
        assert i >= 0, start
        a = s.find('[', i); depth = 0; j = a
        while True:
            ch = s[j]
            if ch == '[': depth += 1
            elif ch == ']':
                depth -= 1
                if depth == 0: break
            j += 1
        s = s[:a] + json.dumps(opts, ensure_ascii=False) + s[j+1:]
    open(path, 'w').write(s)
