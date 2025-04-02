
## Getting Started

Optional but recommended > Create a new Python virtual environement then activate it

From the root of the project directory run:
pip install -r requirements.txt

### Prerequisites

Python 3.8+

### Installing

From the root of the project directory run:
pip install -r requirements.txt

Add your tinypng api key to your environment variables under the key `TINYPNG_API_KEY`
example: export TINYPNG_API_KEY="<YOUR API KEY HERE>"

## Usage

Put all the files your want copied to .jpg in the /input directory
Put all the files your want copied to thumbnails in the /input_thumbs directory
Run from the `src` directory:

python3 tpu_main.py

When the script is done the new files will be located in the output directory

## Running the tests

## Built With

## Contributing

Please do!

## Authors

Kevin Fink

## License

MIT

## Acknowledgments

TinyPNG for their generosity in allowing some free access to their API.
