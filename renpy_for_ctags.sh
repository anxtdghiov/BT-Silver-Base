#!/bin/bash

# If you're using vim then run this to get some support for renpy in ctags.
# In gvim it'll allow you to jump to variable and label definitions.
#
# to do this, First make sure you saved your changes in this file (or it
# will tell you to). Move your cursor to the variable or label of interest
# press `shift + [' to jump to its definition. You can jump back with
# `Ctrl + t'.
#
# you can also jump there using the vim command line. type `:' and then
# ta [label/variable/screen name - without the `[]']


force=0
[ "$1" == "-f" ] && force=1

s="[ \t]*"
S="[ \t]+"

# make sure lines were not yet added already
if [ ! -e "$HOME/.ctags" -o -z "$(grep "^[-]-langdef=renpy" "$HOME/.ctags")" ]; then

    echo Adding lines to your $HOME/.ctags for renpy support
    [ -e "$HOME/.ctags" -a ! -e "$HOME/.ctags.orig" ] && cp "$HOME/.ctags" "$HOME/.ctags.orig"
    cat <<EOF >> $HOME/.ctags

--langdef=renpy
--langmap=renpy:.rpy
--regex-renpy=/^label$s([a-zA-Z0-9_]+):/\1/l,label/
--regex-renpy=/^$s\$$s([a-zA-Z0-9_]+)$s=/\1/v,variable/
--regex-renpy=/^screen$s([a-zA-Z0-9_]+):/\1/s,screen/
EOF
fi

# (re) create database
if [ -e tags -a $force -eq 0 ]; then
    echo "it seems \`ctags -R' was alredy run, use $0 -f to update database" 1>&2
else
    ctags -R
fi

# add use vims python syntax highlighting for renpy.
if [ -z "`egrep "au$S+BufRead$s,${s}BufNewFile$S+\*\.rpy$S+set$S+filetype=python" $HOME/.vimrc`" ]; then
    [ -e "$HOME/.vimrc" -a ! -e "$HOME/.vimrc.orig" ] && cp "$HOME/.vimrc" "$HOME/.vimrc.orig"
    echo "au BufRead,BufNewFile *.rpy set filetype=python" >> $HOME/.vimrc
fi

