import json
import argparse
from trainer import train


def main():
    args = setup_parser().parse_args()
    param = load_json(args.config)
    args = vars(args)  # Converting argparse Namespace to a dict.
    args.update(param)  # Add parameters from json

    train(args)


def load_json(settings_path):
    with open(settings_path) as data_file:
        param = json.load(data_file)

    return param


def setup_parser():
    parser = argparse.ArgumentParser(description='Reproduce of multiple continual learning algorthms.')
    parser.add_argument('--config', type=str, default='./exps/ewc_2stage.json',
                        help='Json file of settings.')
    parser.add_argument('--datatype', type=str, default='lt',
                        help='Type of data')
    parser.add_argument('--exp', type=str, default='test',
                        help='Type of data')
    return parser



if __name__ == '__main__':
    main()
