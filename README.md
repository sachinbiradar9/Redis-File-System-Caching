# Redis File System Caching
:trophy: Won at [HackIllinois 2018](https://devpost.com/software/redis-file-system-caching)

Redis File System Caching is a File System with Redis cache for efficient read operations. A wrapper is created around Redis for features such as time_created, last_used and optimal cache eviction policy. Whenever a file is read the content is cached in redis, when the file is edited or deleted the content in redis is changed accordingly. The performance of read request for file was seen to be improved by 15%

## Installation
`pip install redis`  
`pip install fusepy`

## Usage
create a empty directory  
`mkdir mountdir`

Run the caching system  
`git clone https://github.com/sachinbiradar9/Redis-File-System-Caching.git`  
`python filesystem.py ../mountdir/`

Now change directory to mountdir  
`cd ../mountdir`

Try any file operations  
`vim example.txt`  
`cat example.txt`  
`rm example.txt`  
`mkdir example`  
`rm -rf example`
