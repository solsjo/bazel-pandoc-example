import argparse

from pdf2image import convert_from_path


def setup_argparse():
    parser = argparse.ArgumentParser(description='Foo')
    parser.add_argument('-o', '--output', help='Output file name', default='stdout')
    requiredNamed = parser.add_argument_group('required named arguments')
    requiredNamed.add_argument('-i', '--input', help='Input file name', required=True)
    requiredNamed.add_argument('-f', '--format', help='format', required=True)
    return parser


def main():
    parser = setup_argparse()
    args = parser.parse_args()
    input = args.input
    output = args.output
    format = args.format
    # Store Pdf with convert_from_path function
    images = convert_from_path(input)
 
    for i in range(len(images)):
        images[i].save(output, format.upper())

if __name__ == "__main__":
  main()
