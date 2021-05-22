# BLC

Checks link is broken or not and stores in respective files

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
