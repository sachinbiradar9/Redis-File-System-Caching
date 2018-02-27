# Redis-File-System-Caching

Redis File System Caching is a File System with Redis cache for efficient read operations. A wrapper was created around Redis for features such as time_created, last_used and optimal cache replacement policy. The performance of read request for file was seen to be improved by 15%

## How to run
clone this repository using

`git clone https://github.com/sachinbiradar9/Redis-File-System-Caching.git `

create a empty directory

`mkdir mountdir`

change directory 

`cd Redis-File-System-Caching`

Then run the following command to run the python file:

`python filesystem.py ../mountdir/`

Now route into mountdir

`cd ../mountdir`

Now try any file operations. The system first tries to fetch data from cache, if its a cache miss, then data is fetched from disk and updated onto the cache

`vim example.txt`

`cat example.txt`

`rm example.txt`

`mkdir example`

`rm -rf example`
