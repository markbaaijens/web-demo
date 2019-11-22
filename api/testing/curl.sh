#!/bin/bash
#
# Usage:
#  chown +x curl.sh
#  ./curl.sh
#  (or)
#  ./curl.sh | grep -i "error"
#
debug=0  # Set to 1 to show curl-statements

run_test() {
    result=$($2 -s | grep "$3") 
    if [ "$result" != "" ]
    then
        echo "[$1] returns [$3] => OK"
    else
        echo "[$1] returns [$3] => Error"
    fi
    if [ "$debug" == 1 ]
    then
        echo "$2"
        echo
    fi
}

# GET /
title="GET /"
test_cmd="curl -i http://localhost:5000"
test_value="API-demo"
run_test "$title" "$test_cmd" "$test_value"

test_cmd="curl -i http://localhost:5000"
test_value="HTTP/1.0 200 OK"
run_test "$title" "$test_cmd" "$test_value"

# PATCH /
title="PATCH /"
test_cmd="curl -i http://localhost:5000 -X PATCH"
test_value="HTTP/1.0 405 METHOD NOT ALLOWED"
run_test "$title" "$test_cmd" "$test_value"

# GET /books
title="GET /books"
test_cmd="curl -i http://localhost:5000/books"
test_value="HTTP/1.0 200 OK"
run_test "$title" "$test_cmd" "$test_value"

test_cmd="curl -i http://localhost:5000/books"
test_value="Content-Length: 246"
run_test "$title" "$test_cmd" "$test_value"

# GET /books/1"
title="GET /books/1"
test_cmd="curl -i http://localhost:5000/books/1"
test_value="HTTP/1.0 200 OK"
run_test "$title" "$test_cmd" "$test_value"

test_cmd="curl -i http://localhost:5000/books/1"
test_value="Content-Length: 82"
run_test "$title" "$test_cmd" "$test_value"

# GET /books/4
title="GET /books/4 (record does not exist)"
test_cmd="curl -i http://localhost:5000/books/4"
test_value="HTTP/1.0 404 NOT FOUND"
run_test "$title" "$test_cmd" "$test_value"

# POST /books # TODO Should be OK but is not
title="POST /books"
test_cmd="curl -i http://localhost:5000/books -X POST -H "\""Content-Type: application/json"\"" -d '{"\""isbn"\"": 5, "\""name"\"":"\""Name"\""}' "
test_value="HTTP/1.0 201 CREATED"
run_test "$title" "$test_cmd" "$test_value"

# POST /books 
title="POST /books (without required field)"
test_cmd="curl -i http://localhost:5000/books -X POST -H "\""Content-Type: application/json"\"" -d '{"\""name"\"":"\""Name"\""}' "
test_value="HTTP/1.0 400 BAD REQUEST"
run_test "$title" "$test_cmd" "$test_value"

# PATCH /books/3  #TODO Should be OK but is not
title="PATCH /books/3"
test_cmd="curl -i http://localhost:5000/books/3 -X PATCH -H "\""Content-Type: application/json"\"" -d '{"\""name"\"":"\""Name66"\""}' "
test_value="HTTP/1.0 200 OK"
run_test "$title" "$test_cmd" "$test_value"

# DELETE /books/3 
title="DELETE /books/3"
test_cmd="curl -i http://localhost:5000/books/3 -X DELETE"
test_value="HTTP/1.0 200 OK"
run_test "$title" "$test_cmd" "$test_value"

# DELETE /books/3 
title="DELETE /books/3 (second deletion, record is already deleted)"
test_cmd="curl -i http://localhost:5000/books/3 -X DELETE"
test_value="HTTP/1.0 404 NOT FOUND" 
run_test "$title" "$test_cmd" "$test_value"

# PATCH /books/3 (empty body) 
title="PATCH /books/3 (empty body)"
test_cmd="curl -i http://localhost:5000/books/3 -X PATCH"
test_value="HTTP/1.0 400 BAD REQUEST"
run_test "$title" "$test_cmd" "$test_value"

# POST /books (empty body) 
title="POST /books (empty body)"
test_cmd="curl -i http://localhost:5000/books -X POST"
test_value="HTTP/1.0 400 BAD REQUEST"
run_test "$title" "$test_cmd" "$test_value"
