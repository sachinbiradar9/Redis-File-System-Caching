# Redis-File-System-Caching
Redis File System Caching is a File System with Redis cache for efficient read operations. A wrapper was created around Redis for features such as time_created, last_used and optimal cache replacement policy. The performance of read request for file was seen to be improved by 15%

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
