#! /bin/bash
if [ $# -ne 2 ] ; then
    echo "usage: $(basename $0) terminal nums,time counts" >&2
    exit 2
fi

if [[ $1 -lt 10 ]]; then
	for (( i = 1; i < $1 +1; i++ )); do
		touch Term-0$i
	done
else
	for x in {1..9}
	do
	    touch Term-0$x
	done

	for (( i = 10; i < $1 +1; i++ )); do
		touch Term-$i
	done
fi
echo "touch $1 files"
./rndtime.py $1 $2
echo "generate $2 random sleemtime per terminal"