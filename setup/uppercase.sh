# to convert a variable to uppercase: var = $(uppercase.sh $var)
echo "$1" | tr '[:lower:]' '[:upper:]'
