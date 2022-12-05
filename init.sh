touch start
mkdir -p pvm
rm -rf pvm
git clone https://github.com/poggingfish/pvm
mkdir -p plisp
rm -rf plisp
git clone https://github.com/poggingfish/plisp
rm start
clang start.c -o start
black=$(tput setaf 0)
echo "Resetting."
mkdir -p os
rm -r os
mkdir -p os
cd os
echo "Creating /"
mkdir -p bin
mkdir -p boot
mkdir -p dev
mkdir -p etc
mkdir -p home
mkdir -p lib
mkdir -p media
mkdir -p mnt
mkdir -p opt
mkdir -p proc
mkdir -p root
mkdir -p sbin
mkdir -p srv
mkdir -p sys
mkdir -p tmp
mkdir -p unix
mkdir -p usr
echo "Creating /usr/"
cd usr
mkdir -p include
mkdir -p lib
mkdir -p libexec
mkdir -p local
mkdir -p share
cd ..
mkdir -p var
echo "Creating /var/"
cd var
mkdir -p log
mkdir -p mail
mkdir -p spool
mkdir -p src
mkdir -p tmp
cd ..
cd ..

echo "Creating user: test"
touch os/etc/password
echo -n "test:pog" > os/etc/password
echo "test user created. Password: pog"
echo "Installing plisp"
cd plisp
sh ./install.sh
cd ..
echo
echo
tput setaf 4
echo "                                       88"
echo "                                         "               
echo            
echo "8b,dPPYba,    ,adPPYba,   8b,dPPYba,   88  8b,     ,d8  "
echo "88P'    \"8a  a8\"     \"8a  88P'   \`\"8a  88   \`Y8, ,8P'   "
echo "88       d8  8b       d8  88       88  88     )888(     "
echo "88b,   ,a8\"  \"8a,   ,a8\"  88       88  88   ,d8\" \"8b,   "
echo "88\`YbbdP\"'    \`\"YbbdP\"'   88       88  88  8P'     \`Y8  "
echo "88"                                                     
echo "88"
echo "Get started by typing ./start"