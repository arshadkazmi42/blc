# BLC

- Find all the links from the response of the input link.
- Checks each link if its broken or not.
- Stores the broken links in results/*/broken.txt
- Stores all the parsed urls from response in results/*/output.txt

## Setup

```
pip install -r requirements.txt
```

## Usage

```
$ python start.py {URL}
```

## Notes

- Broken links will be stored in results directory
- You can use this command to get list of broken links

```
$ cat results/*/broken.txt | grep -v Processing | sort | uniq
```
