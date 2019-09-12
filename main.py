import re
import os

MARKER = '#### DOCKER HOSTS UPDATER ####'
HOSTS_PATH = '/opt/hosts'


def string_to_array(input_string):
    dd = [(rec.group().replace("{", "").replace("}", "").split(","), rec.span()) for rec in
          re.finditer("{[^}]*}", input_string)]

    texts = []
    if len(dd) != 0:
        for i in range(len(dd)):
            if i == 0:
                if dd[0][1][0] == 0:
                    texts.append("")
                else:
                    texts.append(input_string[0:dd[0][1][0]])
            else:
                texts.append(input_string[dd[i - 1][1][1]:dd[i][1][0]])
            if i == len(dd) - 1:
                texts.append(input_string[dd[-1][1][1]:])
    else:
        texts = [input_string]

    if len(dd) > 0:
        idxs = [0] * len(dd)
        summary = []

        while idxs[0] != len(dd[0][0]):
            summary_string = ""
            for i in range(len(idxs)):
                summary_string += texts[i] + dd[i][0][idxs[i]]
            summary_string += texts[-1]
            summary.append(summary_string)
            for j in range(len(idxs) - 1, -1, -1):
                if j == len(idxs) - 1:
                    idxs[j] += 1
                if j > 0 and idxs[j] == len(dd[j][0]):
                    idxs[j] = 0
                    idxs[j - 1] += 1
    else:
        summary = texts

    return summary


def update(hosts):
    f = open(HOSTS_PATH, 'r+')
    lines = []
    skip_lines = False
    for line in f.read().split('\n'):
        if line == MARKER:
            skip_lines = not skip_lines
            continue

        if not skip_lines:
            lines.append(line)

    if hosts:
        lines.append(MARKER)
        for host in hosts:
            line = '{} {}'.format('127.0.0.1', host)
            lines.append(line)
            print(line)
        lines.append(MARKER)

    summary = '\n'.join(lines)

    f.seek(0)
    f.truncate()
    f.write(summary)
    f.close()


def handle():
    print('Recompiling...')

    value = os.environ['HOSTS_LIST']
    hosts = []

    for string in value.split(';'):
        hosts = hosts + string_to_array(string)

    update(hosts)


handle()
