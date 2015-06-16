#!/usr/bin/env python

import sys


def main():
    in_fname, out_fname = sys.argv[1:3]
    data = {}
    for line in open(in_fname, 'r'):
        if line.startswith('variable'):
            temp = line[:-1].split(' ')
            chrom = temp[1].split('=')[1].strip('chr')
            data[chrom] = {}
            span = int(temp[2].split('=')[1]) / 2
            continue
        elif line.startswith('track'):
            continue
        temp = line[:-1].split('\t')
        index = (int(temp[0]) + span) / 1000
        if index not in data:
            data[chrom][index] = [float(temp[1]), 1]
        else:
            data[chrom][index][0] += float(temp[1])
            data[chrom][index][1] += 1
    output = open(out_fname, 'w')
    print >> output, """{"""
    for chrom in data:
        keys = data[chrom].keys()
        keys.sort()
        print >> output, """\t%s:{\n\t\tstart:[""" % chrom
        for i in keys:
            print >> output, """\t\t\t%i,""" % (i * 1000)
        print >> output, """\t\t],\n\t\tstop:["""
        for i in keys:
            print >> output, """\t\t\t%i,""" % (i * 1000 + 1000)
        print >> output, """\t\t],\n\t\tscore:["""
        for i in keys:
            print >> output, """\t\t\t%f,""" % (data[chrom][i][0] / data[chrom][i][1])
        print >> output, """\t\t]\n\t},"""
    print >> output, """}"""
    output.close()

if __name__ == "__main__":
    main()