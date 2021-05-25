if [ -f source/$1.txt ]; then
	echo "source/$1.txt already exists"
        exit 0
fi

sh $BBS_PATH/subdomains/subdomains.sh $1

python3 start.py --crawl $BBS_PATH/subdomains/subdomains/$1.txt
cat results/*/links.txt | sort | uniq > source/$1.txt
rm -rf results/*/
