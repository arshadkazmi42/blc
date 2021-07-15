DEPTH=3

echo "Using Depth: "$DEPTH

mkdir source
mkdir results
cat ../output/active_urls.txt > ../output/crawl_urls.txt

i=1
while [ $i -le $DEPTH ]; do
    echo "Processing at depth: "$i
    cat ../output/crawl_urls.txt | anew crawl_old.txt > crawl_process.txt
    python3 start.py --crawl crawl_process.txt
    cat results/*/links.txt | sort | uniq >  ../output/crawl_urls.txt
    i=$(($i+1))
done


cat results/*/links.txt | sort | uniq > ../output/crawl_urls.txt

rm -rf crawl_process.txt crawl_old.txt
rm -rf results/*/
