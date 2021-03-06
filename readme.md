# zip_dl.py

This  python script was written to crawl a downloads page and download all .zip files, organized by the author's name. It assumes that media content is organized by author on a main download splash page, similar to below:

```
--- Downloads (main page)
|
|---Author A (subpage) 
|  |
|   --- file1.zip
|   --- file2.zip
| 
|---Author B (subpage)
   |
   --- file3.zip
   --- file4.zip
```
  
Running this script will result in all .zip files being downloaded, as specified below. 


## Usage
First, you must specify the 'target_url' variable at the beginning of the file. For example: 'https://sample-domain.org/downloads/'


Second, define a parent directory for bulk downloading by modifying the variable 'parent_dir'
depending upon your OS and where you would like to store 
these files. On Mac or Linux something like: '/Users/user/bulk_download/' 
on Windows something similar to 'C:\user\music\bulk_download\'. 

The crawl() function will request each page corresponding to each author
(Author A, Author B, etc) and find all links ending in .zip. If you would 
like to download a different file type, modify the regular expression on line 36. 
Also note the regular expression on line 27, this was necessary for 
my intended use of this program, but you may need to change. Altering this line as 
shown below should suffice for most purposes: 
```angular2html
    indirect_links = soup.find_all('a', href=True)

```
