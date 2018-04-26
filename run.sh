if command -v python3 &>/dev/null; then
    echo "wait a minute while thermos installs..." && .install.sh
else
    echo You need to have python 3+ installed
fi
