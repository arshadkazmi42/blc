sh generate.sh $1
cat source/$1.txt | xargs -I {} python3 start.py {}
