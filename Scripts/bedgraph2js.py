#!/usr/bin/env python

import sys


def main():
    in_fname, out_fname = sys.argv[1:3]
    data = {}
    for line in open(in_fname, 'r'):
        temp = line[:-1].split('\t')
        if len(temp) < 4:
            continue
        temp[0] = temp[0].strip('chr')
        if temp[0] not in data:
            data[temp[0]] = []
        data[temp[0]].append([temp[1], temp[2], temp[3]])
    output = open(out_fname, 'w')
    print >> output, """{"""
    for chrom in data:
        print >> output, """\t%s:{\n\t\tstart:[""" % chrom
        for i in range(len(data[chrom])):
            print >> output, """\t\t\t%s,""" % data[chrom][i][0]
        print >> output, """\t\t],\n\t\tstop:["""
        for i in range(len(data[chrom])):
            print >> output, """\t\t\t%s,""" % data[chrom][i][1]
        print >> output, """\t\t],\n\t\tscore:["""
        for i in range(len(data[chrom])):
            print >> output, """\t\t\t%s,""" % data[chrom][i][2]
        print >> output, """\t\t]\n\t},"""
    print >> output, """}"""
    output.close()

if __name__ == "__main__":
    main()