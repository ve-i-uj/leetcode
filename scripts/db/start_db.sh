docker run --rm \
    -d \
    -p 23306:3306 \
    --name leetcode-mysql \
    -e MYSQL_ROOT_PASSWORD=leetcode \
    -e MYSQL_DATABASE=leetcode \
    -e MYSQL_USER=leetcode \
    -e MYSQL_PASSWORD=leetcode \
    mysql:debian \
    mysqld --default-authentication-plugin=mysql_native_password
