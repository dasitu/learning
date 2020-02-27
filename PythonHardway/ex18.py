# -*- coding: utf-8 -*-


def print_two(*args):
    arg1, arg2 = args
    print "arg1: %r, arg2: %r" % (arg1, arg2)


def print_two_again(arg1, arg2):
    print "arg1: %r, arg2: %r" % (arg1, arg2)


def print_one(arg):
    print "arg: %r" % arg


def print_none():
    print "No args"

print_none()
print_one("One Arg")
print_two("Zed", "Shaw")
print_two_again("Zed1","Shaw2")