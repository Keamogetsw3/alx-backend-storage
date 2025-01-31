# 0x02. Redis Basic

## Back-end
### Redis

**Weight:** 1  
**Project Duration:** Oct 23, 2024 6:00 AM - Oct 24, 2024 6:00 AM  
An auto review will be launched at the deadline.

## In a nutshell…
- **Auto QA review:** 0.0/27 mandatory & 0.0/6 optional  
- **Altogether:** 0.0%  
- **Mandatory:** 0.0%  
- **Optional:** 0.0%  
- **Calculation:** 0.0% + (0.0% * 0.0%) == 0.0%  

## Resources
Read or watch:
- [Redis Crash Course Tutorial](https://example.com)
- [Redis Commands](https://example.com)
- [Redis Python Client](https://example.com)
- [How to Use Redis With Python](https://example.com)

## Learning Objectives
- Learn how to use Redis for basic operations.
- Learn how to use Redis as a simple cache.

## Requirements
- All files will be interpreted/compiled on Ubuntu 18.04 LTS using Python 3.7.
- All files should end with a new line.
- A README.md file at the root of the project folder is mandatory.
- The first line of all files should be exactly:  
  \`\`\`python
  #!/usr/bin/env python3
  \`\`\`
- Your code should follow pycodestyle (version 2.5).
- All modules, classes, functions, and methods should have proper documentation.
- Functions and coroutines must be type-annotated.

## Install Redis on Ubuntu 18.04
\`\`\`sh
$ sudo apt-get -y install redis-server
$ pip3 install redis
$ sed -i "s/bind .*/bind 127.0.0.1/g" /etc/redis/redis.conf
\`\`\`

## Use Redis in a Container
By default, the Redis server is stopped when starting a container. Start it with:  
\`\`\`sh
$ service redis-server start
\`\`\`