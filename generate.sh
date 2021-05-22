TOOLS_PATH=$BBS_PATH/tools
SUBDOMAINS_PATH=$BBS_PATH/subdomains
JS_PATH=$BBS_PATH/getJS
GAU_PATH=$BBS_PATH/gau

if [ -f source/$1.txt ]; then
	exit 0
fi

sh $SUBDOMAINS_PATH/subdomains.sh $1
sh $JS_PATH/run.sh $1
sh $GAU_PATH/get.sh $1

# Merge JS and Live domains
cat $SUBDOMAINS_PATH/subdomains/$1.txt $JS_PATH/results/$1"-js.txt" $GAU_PATH/gau/$1.txt | sort | uniq > source/$1.txt


