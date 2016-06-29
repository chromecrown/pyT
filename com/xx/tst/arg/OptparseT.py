#coding=utf-8

from optparse import OptionParser
from optparse import OptionGroup

"""
localhost:arg wq$ python OptparseT.py -h
Usage: OptparseT.py [options]

Options:
  -h, --help            show this help message and exit
  -f FILE, --file=FILE  write report to FILE
  -q, --quiet           don't print status messages to stdout

  Dangerous Options:
    Caution: use these options at your own risk.  It is believed that some
    of them bite.

    -g                  Group option.

  Debug Options:
    -d, --debug         Print debug information
    -s, --sql           Print all SQL statements executed
    -e                  Print every action done
"""

parser = OptionParser()
parser.add_option("-f", "--file", dest="filename",
                  help="write report to FILE", metavar="FILE")
parser.add_option("-q", "--quiet",
                  action="store_false", dest="verbose", default=True,
                  help="don't print status messages to stdout")
parser.add_option("-m","--email",dest="mail",help="please type right email address")
                                                                                                                                                             
group = OptionGroup(parser, "Dangerous Options",
                    "Caution: use these options at your own risk.  "
                    "It is believed that some of them bite.")
group.add_option("-g", action="store_true", dest="grp",help="Group option.")
parser.add_option_group(group)
                     
group = OptionGroup(parser, "Debug Options")
group.add_option("-d", "--debug", action="store_true",dest="dbg",
                 help="Print debug information")
group.add_option("-s", "--sql",dest="sq",
                 help="Print all SQL statements executed")
group.add_option("-e", dest="excep", action="store_true", help="Print every action done")
parser.add_option_group(group)

(options, args) = parser.parse_args()
print "options:",options
print "args:",args
print "options.except:",options.excep
print "options.verbose:",options.verbose