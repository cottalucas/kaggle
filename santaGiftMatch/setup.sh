# Function to check if the python status
exists()
{
  command -v "$1" >/dev/null 2>&1
}

if exists python3; then
	echo "python3 installed"
else
	brew install python3
fi

pip3 install pandas
pip3 install numpy
pip3 install matlibplot
