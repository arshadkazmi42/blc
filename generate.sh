TOOLS_PATH=$BBS_PATH/tools
SUBDOMAINS_PATH=$BBS_PATH/subdomains
JS_PATH=$BBS_PATH/getJS
WBM_PATH=$BBS_PATH/wbm

if [ -f source/$1.txt ]; then
	exit 0
fi

sh $SUBDOMAINS_PATH/subdomains.sh $1
sh $JS_PATH/run.sh $1
sh $WBM_PATH/get.sh $1

# Merge JS and Live domains
cat $SUBDOMAINS_PATH/subdomains/$1.txt $JS_PATH/results/$1"-js.txt" $WBM_PATH/output/$1.txt | sort | uniq > source/$1.txt


