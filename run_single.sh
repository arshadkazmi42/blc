sh crawl_single.sh $1 $2
python3 start.py --file source/$1.txt
cat results/*/broken.txt | sort | uniq > final/$1_broken.txt
cat results/*/output.txt > final/$1_output.txt
rm -rf results/*

echo "Completed for "$1 | $BBS_PATH/tools/notify
