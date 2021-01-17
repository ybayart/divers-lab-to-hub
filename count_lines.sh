DIR=repo/
rm -f out
find $DIR -name '*.c' -exec cat {} \;>>out
find $DIR -name '*.h' -exec cat {} \;>>out
find $DIR -name '*.cpp' -exec cat {} \;>>out
find $DIR -name '*.hpp' -exec cat {} \;>>out
find $DIR -name '*.s' -exec cat {} \;>>out
find $DIR -name '*.yaml' -exec cat {} \;>>out
find $DIR -name '*.rb' -exec cat {} \;>>out
find $DIR -name '*.py' -exec cat {} \;>>out
find $DIR -name '*.sh' -exec cat {} \;>>out
find $DIR -name 'Dockerfile' -exec cat {} \;>>out
find $DIR -name 'docker-compose.yml' -exec cat {} \;>>out
wc out
rm -f out
