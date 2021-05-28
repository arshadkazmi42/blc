# BLC

- Find all the links from the response of the input link.
- Checks each link if its broken or not.
- Stores the broken links in `results/*/broken.txt`
- Stores all the parsed urls from response in `results/*/output.txt`

## Prerequisite

1. Install anew. This will be needed for crawl.sh script
https://github.com/tomnomnom/anew

## Setup

```
pip install -r requirements.txt
```

## Usage

```
$ python start.py --file {FILE_NAME}
```

**Example**

```
$ python start.py --file hackeronne-links.txt
```

### For crawling links

```
$ python start.py --crawl {FILE_NAME} {DEPTH}
```

**Example**

```
$ python start.py --crawl hackerone-subdomains.txt 5
```


## Notes

- Broken links will be stored in results directory
- You can use this command to get list of broken links

```
$ cat results/*/broken.txt | grep -v Processing | sort | uniq
```


