#!/bin/bash
echo "Installing somesites..."
pip install beautifulsoup4 requests --break-system-packages
echo 'python $HOME/scanner.py' > $PREFIX/bin/somesites
chmod +x $PREFIX/bin/somesites
echo "Installation complete! Type 'somesites' to run."
