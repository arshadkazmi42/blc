if [ -f source/$1.txt ]; then
	echo "source/$1.txt already exists"
        exit 0
fi

DEPTH=5

# Check for input depth
if [ $2 ]; then
        DEPTH=$2
fi

echo "Using Depth: "$DEPTH

sh $BBS_PATH/subdomains/subdomains.sh $1

cat $BBS_PATH/subdomains/subdomains/$1.txt > source/$1.txt

i=1
while [ $i -le $DEPTH ]; do
    echo "Processing at depth: "$i
    cat source/$1.txt | anew crawl_old.txt > crawl_process.txt
    python3 start.py --crawl crawl_process.txt
    cat results/*/links.txt | sort | uniq > source/$1.txt
    i=$(($i+1))
done


cat results/*/links.txt | sort | uniq > source/$1.txt

rm -rf crawl_process.txt crawl_old.txt
rm -rf results/*/
