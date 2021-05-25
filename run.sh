sh crawl.sh $1
python3 start.py --file source/$1.txt
cat results/*/broken.txt | sort | uniq > final/$1_broken.txt
cat results/*/output.txt > final/$1_output.txt
rm -rf results/*
